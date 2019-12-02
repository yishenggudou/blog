Title: 基于java的异构结构迁移方案
Date: 2019-11-28 10:02
Category: java
Tags: java, hibernate
Summary: 基于java的异构结构迁移方案
Status: _published

# 背景

在公司占了个数据迁移的坑,调研了些结构迁移的事. 
大概理了个java版本的异构数据库结构转换思路,没时间细写,整体很粗糙.


# 思路


## 从数据库反射为java对象(提取)

https://github.com/hibernate/hibernate-tools/blob/master/ant/src/main/java/org/hibernate/tool/ant/HibernateToolTask.java

https://hibernate.org/tools/

https://www.javacodegeeks.com/2013/10/step-by-step-auto-code-generation-for-pojo-domain-java-classes-and-hbm-using-eclipse-hibernate-plugin.html

## 异构转换(转换)

由于hibernate本身模型是统一的,所以只需指定不同的放呀就行

## java再到DDL(生成)

http://fruzenshtein.com/hibernate-ddl-schema-generation/

https://geowarin.com/generate-ddl-with-hibernate/


https://github.com/geowarin/hibernate-examples/blob/master/generate-ddl-hibernate/src/main/java/com/geowarin/HibernateExporter.java

## 支持的方言

![](/docs/blog/static/15749338251165.jpg)


