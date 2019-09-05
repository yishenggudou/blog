Title: npm usage
Date: 2019-09-03 17:33
Category: tool
Tags: npm, javascript
Summary: npm usage 
Status: published


# 背景

写web甚久,但是crud而已,没有特别的高层次产物和沉淀,
需要了解一个语言的生态得先从包管理工具入手.本着以后希望沉淀一个自己的组件包,告别copy and Modify 模式.
简单了解了下npm, 记录如下

# 发布

## 新增账号

如果已经有账号可以不需要

```bash
➜  schema-antd git:(master) ✗ npm adduser 
Username: yishenggudou
Password: 
Email: (this IS public) yishenggudou@gmail.com
Logged in as yishenggudou on https://registry.npmjs.org/.


   ╭────────────────────────────────────────────────────────────────╮
   │                                                                │
   │       New minor version of npm available! 6.7.0 → 6.11.3       │
   │   Changelog: https://github.com/npm/cli/releases/tag/v6.11.3   │
   │               Run npm install -g npm to update!                │
   │                                                                │
   ╰────────────────────────────────────────────────────────────────╯

➜  schema-antd git:(master) ✗ 

```

确认

```
➜  schema-antd git:(master) ✗ npm who am i
yishenggudou
➜  schema-antd git:(master) ✗ 
```

## 打包

```
npm pack
```

将会形成一个tar.gz的包, 可以被npm直接install 

## 确认package

![](/docs/blog/static/15676561408950.jpg)


## 发布

```
npm publish
```

执行日志如下

```
➜  schema-antd git:(master) ✗ npm publish
npm notice 
npm notice 📦  schema-antd@0.1.0
npm notice === Tarball Contents === 
npm notice 820B    package.json              
npm notice 2.1kB   README.md                 
npm notice 417.6kB schema-antd-0.1.0.tgz     
npm notice 491B    tsconfig.json             
npm notice 475.5kB yarn.lock                 
npm notice 3.9kB   public/favicon.ico        
npm notice 1.7kB   public/index.html         
npm notice 5.3kB   public/logo192.png        
npm notice 9.7kB   public/logo512.png        
npm notice 494B    public/manifest.json      
npm notice 57B     public/robots.txt         
npm notice 492B    src/App.css               
npm notice 248B    src/App.test.tsx          
npm notice 569B    src/App.tsx               
npm notice 0       src/command/BaseCommand.ts
npm notice 366B    src/index.css             
npm notice 452B    src/index.tsx             
npm notice 2.7kB   src/logo.svg              
npm notice 40B     src/react-app-env.d.ts    
npm notice 5.2kB   src/serviceWorker.ts      
npm notice === Tarball Details === 
npm notice name:          schema-antd                             
npm notice version:       0.1.0                                   
npm notice package size:  626.7 kB                                
npm notice unpacked size: 927.7 kB                                
npm notice shasum:        7ff15b367e419747206930a3b079153210b6cfe4
npm notice integrity:     sha512-gC6cIxgK0eKuS[...]He6J3bz1OEqmQ==
npm notice total files:   20                                      
npm notice 
+ schema-antd@0.1.0
➜  schema-antd git:(master) ✗ 
```

如果报错需要根据具体情况处理

最终可以在 [npm官网](https://www.npmjs.com/package/schema-antd) 上看到你的包, 包名需要替换为自己内容


# 总结

npm在易用性上做的非常不错,我们只需要几个命令就可以完成发布和创建,重点是每个命令的语义非常清晰,一下子就能理解看明白, 对比java的maven和 python的 pypi 实在好用太多
npm上包的数量这么多跟npm好用有离不开的关系

