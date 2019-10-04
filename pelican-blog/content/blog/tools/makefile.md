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

Makefile的规则如下：
```
target ... : prerequisites ...
        command
        ...
        ...
```

target也就是一个目标文件，可以是Object 文件，也可以是执行文件。还可以是一个标签(Label)，对于标签这种特性，将在后面叙述。

prerequisites就是，要生成那个target所需要的文件或是目标。

command也就是make需要执行的命令。(任意的Shell命令)

这个规则可以这么看，目标文件target的生成需要依赖prerequisites中的一些文件，而target文件的生成规则是在command中定义的。

整体上就是描述按需依赖

### 目标

target也就是一个目标文件，可以是Object 文件，也可以是执行文件。还可以是一个标签(Label)，对于标签这种特性，将在后面叙述。

标签名就类似于任务名

目标单独存在时候类似于任务，　被依赖时候就可以明确说生成目标，command部分,应该是描述生成目标的定义. 目标可以被其他任务或者文件依赖,

所以很多个目标,组合依赖, 就可以完成很复杂的事情.

`.PHONY:` 表示一个虚目标

PHONY 目标并非实际的文件名：只是在显式请求时执行命令的名字。有两种理由需要使用PHONY 目标：避免和同名文件冲突，改善性能。

如果编写一个规则，并不产生目标文件，则其命令在每次make 该目标时都执行。例如：
　　clean:
　　rm *.o temp
因为"rm"命令并不产生"clean"文件，则每次执行"make clean"的时候，该命令都会执行。如果目录中出现了"clean"文件，则规则失效了：没有依赖文件，文件"clean"始终是最新的，命令永远不会 执行；为避免这个问题，可使用".PHONY"指明该目标。如：
　　.PHONY : clean
　　这样执行"make clean"会无视"clean"文件存在与否。

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

果依赖因, 因本身又是果, 如此递归下去.

### 注释

```
clean-test: ## remove test and coverage artifacts
    do some
```

将会在 `make` 时候显示

```
clean-test           remove test and coverage artifacts

```



## 技巧

### 自动生产帮助文档


```
help:
	@python -c "import re;help='\n'.join([line.replace('##','\n\t') for line in open('Makefile').readlines() if re.search('^[a-zA-Z0-9\-\_]*?\:[\s\S]*?$$',line,flags=re.I)]);print help"

.DEFAULT_GOAL := help
```

当然也可以手写
```
help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '   
```

### 使用上下文

```
make-doc: ##build doc
	. ${V_PYTHON}; cd docs; make html
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
2. [automake](https://www.gnu.org/software/automake/manual/automake.html)
3. [auto-documented-makefile](https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html)
4. [makefile-help](https://github.com/ianstormtaylor/makefile-help)
5. [makefile里PHONY的相关介绍](https://www.cnblogs.com/hnrainll/archive/2011/04/12/2013377.html)


