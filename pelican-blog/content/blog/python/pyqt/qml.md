Title: qml
Date: 2019-09-03 17:33
Category: qt
Tags: python, pyqt, qml
Summary: qml 简介
Status: _published

# 简介

QML是一种描述性的脚本语言，文件格式以.qml结尾。语法格式非常像CSS（参考后文具体例子），但又支持javascript形式的编程控制。QtDesigner可以设计出·ui界面文件，但是不支持和Qt原生C++代码的交互。QtScript可以和Qt原生代码进行交互，但是有一个缺点，如果要在脚本中创建一个继承于QObject的图形对象非常不方便，只能在Qt代码中创建图形对象，然后从QtScript中进行访问。而QML可以在脚本里创建图形对象，并且支持各种图形特效，以及状态机等，同时又能跟Qt写的C++代码进行方便的交互，使用起来非常方便。

# 核心概念

## model

qml大致上还是遵循`MVC`设计的.

![](/docs/blog/static/15683005401746.jpg)


## ui组件

### 分类

#### 工具栏

#### window

#### view


### 嵌套



### 工具栏

### window系列



## 事件

### ui事件

### 数据事件


# 调试工具

## qmlscene

```
brew install qt5
```

然后

```
brew linkapps qt5
brew link --force qt5
```

或者

```
➜  ~ ls -alh /usr/local/Cellar/qt/5.13.1/bin
total 45344
drwxr-xr-x  45 timger  staff   1.4K  9  3 20:32 .
drwxr-xr-x  16 timger  staff   512B  9 12 09:34 ..
-r-xr-xr-x   1 timger  staff    51K  9 12 09:34 canbusutil
-r-xr-xr-x   1 timger  staff   6.2K  9  3 20:32 fixqt4headers.pl
-r-xr-xr-x   1 timger  staff   251K  9 12 09:34 lconvert
-r-xr-xr-x   1 timger  staff   311K  9 12 09:34 lprodump
-r-xr-xr-x   1 timger  staff   276K  9 12 09:34 lrelease
-r-xr-xr-x   1 timger  staff    30K  9 12 09:34 lrelease-pro
-r-xr-xr-x   1 timger  staff   667K  9 12 09:34 lupdate
-r-xr-xr-x   1 timger  staff    30K  9 12 09:34 lupdate-pro
-r-xr-xr-x   1 timger  staff   179K  9 12 09:34 macchangeqt
-r-xr-xr-x   1 timger  staff   200K  9 12 09:34 macdeployqt
-r-xr-xr-x   1 timger  staff   847K  9  3 20:32 moc
-r-xr-xr-x   1 timger  staff    13K  9  3 20:32 qcollectiongenerator
-r-xr-xr-x   1 timger  staff    66K  9 12 09:34 qdbus
-r-xr-xr-x   1 timger  staff   249K  9 12 09:34 qdbuscpp2xml
-r-xr-xr-x   1 timger  staff    72K  9 12 09:34 qdbusxml2cpp
-r-xr-xr-x   1 timger  staff   134K  9 12 09:34 qdistancefieldgenerator
-r-xr-xr-x   1 timger  staff   6.7M  9 12 09:34 qgltf
-r-xr-xr-x   1 timger  staff   154K  9 12 09:34 qhelpgenerator
-r-xr-xr-x   1 timger  staff   115K  9 12 09:34 qlalr
-r-xr-xr-x   1 timger  staff   5.9M  9  3 20:32 qmake
-r-xr-xr-x   1 timger  staff   728K  9 12 09:34 qmlcachegen
-r-xr-xr-x   1 timger  staff   102K  9 12 09:34 qmleasing
-r-xr-xr-x   1 timger  staff   291K  9 12 09:34 qmlimportscanner
-r-xr-xr-x   1 timger  staff   238K  9 12 09:34 qmllint
-r-xr-xr-x   1 timger  staff   121K  9 12 09:34 qmlmin
-r-xr-xr-x   1 timger  staff   146K  9 12 09:34 qmlplugindump
-r-xr-xr-x   1 timger  staff    98K  9 12 09:34 qmlpreview
-r-xr-xr-x   1 timger  staff   179K  9 12 09:34 qmlprofiler
-r-xr-xr-x   1 timger  staff    66K  9 12 09:34 qmlscene
-r-xr-xr-x   1 timger  staff    24K  9 12 09:34 qmltestrunner
-r-xr-xr-x   1 timger  staff   330K  9 12 09:34 qscxmlc
-r-xr-xr-x   1 timger  staff    68K  9 12 09:34 qtattributionsscanner
-r-xr-xr-x   1 timger  staff    74K  9 12 09:34 qtdiag
-r-xr-xr-x   1 timger  staff    38K  9 12 09:34 qtpaths
-r-xr-xr-x   1 timger  staff    32K  9 12 09:34 qtplugininfo
-r-xr-xr-x   1 timger  staff    38K  9 12 09:34 qvkgen
-r-xr-xr-x   1 timger  staff   1.7M  9 12 09:34 qwebengine_convert_dict
-r-xr-xr-x   1 timger  staff   761K  9  3 20:32 rcc
-r-xr-xr-x   1 timger  staff   437K  9 12 09:34 repc
-r-xr-xr-x   1 timger  staff    47K  9  3 20:32 syncqt.pl
-r-xr-xr-x   1 timger  staff   445K  9 12 09:34 uic
-r-xr-xr-x   1 timger  staff    73K  9 12 09:34 xmlpatterns
-r-xr-xr-x   1 timger  staff    19K  9 12 09:34 xmlpatternsvalidator 
```
或者加入上面路径到PATH

```
export PATH=$PATH:/usr/local/Cellar/qt/5.13.1/bin/
```

然后
```
which qmake
which qmlscene
```

查看是否生效
    
## OwaViewer

[OwaViewer](https://github.com/HanGee/OwaViewer)


# 参考

1. [qmlbook-in-chinese](https://cwc1987.gitbooks.io/qmlbook-in-chinese/content/)
2. [PyQt](https://github.com/PyQt5/PyQt/tree/master/QPushButton)
3. [QML-Example](https://github.com/cfsghost/QML-Example)
4. [clean-editor](https://github.com/Fagrell/clean-editor)
5. [awesome-qt-qml](https://github.com/mikalv/awesome-qt-qml)
6. [awesome-python-qt](https://github.com/JulienGrv/awesome-python-qt)
7. [awesome-qt](https://github.com/skhaz/awesome-qt)

