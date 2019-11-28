Title: 国内环境sbt使用方案
Date: 2019-11-25 12:00
Category: tool
Tags: sbt,tool
Summary: 国内环境sbt使用方案
Status: published

编辑 `vim ~/.sbt/repositories`

```
[repositories]
#本地源
local
#国内源，osChina
osc: http://maven.oschina.net/content/groups/public/
#兼容 Ivy 路径布局
oschina-ivy:http://maven.oschina.net/content/groups/public/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext]
#添加国外源备用
typesafe: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext], bootOnly
sonatype-oss-releases
maven-central
sonatype-oss-snapshots
```

# 参考

1. [SBT无痛入门指南](https://cloud.tencent.com/developer/article/1506710)


