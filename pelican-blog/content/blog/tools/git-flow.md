Title: gitflow
Date: 2019-09-13 19:00
Category: tool
Tags: git,gitflow
Summary: gitflow 简介
Status: published

# 简介

git flow 核心点是解决一个开发共识问题, 赋予特定分支特定意义,来约定大家的认知.我觉得对于我来说核心还是不用乱开分支.按照约束就行了.多人协作能更加清晰,或者多版本产出也更加清晰.

核心解决还是 多版本管理和多人协作.


Git Flow常用的分支

#### Production 分支

也就是我们经常使用的Master分支，这个分支最近发布到生产环境的代码，最近发布的Release， 这个分支只能从其他分支合并，不能在这个分支直接修改

#### Develop 分支

这个分支是我们是我们的主开发分支，包含所有要发布到下一个Release的代码，这个主要合并与其他分支，比如Feature分支

#### Feature 分支

这个分支主要是用来开发一个新的功能，一旦开发完成，我们合并回Develop分支进入下一个Release,

#### Release分支

当你需要一个发布一个新Release的时候，我们基于Develop分支创建一个Release分支，完成Release后，我们合并到Master和Develop分支

#### Hotfix分支

当我们在Production发现新的Bug时候，我们需要创建一个Hotfix, 完成Hotfix后，我们合并回Master和Develop分支，所以Hotfix的改动会进入下一个Release

![](/docs/blog/static/15683780538729.jpg)


# 方案对比

## 命令行

1. [gitflow](https://github.com/nvie/gitflow)

## 界面

1. [www.sourcetreeapp.com](https://www.sourcetreeapp.com/)


# 用法

## 安装

![](/docs/blog/static/15683766773493.jpg)

sourcetree 会需要账号注册

![](/docs/blog/static/15683774467821.jpg)

授权


## 初始化

```
git flow init -d
```

或者sourcetree
![](/docs/blog/static/15683776771017.jpg)

初始化

![](/docs/blog/static/15683776955347.jpg)


## 开始feature

```
git flow feature start python3-support
```

或者sourcetree界面

![](/docs/blog/static/15683777451094.jpg)

## 发布

```
git flow feature publish python3-support
```



# 引用

1. [gitflow](https://github.com/nvie/gitflow)
2. [www.sourcetreeapp.com](https://www.sourcetreeapp.com/)
3. [a-successful-git-branching-model](https://nvie.com/posts/a-successful-git-branching-model/)

