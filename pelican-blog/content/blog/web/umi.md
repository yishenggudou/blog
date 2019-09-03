Title: umi
Date: 2019-09-03 23:02
Category: web
Tags: umi, web
Summary: umi usage

# 背景

# 用法

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
关于怎么生成动态路径带参数的路径？请看官方文档。
[umi文档](https://umijs.org/zh/guide/router.html#%E5%90%AF%E7%94%A8-hash-%E8%B7%AF%E7%94%B1)

## 数据交互

数据交互。没找到好的库。




