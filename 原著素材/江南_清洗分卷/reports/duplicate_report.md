# 江南语料去重报告

## 既有原著基线

- `/Users/teddyjiang/Documents/GitHub/JiangNanNovel/原著素材/龙族/《龙族》（实体版1-4部全本）.txt`：2,138,172 字，SHA-256 `c52b6641a46cf8de12d65d6b12e62dc9851ea506882ee6ac2fa58b9e2031028b`
- `/Users/teddyjiang/Documents/GitHub/JiangNanNovel/原著素材/龙族/龙族Ⅴ·悼亡者归来.txt`：752,344 字，SHA-256 `d8f78ef1f3f863df8e014902d16b13ffacc55a9d1c5ebaab1b2b48805c4599c6`
- `/Users/teddyjiang/Documents/GitHub/JiangNanNovel/原著素材/九州缥缈录/九州缥缈录.txt`：1,165,386 字，SHA-256 `167c95006cd9805a6684ad4c6fe437f17d44a6fe582f78cb0309b8e18aa5e1f9`
- `/Users/teddyjiang/Documents/GitHub/JiangNanNovel/原著素材/天之炽/天之炽（三册全）.txt`：640,321 字，SHA-256 `ad35d8b7dd33627f67f2b2c6a78e17fb0745ba14a785cba50fff1e138a4d9726`

## 完整文件级排除

