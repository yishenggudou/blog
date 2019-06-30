# python 环境相关 

## 国内环境

国内常见安装官方的 pypi 会被强,建议修改全局设置

修改文件`~/.pip/pip.conf`

```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

## 发布包到官方仓库



