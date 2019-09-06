Title: 状态管理杂谈
Date: 2019-09-05 23:02
Category: web
Tags: state, web, javascript
Summary: 状态管理历史杂谈
Status: published


# 背景 

写前端的很多工作其实本质是处理各种事件状态和数据状态.尤其在 react组件方式出来之后

 $组件=状态+UI逻辑$

# 历史

## jquery时代

jquery 时代的状态就是 dom 的状态, 很多时候记录在 dom 的属性上, 或者 dom 节点上

通常是这样

```html
<div data="x"/>
```

用法上很多时候是

```js
$('#x').attr('data')
```

## backbone时代

[backbone](https://backbonejs.org) 时代的状态在 js 里面, 有模型定义,然后很简单的接口监听模型属性的变化

![](/docs/blog/static/15676953790976.jpg)


到现在为止,我还是觉得 backbone 的方式是比较清晰理解的.因为他有清晰的模型定义,这个是一切的前提
而且这个 model 和 http 接口结合的很好, 

```
var book = new Backbone.Model({
  title: "The Rough Riders",
  author: "Theodore Roosevelt"
});
```

然后`book.on(event)`来监听数据的变化, `book.fetch()` 来处理同server 端的数据同步

每个模型定义能够清晰的对应到 http 到操作,也可以很方便的扩展 http 的操作.


## angular 时代

angular早期的特点就是[MVVM](https://baike.baidu.com/item/MVVM/96310) 模板中的变量就是 model

angular model的特点是贴近 view 层,但是和后端接口层不是太清晰,充斥着大量的 js 对象完全不可清晰查看数据的变更. 其实本质是 viewmodel 在解决 viewmodel 部分比较清晰, 但是在解决后端资源时候不清晰. 

## react 时代

react本质是一个组件,我理解标准的 react 组件应该是纯函数的,无副作用的

1. state 应该是局部变量,控制自包含 ui 部分的一些变量, 
2. props 应该是外部数据,上游数据以及其他数据源, 比如 http 接口

但是我们的使用的过程一般混用没有很清晰的边界,其实主要还是跟. react概念有关,因为state 的定义不清晰.

#### redux
 
没了解不评论,看[文档](https://redux.js.org/introduction/getting-started) 关注点在UI事件部分, 使用成本很高,所以一直没有流行起来

#### mobx

[mobx](https://mobx.js.org/)算是react里面比较成熟的,也算比较好用, 接近viewmodel的能力,能很好的把数据变化相应到组件上, 但是对与比如和 http 对接其实还是不太清晰,主要得问他在于是 mobx 还是围绕的是数据变化,而不是数据模型,且 mobx 需要对组件注解,对组件的侵入性很高.

![](/docs/blog/static/15677471434314.jpg)

mobx的抽象是以action为组织的, 需要各种注解, 整个侵入性比较高.

# 个人的想法

综合之前的理解, 我个人理解最好的,模式应该是这样

![](/docs/blog/static/15676993400630.jpg)

从数据状态分类角度,大概的分类如下

![](/docs/blog/static/15676997061508.jpg)


细节描述待续.. 