- `《龙与少年游（出书版）》作者：江南【诗歌散文】.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=87.4%；duplicate_of=`江南作品合集/[06]散文随笔/《龙与少年游》江南散文随笔精选.txt`
- `《龙族1·火之晨曦》作者：江南.txt`：`excluded_reference_duplicate`；reference=99.9%，internal=0.0%
- `《龙族2·悼亡者之瞳》作者：江南.txt`：`excluded_reference_duplicate`；reference=99.9%，internal=0.0%
- `《龙族3·黑月之潮》作者：江南.txt`：`excluded_reference_duplicate`；reference=99.2%，internal=0.0%
- `《龙族·哀悼之翼(龙族前传)》作者：江南.txt`：`excluded_after_block_dedup`；reference=0.0%，internal=79.2%
- `《龙族Ⅳ：奥丁之渊》作者：江南.txt`：`excluded_reference_duplicate`；reference=99.4%，internal=0.0%
- `九州·缥缈录.txt`：`excluded_reference_duplicate`；reference=99.7%，internal=0.0%
- `天之炽Ⅱ：女武神1.txt`：`excluded_reference_variant`；reference=39.9%，internal=0.0%
- `天之炽Ⅱ：女武神2.txt`：`excluded_after_block_dedup`；reference=57.9%，internal=0.0%
- `此间的少年Ⅰ.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=95.5%；duplicate_of=`江南作品合集/[04]其它长篇小说/《此间的少年》.txt`
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅰ：蛮荒》.txt`：`excluded_reference_duplicate`；reference=93.6%，internal=0.0%
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅱ：苍云古齿》.txt`：`excluded_reference_duplicate`；reference=97.3%，internal=0.0%
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅲ：天下名将》.txt`：`excluded_reference_duplicate`；reference=97.9%，internal=0.0%
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅳ：辰月之征》.txt`：`excluded_reference_duplicate`；reference=90.2%，internal=0.0%
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅴ：一生之盟》.txt`：`excluded_reference_duplicate`；reference=85.1%，internal=0.0%
- `江南作品合集/[01]九州长篇小说/《九州缥缈录Ⅵ：豹魂》.txt`：`excluded_reference_duplicate`；reference=95.4%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《天之炽 女武神2》.txt`：`excluded_reference_duplicate`；reference=98.2%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《天之炽Ⅰ红龙的归来》..txt`：`excluded_reference_variant`；reference=24.1%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《天之炽Ⅱ：女武神》.txt`：`excluded_reference_duplicate`；reference=98.2%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族IV 奥丁之渊》.txt`：`excluded_reference_duplicate`；reference=99.8%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅰ：火之晨曦》.txt`：`excluded_reference_duplicate`；reference=76.7%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅱ悼亡者之瞳》..txt`：`excluded_reference_duplicate`；reference=87.6%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅱ：悼亡者之瞳》.txt`：`excluded_reference_duplicate`；reference=88.5%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅲ：黑月之潮（上）》.txt`：`excluded_reference_duplicate`；reference=77.1%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅲ：黑月之潮（下）》.txt`：`excluded_reference_duplicate`；reference=87.3%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅲ：黑月之潮（中）》.txt`：`excluded_reference_variant`；reference=70.9%，internal=0.0%
- `江南作品合集/[04]其它长篇小说/《龙族Ⅲ：黑月之潮（全本）》.txt`：`excluded_reference_duplicate`；reference=79.5%，internal=0.0%
- `江南作品合集/[06]散文随笔/《我们存在的碑记》.txt`：`excluded_after_block_dedup`；reference=0.0%，internal=85.5%
- `江南作品合集/[08]文论/《关于〈此间〉的一些问题》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=95.4%；duplicate_of=`江南作品合集/[04]其它长篇小说/《此间的少年》.txt`
- `江南作品合集/[09]影评/《从〈夜宴〉开始》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=99.4%；duplicate_of=`江南作品合集/[11]刊首语/《幻想1+1》2006年11月刊首语【从《夜宴》开始】.txt`
- `江南作品合集/[10]序跋/《〈光明皇帝〉自序或跋》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=98.9%；duplicate_of=`江南作品合集/[03]武侠小说/《光明皇帝·业火》.txt`
- `江南作品合集/[10]序跋/《〈台北红玫瑰〉——代〈蝴蝶风暴〉自序.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=99.2%；duplicate_of=`江南作品合集/[04]其它长篇小说/《蝴蝶风暴Ⅰ：猎犬狐》.txt`
- `江南作品合集/[10]序跋/《〈此间的少年〉后记》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=98.7%；duplicate_of=`江南作品合集/[04]其它长篇小说/《此间的少年》.txt`
- `江南作品合集/[10]序跋/《〈涿鹿〉跋》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=99.1%；duplicate_of=`江南作品合集/[04]其它长篇小说/《涿鹿·炎的最后王孙》.txt`
- `江南作品合集/[10]序跋/《光明神话——写给〈光明皇帝〉前传的后记》.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=97.3%；duplicate_of=`江南作品合集/[03]武侠小说/《光明皇帝·业火》.txt`
- `江南作品合集/[11]刊首语/《九州幻想》06年3月刊首语【春天来了】.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=99.4%；duplicate_of=`江南作品合集/[06]散文随笔/《当春乃发生》.txt`
- `江南作品合集/[11]刊首语/《龙文·漫小说》Vol.29刊首语【我想我很累了】.txt`：`excluded_internal_duplicate`；reference=0.0%，internal=99.7%；duplicate_of=`江南作品合集/[06]散文随笔/《我想我很累了——写在《九州缥缈录》再版的时候》.txt`
- `江南作品合集/[14]其它/《天之炽 II 女武神》（连载版）.txt`：`excluded_reference_duplicate`；reference=99.0%，internal=0.0%
- `江南作品合集/[14]其它/《天之炽Ⅰ红龙的归来》（连载版）..txt`：`excluded_reference_duplicate`；reference=96.2%，internal=0.0%
- `江南作品合集/[14]其它/《天之炽第一卷：炽天的骑者》（连载版）.txt`：`excluded_reference_duplicate`；reference=94.1%，internal=0.0%
- `江南作品合集/[作品目录].txt`：`excluded_metadata`；reference=0.0%，internal=0.0%
- `江南作品合集/[作者简介].txt`：`excluded_metadata`；reference=0.0%，internal=0.0%
- `江南作品合集/[合集说明].txt`：`excluded_metadata`；reference=0.0%，internal=0.0%
- `江南作品合集/[更新记录].txt`：`excluded_metadata`；reference=0.0%，internal=0.0%
- `龙族5悼亡者归来.txt`：`excluded_reference_duplicate`；reference=99.3%，internal=0.0%
- `龙族全集.txt`：`excluded_reference_duplicate`；reference=97.7%，internal=0.0%

## 部分段落去重

- `上海堡垒.txt`：既有原著 0 段；集合内部 1547 段
- `天之炽I：红龙的归来.txt`：既有原著 7 段；集合内部 15 段
- `江南作品合集/[02]九州短篇小说/《一生之盟》.txt`：既有原著 305 段；集合内部 0 段
- `江南作品合集/[02]九州短篇小说/《九州飘零书·海市》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[02]九州短篇小说/《威武王》.txt`：既有原著 111 段；集合内部 0 段
- `江南作品合集/[02]九州短篇小说/《星野变》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[02]九州短篇小说/《殇阳血》.txt`：既有原著 218 段；集合内部 0 段
- `江南作品合集/[02]九州短篇小说/《燕子焚》.txt`：既有原著 0 段；集合内部 6 段
- `江南作品合集/[02]九州短篇小说/《猎风》.txt`：既有原著 0 段；集合内部 150 段
- `江南作品合集/[02]九州短篇小说/《虎牙》.txt`：既有原著 47 段；集合内部 11 段
- `江南作品合集/[04]其它长篇小说/《天之炽Ⅰ：红龙的归来》.txt`：既有原著 1036 段；集合内部 0 段
- `江南作品合集/[04]其它长篇小说/《此间的少年Ⅱ》.txt`：既有原著 0 段；集合内部 25 段
- `江南作品合集/[04]其它长篇小说/《蝴蝶风暴Ⅱ：第二天国》 .txt`：既有原著 0 段；集合内部 3 段
- `江南作品合集/[05]其它短篇小说/《帝王》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[05]其它短篇小说/《猎犬狐》.txt`：既有原著 0 段；集合内部 2 段
- `江南作品合集/[06]散文随笔/《我想对少年们说的话》.txt`：既有原著 1 段；集合内部 0 段
- `江南作品合集/[06]散文随笔/《温故2009·最好的时候》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[06]散文随笔/《白马·勺园·凤凰台》.txt`：既有原著 1 段；集合内部 0 段
- `江南作品合集/[06]散文随笔/《过去的2008年总结》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[06]散文随笔/《龙与少年游》江南散文随笔精选.txt`：既有原著 0 段；集合内部 55 段
- `江南作品合集/[08]文论/《Who is Champollion》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[08]文论/《好吧，莫列狐老师……》.txt`：既有原著 37 段；集合内部 0 段
- `江南作品合集/[08]文论/《苏息的世界》.txt`：既有原著 147 段；集合内部 11 段
- `江南作品合集/[08]文论/《谁说奇幻已死？！》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[10]序跋/《〈上海堡垒〉——2016再版后记》.txt`：既有原著 0 段；集合内部 3 段
- `江南作品合集/[10]序跋/《〈上海堡垒〉后记》.txt`：既有原著 0 段；集合内部 15 段
- `江南作品合集/[11]刊首语/《九州幻想》06年7月刊首语【远游】.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[11]刊首语/《龙文·漫小说》Vol.08刊首语【那些年我们的小小朋党】.txt`：既有原著 1 段；集合内部 0 段
- `江南作品合集/[12]访谈录/《〈公主志〉的访谈稿》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[12]访谈录/《我的写作天赋并不比别人高——〈宁波晚报〉访谈》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[13]设定集/《〈九州缥缈录〉故事纲目》.txt`：既有原著 0 段；集合内部 10 段
- `江南作品合集/[13]设定集/《启示之卷》.txt`：既有原著 0 段；集合内部 10 段
- `江南作品合集/[13]设定集/《狮牙之卷》.txt`：既有原著 2 段；集合内部 0 段
- `江南作品合集/[13]设定集/《逆顺之轮·天驱之章》.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[13]设定集/《野尘军主要构成 & 乱世联盟成员简要资料》.txt`：既有原著 0 段；集合内部 10 段
- `江南作品合集/[14]其它/《中间人》（杂志版）.txt`：既有原著 0 段；集合内部 9 段
- `江南作品合集/[14]其它/《佛心红颜》（《茧》杂志版）.txt`：既有原著 0 段；集合内部 3 段
- `江南作品合集/[14]其它/《兄弟诀》（《何乃太多情》杂志版）.txt`：既有原著 0 段；集合内部 54 段
- `江南作品合集/[14]其它/《春风柳上原》（杂志版）.txt`：既有原著 0 段；集合内部 9 段
- `江南作品合集/[14]其它/《涿鹿》（第一人称版）.txt`：既有原著 0 段；集合内部 31 段
- `江南作品合集/[14]其它/《紫薇劫》（《紫薇·残红·风华》杂志版）.txt`：既有原著 0 段；集合内部 106 段
- `江南作品合集/[14]其它/《翰海龙吟》（《长沙绞风》杂志版）.txt`：既有原著 0 段；集合内部 1 段
- `江南作品合集/[14]其它/《荆棘王座》（旧版）.txt`：既有原著 0 段；集合内部 5 段
- `江南作品合集/[14]其它/《龙族Ⅰ：火之晨曦》（连载版）.txt`：既有原著 130 段；集合内部 0 段
- `江南作品合集/[14]其它/《龙族Ⅱ：悼亡者之瞳》（连载版）.txt`：既有原著 328 段；集合内部 0 段
- `江南作品合集/[14]其它/《龙族Ⅲ：黑月之潮》（连载版）.txt`：既有原著 10 段；集合内部 0 段
- `江南作品合集/[14]其它/《龙族Ⅳ：奥丁之渊》（连载版）.txt`：既有原著 1928 段；集合内部 0 段

## 疑似版本差异（保留）

- `上海堡垒.txt`：reference_before=0.0%，reference_after=0.0%，internal=53.4%；未达到整文件删除阈值
- `天之炽I：红龙的归来.txt`：reference_before=23.7%，reference_after=3.7%，internal=64.1%；未达到整文件删除阈值
- `江南作品合集/[02]九州短篇小说/《猎风》.txt`：reference_before=0.0%，reference_after=0.0%，internal=52.1%；未达到整文件删除阈值
- `江南作品合集/[06]散文随笔/《龙与少年游》江南散文随笔精选.txt`：reference_before=0.0%，reference_after=0.0%，internal=43.6%；未达到整文件删除阈值
- `江南作品合集/[10]序跋/《〈上海堡垒〉后记》.txt`：reference_before=0.0%，reference_after=0.0%，internal=43.1%；未达到整文件删除阈值
- `江南作品合集/[13]设定集/《野尘军主要构成 & 乱世联盟成员简要资料》.txt`：reference_before=0.0%，reference_after=0.0%，internal=64.5%；未达到整文件删除阈值
- `江南作品合集/[14]其它/《兄弟诀》（《何乃太多情》杂志版）.txt`：reference_before=0.0%，reference_after=0.0%，internal=42.6%；未达到整文件删除阈值
- `江南作品合集/[14]其它/《紫薇劫》（《紫薇·残红·风华》杂志版）.txt`：reference_before=0.0%，reference_after=0.0%，internal=33.9%；未达到整文件删除阈值
