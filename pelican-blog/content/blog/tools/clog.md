Title: cloc静态代码分析
Date: 2019-10-29 17:00
Category: tool
Tags: cloc,tool, mac
Summary: cloc静态代码分析 
Status: published

# 简介

cloc counts blank lines, comment lines, and physical lines of source code in many programming languages.


# 使用


## 用法

`cloc .`

结果

```txt
    6913 text files.
    5746 unique files.                                          
    2035 files ignored.

github.com/AlDanial/cloc v 1.84  T=38.49 s (129.7 files/s, 43463.3 lines/s)
-----------------------------------------------------------------------------------
Language                         files          blank        comment           code
-----------------------------------------------------------------------------------
Python                            3196         179476         281964         708125
PO File                             48          33744          36546          96048
JavaScript                          97           9567           9113          73608
SVG                                 37              7            141          59117
Java                               556           8826          13558          41242
HTML                               242          22773            219          36291
XML                                345            621            205          15681
C/C++ Header                        26            941           1360           5943
CSS                                 46           1991            742           5660
SQL                                 12            435            513           4180
reStructuredText                    88           2339           1288           4118
Maven                               25            243            227           3297
JSON                                80              0              0           2191
TeX                                  8            112            659           1763
C                                    5            144            121           1322
Markdown                           100            791              0           1070
Bourne Shell                        33             97            112            689
Lua                                  3            280             75            683
YAML                                 8             59             74            498
make                                 4             67             17            287
DOS Batch                            2             42              3            254
Fortran 90                          15             69             35            252
Jupyter Notebook                     1              0            522            118
INI                                  5              6              0             54
Fish Shell                           1             16             13             47
Dockerfile                           2              2              0             29
RAML                                 2              2              0             28
C Shell                              1             12              7             17
Fortran 77                           2              1              1             14
Bourne Again Shell                   1              0              0              6
Mustache                             1              0              0              3
Windows Resource File                1              1              0              2
-----------------------------------------------------------------------------------
SUM:                              4993         262664         347515        1062637
-----------------------------------------------------------------------------------
```

# 引用

1. [cloc](https://github.com/AlDanial/cloc)


