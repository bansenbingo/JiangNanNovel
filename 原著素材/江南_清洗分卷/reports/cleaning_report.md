# 江南语料清洗报告

- 工具版本：1.0.0
- 输入 TXT：493
- 保留文件：447
- 原始字节：48,163,998
- 解码字符：23,124,831
- 清洗后非空白字符：21,565,368
- 去重后非空白字符：7,044,907
- 输出分卷：702

## 编码分布

- `gb18030`：478
- `utf-8`：8
- `utf-8-sig`：4
- `utf-16`：2
- `gb18030-replace`：1

## 删除规则命中

- `social_promo`：453 行
- `separator_or_noncontent`：341 行
- `url`：55 行
- `consecutive_duplicate_line`：20 行
- `download_ad`：10 行
- `web_ui`：6 行

## 文件状态

- `included`：447
- `excluded_reference_duplicate`：25
- `excluded_internal_duplicate`：11
- `excluded_metadata`：4
- `excluded_after_block_dedup`：3
- `excluded_reference_variant`：3

## 分卷范围

- 最小：5,363
- 中位数：10,044
- 最大：11,564

小于目标下限的卷通常来自整个分类不足一万字，或为了不跨分类混合而保留。
