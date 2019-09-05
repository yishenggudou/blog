Title: umi 用法
Date: 2019-09-03 23:02
Category: web
Tags: umi, web
Summary: umi usage
Status: published


# 背景

最近有需要写些前端业务,需要写一些前端.
看了最新的 angular 和 react 觉得 angular 全家桶虽然很成熟,但是在组件方面还是 react 更多.
angular 变化太大, 学了也没啥用, 主要国内感觉没场景, 已经被 react 带偏了.

调研了一些脚手架工具发现umi的设计思路跟我之前的想法很像, 

具体可以参见 [umijs](https://github.com/umijs/umi) 作者为支付宝人.

> js项目真的吸粉

#### 优点:


1. 以page为维度组织,每个page一个文件单元,隔离性非常好
2. 路由约定在路径命名方式中,不需要单独配置.以约定为主.
3. layout层独立出来,全局只有一个layout.单独配置
3. 脚手架快速生成工程.

以上点在我写项目写基本是按照这个约定来的,不过没有变成框架.

#### 不足

1. 状态管理还是缺乏, 后续我会写文章再说

# 用法

记录如下

## 初始化工程
```
npm install create-umi -g
cd appdir
create-umi
```

## 新增页面
```
umi generate page index
```

将会自动

## 路由编辑


### 确定路由方式

下面改了`history: 'hash'` 避免直接路由

```javascript
import {IConfig} from 'umi-types';

// ref: https://umijs.org/config/
const config: IConfig = {
  treeShaking: true,
  history: 'hash',
  plugins: [
    // ref: https://umijs.org/plugin/umi-plugin-react.html
    ['umi-plugin-react', {
      antd: true,
      dva: false,
      dynamicImport: false,
      title: 'webui',
      dll: false,

      routes: {
        exclude: [
          /components\//,
        ],
      },
    }],
  ],
};

export default config;

```

### 路由规则

关于怎么生成动态路径带参数的路径？请看官方文档。
[umi文档](https://umijs.org/zh/guide/router.html#%E5%90%AF%E7%94%A8-hash-%E8%B7%AF%E7%94%B1)

#### 基础路由

假设 pages 目录结构如下：

```
+ pages/
  + users/
    - index.js
    - list.js
  - index.js
```

那么，umi 会自动生成路由配置如下：

```js
[
  { path: '/', component: './pages/index.js' },
  { path: '/users/', component: './pages/users/index.js' },
  { path: '/users/list', component: './pages/users/list.js' },
]

```

#### 动态路由

page目录如下:

```
+ pages/
  + $post/
    - index.js
    - comments.js
  + users/
    $id.js
  - index.js
```

会生成路由配置如下：


```js
[
  { path: '/', component: './pages/index.js' },
  { path: '/users/:id', component: './pages/users/$id.js' },
  { path: '/:post/', component: './pages/$post/index.js' },
  { path: '/:post/comments', component: './pages/$post/comments.js' },
]
```

### 在组件中获取路由参数

因为路由会对到component里面的组件, 可以用一下方式获取

比如路径为

```js
  { path: '/:post/', component: './pages/$post/index.js' }
```

那么js代码为

```js
const post = this.props.match.params.post;
```

具体用法可以参见 [react-router](https://reacttraining.com/react-router/core/api/Route)

## 数据交互

数据交互。没找到好的库。




