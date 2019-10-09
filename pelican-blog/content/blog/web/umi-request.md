Title: umi-request用法
Date: 2019-10.09 20:00
Category: web
Tags: umi, web
Summary: umi-request用法
Status: published

# 简介

# 用法

## 全局封装

```
import { extend } from 'umi-request';

const request = extend({
  timeout: 1000,
  mode: 'no-cors',
  requestType: 'json',
  parseResponse: true,
  responseType: 'json',
  charset: 'utf8',
  getResponse: true,
  credentials: 'include',
  throwErrIfParseFail: true,
  errorHandler: function(error) {
    console.log(error, arguments);
  },
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});
export { request };
```


## 自定义中间层

```
request.use(async (ctx, next) => {
  console.log(ctx, next);
  await next();
}, { global: true });
```

## 业务使用

```
request.get
request.post
```

# 参考

1. [umi-request](https://github.com/umijs/umi-request)

