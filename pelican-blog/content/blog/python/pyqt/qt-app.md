Title: qt wrapper the webapp and build a single app
Date: 2019-09-04 19:36
Category: qt
Tags: python, pyqt
Summary: 使用qt构建轻量级的mac app 和 window app
Status: published

# 背景

# 方案

## 方案1 基于 fbs

1. [fbs-tutorial](https://github.com/mherrmann/fbs-tutorial)
2. [fbs](https://github.com/mherrmann/fbs/)

fbs is the fastest way to create a Python GUI. It solves common pain points such as packaging and deployment. Based on Python and Qt, fbs is a lightweight alternative to Electron.

![](/docs/blog/static/15680020667660.jpg)


fbs的说法是Electron的替代品,Electron没深入了解过, 从教程看如果都用python3+pyqt确实很简单

#### 问题

1. 版权GPL协议 不能直接商用
2. 需要开源
3. 不支持python2.x, 恰好我的一个项目是依赖python2

## 方案2 pyinstaller

[pyinstaller](http://www.pyinstaller.org/)

pyinstaller 最早的开发 我貌似还在maillist里面看到宣传邮件
官方的介绍如下:

PyInstaller freezes (packages) Python applications into stand-alone executables, under Windows, GNU/Linux, Mac OS X, FreeBSD, Solaris and AIX.

![](/docs/blog/static/15680020398783.jpg)


pyinstaller实际上简单的代码是ok,如果复杂的工程,难点在于依赖, 比如django, 我就怎么也没搞定过.

#### 问题

1. 需要定制的东西很多
2. python依赖问题不好弄,切各个平台打包细节复杂


# 我的观点

我个人觉得virtualenv的适应性貌似更好,我觉得生命力最强的模式是

## 纯python3的想

直接使用PyQt和FBS,不做其他处理

## 集成python2.x或者其他组件,以及django+webui类产品

1. 制造一个qt的安装器(初始化器)
2. 第一次进入app的时候,下载最新virtual的包(或者自带virtual文件)
3. 升级时候下载对应的virtual包
4. 拿到包之后修正文件路径, 
5. 使用supervisor 封装服务,拉起其他服务进程.

> 其实我也思考过不用django直接js算了,不过鉴于对js的了解说不定js的坑更多,由于多年的python圈子,我还是对python放心点. flask也不错,但是写crud还是没有django全套快.

针对上面的想法 我起了一个工程[qtcontainer](https://github.com/yishenggudou/qtcontainer) 专门做一个壳子
匹配到我的三个千万方向的其中之一.


