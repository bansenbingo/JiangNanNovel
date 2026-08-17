[CmdletBinding()]
param(
    [ValidateSet('codex', 'claude', 'gemini', 'opencode', 'cursor', 'copilot')]
    [string]$Agent = $env:JIANGNANNOVEL_AGENT,
    [switch]$List,
    [switch]$Version,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'
$InstallerVersion = '1.2.0'
$SkillName = 'JiangNanNovel'
$SkillSubdir = 'skill'
$DefaultRepoUrl = 'https://github.com/bansenbingo/JiangNanNovel.git'
$RepoUrl = if ($env:JIANGNANNOVEL_REPO_URL) { $env:JIANGNANNOVEL_REPO_URL } else { $DefaultRepoUrl }
$AgentHome = if ($env:JIANGNANNOVEL_HOME) { $env:JIANGNANNOVEL_HOME } else { $HOME }
$MarkerFile = '.jiangnannovel-revision'

function Show-Usage {
    @'
Install or update the complete JiangNanNovel skill bundle for a local agent CLI.

Usage:
  .\install.ps1 [-Agent AGENT]
  .\install.ps1 -List
  .\install.ps1 -Version

Without -Agent, the script scans PATH and prompts when multiple agents exist.
Run the same command again to check for and install bundle updates.
'@
}

function Get-DetectedAgents {
    $candidates = @(
        [pscustomobject]@{ Id = 'codex';   Command = 'codex';        Label = 'Codex';              Root = [IO.Path]::Combine($AgentHome, '.agents', 'skills') },
        [pscustomobject]@{ Id = 'claude';  Command = 'claude';       Label = 'Claude Code';        Root = [IO.Path]::Combine($AgentHome, '.claude', 'skills') },
        [pscustomobject]@{ Id = 'gemini';  Command = 'gemini';       Label = 'Gemini CLI';         Root = [IO.Path]::Combine($AgentHome, '.gemini', 'skills') },
        [pscustomobject]@{ Id = 'opencode'; Command = 'opencode';     Label = 'OpenCode';           Root = [IO.Path]::Combine($AgentHome, '.config', 'opencode', 'skills') },
        [pscustomobject]@{ Id = 'cursor';   Command = 'cursor-agent'; Label = 'Cursor Agent';       Root = [IO.Path]::Combine($AgentHome, '.cursor', 'skills') },
        [pscustomobject]@{ Id = 'copilot';  Command = 'copilot';      Label = 'GitHub Copilot CLI'; Root = [IO.Path]::Combine($AgentHome, '.copilot', 'skills') }
    )

    @($candidates | Where-Object { Get-Command $_.Command -ErrorAction SilentlyContinue })
}

function Show-DetectedAgents([array]$DetectedAgents) {
    if ($DetectedAgents.Count -eq 0) {
        Write-Output 'No compatible agent CLI was found on PATH.'
        return
    }

    Write-Output 'Compatible agent CLIs found on PATH:'
    for ($i = 0; $i -lt $DetectedAgents.Count; $i++) {
        Write-Output ('  {0}. {1,-20} {2}' -f ($i + 1), $DetectedAgents[$i].Label, $DetectedAgents[$i].Root)
    }
}

function Select-Agent([array]$DetectedAgents, [string]$RequestedAgent) {
    if ($DetectedAgents.Count -eq 0) {
        throw 'No compatible agent CLI was found on PATH.'
    }

    if ($RequestedAgent) {
        $selected = @($DetectedAgents | Where-Object { $_.Id -eq $RequestedAgent })
        if ($selected.Count -eq 0) {
            throw "Agent '$RequestedAgent' is not installed or is not on PATH. Run with -List to inspect detected agents."
        }
        return $selected[0]
    }

    if ($DetectedAgents.Count -eq 1) {
        return $DetectedAgents[0]
    }

    Show-DetectedAgents $DetectedAgents
    $choice = Read-Host "Select an agent [1-$($DetectedAgents.Count)]"
    $number = 0
    if (-not [int]::TryParse($choice, [ref]$number) -or $number -lt 1 -or $number -gt $DetectedAgents.Count) {
        throw "Invalid selection: $choice"
    }
    $DetectedAgents[$number - 1]
}

function Get-TreeManifest([string]$Root) {
    if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
        return $null
    }

    $resolvedRoot = (Resolve-Path -LiteralPath $Root).Path.TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
    $entries = foreach ($file in Get-ChildItem -LiteralPath $resolvedRoot -File -Recurse | Where-Object { $_.Name -ne $MarkerFile }) {
        $relative = $file.FullName.Substring($resolvedRoot.Length).TrimStart([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
        '{0}`t{1}' -f $relative, (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
    }
    ($entries | Sort-Object) -join "`n"
}

function Install-Skill([string]$Source, [string]$Revision, [pscustomobject]$SelectedAgent) {
    $skillsRoot = $SelectedAgent.Root
    $destination = Join-Path $skillsRoot $SkillName
    $stage = Join-Path $skillsRoot ".$SkillName.stage.$PID"
    $backup = Join-Path $skillsRoot ".$SkillName.backup.$PID"

    New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
    if ((Test-Path -LiteralPath $stage) -or (Test-Path -LiteralPath $backup)) {
        throw "A temporary install path already exists under $skillsRoot."
    }

    $sourceManifest = Get-TreeManifest $Source
    $destinationManifest = Get-TreeManifest $destination
    if ($null -ne $destinationManifest -and $sourceManifest -ceq $destinationManifest) {
        Set-Content -LiteralPath (Join-Path $destination $MarkerFile) -Value $Revision -Encoding ASCII
        Write-Output "$SkillName is already up to date in $destination"
        return
    }

    Copy-Item -LiteralPath $Source -Destination $stage -Recurse
    Set-Content -LiteralPath (Join-Path $stage $MarkerFile) -Value $Revision -Encoding ASCII

    if (-not (Test-Path -LiteralPath $destination)) {
        Move-Item -LiteralPath $stage -Destination $destination
        Write-Output "$SkillName installed for $($SelectedAgent.Label) at $destination"
        return
    }

    Move-Item -LiteralPath $destination -Destination $backup
    try {
        Move-Item -LiteralPath $stage -Destination $destination
        Remove-Item -LiteralPath $backup -Recurse -Force
        Write-Output "$SkillName updated for $($SelectedAgent.Label) at $destination"
    }
    catch {
        if (-not (Test-Path -LiteralPath $destination) -and (Test-Path -LiteralPath $backup)) {
            Move-Item -LiteralPath $backup -Destination $destination
        }
        throw 'Update failed; the previous installation was restored.'
    }
}

if ($Help) {
    Show-Usage
    exit 0
}
if ($Version) {
    Write-Output $InstallerVersion
    exit 0
}

$detectedAgents = Get-DetectedAgents
if ($List) {
    Show-DetectedAgents $detectedAgents
    exit 0
}

$selectedAgent = Select-Agent $detectedAgents $Agent
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git 2.25 or newer is required.'
}

$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("jiangnannovel-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tempRoot | Out-Null

try {
    $repoPath = Join-Path $tempRoot 'repo'
    Write-Output "Checking the latest $SkillName skill bundle..."
    & git clone --quiet --depth 1 --filter=blob:none --sparse $RepoUrl $repoPath
    if ($LASTEXITCODE -ne 0) { throw "Unable to clone $RepoUrl" }
    & git -C $repoPath sparse-checkout set $SkillSubdir
    if ($LASTEXITCODE -ne 0) { throw "Unable to fetch $SkillSubdir" }

    $source = Join-Path $repoPath $SkillSubdir
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
        throw 'The downloaded bundle does not contain its root SKILL.md.'
    }
    if (-not (Test-Path -LiteralPath (Join-Path $source 'JiangNanNovel\SKILL.md') -PathType Leaf)) {
        throw 'The downloaded bundle does not contain the author Skill.'
    }
    if (-not (Test-Path -LiteralPath (Join-Path $source 'characters\lu_mingfei\SKILL.md') -PathType Leaf)) {
        throw 'The downloaded bundle does not contain its character Skills.'
    }

    $revision = (& git -C $repoPath rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0) { throw 'Unable to read the downloaded revision.' }

    Install-Skill $source $revision $selectedAgent
    Write-Output "Restart $($selectedAgent.Label) if the skill is not immediately visible."
}
finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
