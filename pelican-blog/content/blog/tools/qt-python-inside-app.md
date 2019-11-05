Title: 通用python的打包方案
Date: 2019-11-05 12:00
Category: tool
Tags: qt,tool, pyqt
Summary: 通用python的打包方案
Status: published

# 简介

其实这篇是[qtcontainer](https://github.com/yishenggudou/qtcontainer)的一个起因

我最近想打包一个app,出来销售,或者自动化.做过一些调研
比如 https://github.com/mherrmann/fbs 以及 https://github.com/electron
但是个人原因对python熟悉的多一些,所以还是多看了一眼fbs

综合采坑下来,fbs有很多问题
1. 支持不好
2. pythoninstaller打包其实很多包大不进去,也可能是我的水平问题,至少django我觉得不行
3. 多进程管理不方便
最终我觉得采用类似安装器的逻辑

# 思路

## 定义APP

基于pyside2和pythoninstaller

## 安装virtualenv

## 安装软件

## 装配主程序


# 引用

1. [qtcontainer](https://github.com/yishenggudou/qtcontainer)

