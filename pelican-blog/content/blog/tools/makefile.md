Title: makefile
Date: 2019-09-11 17:00
Category: tool
Tags: makefile
Summary: makefile写法研究
Status: published

# 简介

make是一个工具程序（Utility software），经由读取叫做“makefile”的文件，自动化建构软件。它是一种转化文件形式的工具，转换的目标称为“target”；与此同时，它也检查文件的依赖关系，如果需要的话，它会调用一些外部软件来完成任务。它的依赖关系检查系统非常简单，主要根据依赖文件的修改时间进行判断。大多数情况下，它被用来编译源代码，生成结果代码，然后把结果代码连接起来生成可执行文件或者库文件。它使用叫做“makefile”的文件来确定一个target文件的依赖关系，然后把生成这个target的相关命令传给shell去执行。

许多现代软件的开发中（如Microsoft Visual Studio），集成开发环境已经取代make，但是在Unix环境中，仍然有许多任务程师采用make来协助软件开发。


# 概念

简单理解是makefile 是一组特定的DSL,方便快速完成各种基于文件和环境变化的任务定义和构建.

### 目标

目标就是一个任务

### 依赖

一定是一个依赖规则.或者文件.或者宏

```
OBJECTS = main.o text.o
INSTALL_PATH = /usr/local
editor: $(OBJECTS)
	gcc -o editor $(OBJECTS)
main.o: main.c
	gcc -c main.c
text.o: text.c
	gcc -c text.c
install:editor
	mv editor $(INSTALL_PATH)
```

### 注释

```
clean-test: ## remove test and coverage artifacts
    do some
```

将会在 `make` 时候显示

```
clean-test           remove test and coverage artifacts

```

## 场景

### 整合各种零散脚本

比如:

```
build_pri.sh
build_product.sh
build_test.sh
build_docker.sh
```

### 串联各种步骤

```python
def do_one():
    pass
    
def do_two():
    pass
    
def main():
    do_one()
    do_two()

```


# 常见问题

### 设置环境变量



# 引用


1. [wikipedia.org/wiki/Make](https://zh.wikipedia.org/wiki/Make)


