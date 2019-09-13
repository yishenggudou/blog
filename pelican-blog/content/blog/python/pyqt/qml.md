Title: qml
Date: 2019-09-13 17:33
Category: qt
Tags: python, pyqt, qml
Summary: qml 简介
Status: published

# 简介

QML是一种描述性的脚本语言，文件格式以.qml结尾。语法格式非常像CSS（参考后文具体例子），但又支持javascript形式的编程控制。QtDesigner可以设计出·ui界面文件，但是不支持和Qt原生C++代码的交互。QtScript可以和Qt原生代码进行交互，但是有一个缺点，如果要在脚本中创建一个继承于QObject的图形对象非常不方便，只能在Qt代码中创建图形对象，然后从QtScript中进行访问。而QML可以在脚本里创建图形对象，并且支持各种图形特效，以及状态机等，同时又能跟Qt写的C++代码进行方便的交互，使用起来非常方便。

# 核心概念

qml简单说就是一种UI描述DSL,常见UI类DSL其实是 XML居多, 但是UI描述只能描述静态的UI,我们需要的UI,一般还需要数据,事件, 所以除了QML,还需 model和script,Delegate

![](/docs/blog/static/15683709235573.jpg)


## model

qml大致上还是遵循`MVC`设计的.

![](/docs/blog/static/15683005401746.jpg)

modal等价于数据源, 可以被view组件使用,也可以适配后端

但是数据源有很多种:

1. database
2. object
3. http file
4. json file

1. [qtqml-models](https://doc.qt.io/qt-5/qtqml-models-qmlmodule.html)
2. [wishlist](https://github.com/LupusAnay/wishlist)
3. [qt-io](https://doc.qt.io/qt-5/io.html)
4. [localstorage](https://doc.qt.io/qt-5/qtquick-localstorage-qmlmodule.html)
5. [sqlalchemy-example](https://github.com/LupusAnay/wishlist)

## ui组件

### 分类

qml组件文档如下[qmlmodule](https://doc.qt.io/qt-5/qtquick-controls2-qmlmodule.html)

![](/docs/blog/static/15683662851598.jpg)

#### 布局

[qtquicklayouts](https://doc.qt.io/qt-5/qtquicklayouts-index.html)


#### 工具栏

工具栏是`MenuBar`, 工具栏一般在`ApplicationWindow` 下级, 为全局菜单.

MenuBar 在不同的地方可能表现行为不一样

https://doc.qt.io/qt-5/qml-qtquick-controls2-menubar.html

https://doc.qt.io/qt-5/qml-qtquick-controls2-menu.html

```
ApplicationWindow {
    id: window
    width: 320
    height: 260
    visible: true

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            Action { text: qsTr("&New...") }
            Action { text: qsTr("&Open...") }
            Action { text: qsTr("&Save") }
            Action { text: qsTr("Save &As...") }
            MenuSeparator { }
            Action { text: qsTr("&Quit") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("&About") }
        }
    }
}
```


#### window

window简单说 应该是一个窗口, 属于比较重的一个对象. 一般一个APP至少一个window

[applicationwindow](https://doc.qt.io/qt-5/qml-qtquick-controls2-applicationwindow.html)

![](/docs/blog/static/15683682461827.jpg)


#### view




### 嵌套(组件化)

或者叫组件化,我们需要把一些细节内容,变成组件,或者说需要复用和单元化, 这个就需要组件化

#### 示例

目录结构

```
projectdir/
  qml/
    projectname/
      main.qml
      components/component_example.qml
```

in `mycomponent.qml`

```
MyCustomText {
  text:"Hello, Scooby Doo!";
}
```

in `main.qml`

使用`Loader`

```
Rectangle {

  Loader {
    source:"components/component_example.qml";
  }

}
```

或者 `import` :

```

import "components"

Rectangle {
  id: root
  MyCustomText {
    text: "This is my custom text element"
  }
}
```

[include-another-qml-file-from-a-qml-file](https://stackoverflow.com/questions/22168457/include-another-qml-file-from-a-qml-file)




## 事件

### ui事件

### 数据事件

## script





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

## cheat sheet

![](/docs/blog/static/15683688660378.jpg)


# 参考

1. [qmlbook-in-chinese](https://cwc1987.gitbooks.io/qmlbook-in-chinese/content/)
2. [PyQt](https://github.com/PyQt5/PyQt/tree/master/QPushButton)
3. [QML-Example](https://github.com/cfsghost/QML-Example)
4. [clean-editor](https://github.com/Fagrell/clean-editor)
5. [awesome-qt-qml](https://github.com/mikalv/awesome-qt-qml)
6. [awesome-python-qt](https://github.com/JulienGrv/awesome-python-qt)
7. [awesome-qt](https://github.com/skhaz/awesome-qt)

