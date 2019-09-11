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


# 举例

# 引用


1. [wikipedia.org/wiki/Make](https://zh.wikipedia.org/wiki/Make)


