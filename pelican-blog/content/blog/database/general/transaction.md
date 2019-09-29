Title: 事务
Date: 2019-09-28 20:00
Category: database
Tags: database,transaction
Summary: makefile写法研究
Status: _published

# 背景

事务（Transaction），一般是指要做的或所做的事情。在计算机术语中是指访问并可能更新数据库中各种数据项的一个程序执行单元(unit)。事务通常由高级数据库操纵语言或编程语言（如SQL，C++或Java）书写的用户程序的执行所引起，并用形如begin transaction和end transaction语句（或函数调用）来界定。事务由事务开始(begin transaction)和事务结束(end transaction)之间执行的全体操作组成。

在数据库中事务一般为

```
BEGIN TRANSACTION
sql1..
sql2..
COMMIT
```

![](/docs/blog/static/15696851336245.jpg)


## 事务执行逻辑



# 知识点

## 隔离性

### 串行化(Serializable，SQLite默认模式

最高级别的隔离。两个同时发生的事务100%隔离，每个事务有自己的"世界", 串行执行。

串行牺牲了并发能力,对于一个数据库一次只能执行一个事物.其他所有事物需要等待.

### 可重复读（Repeatable read，MySQL默认模式

重复读，就是在开始读取数据（事务开启）时，不再允许修改操作


如果一个事务成功执行并且添加了新数据(事务提交)，这些数据对其他正在执行的事务是可见的。但是如果事务成功修改了一条数据，修改结果对正在运行的事务不可见。所以，事务之间只是在新数据方面突破了隔离，对已存在的数据仍旧隔离。


### 读取已提交（Read committed，Oracle、PostgreSQL、SQL Server默认模式

读提交，顾名思义，就是一个事务要等另一个事务提交后才能读取数据。


可重复读+新的隔离突破。如果事务A读取了数据D，然后数据D被事务B修改（或删除）并提交，事务A再次读取数据D时数据的变化（或删除）是可见的。这叫不可重复读（non-repeatable read）。

### 读取未提交（Read uncommitted

读未提交，顾名思义，就是一个事务可以读取另一个未提交事务的数据。



最低级别的隔离，是读取已提交+新的隔离突破。如果事务A读取了数据D，然后数据D被事务B修改（但并未提交，事务B仍在运行中），事务A再次读取数据D时，数据修改是可见的。如果事务B回滚，那么事务A第二次读取的数据D是无意义的，因为那是事务B所做的从未发生的修改（已经回滚了嘛）。这叫脏读（dirty read）。


### 举例

小明家室做快递的,

### spring中的事物隔离

# 现实中的问题

## 嵌套事务



# 引用 

1. [数据库中事务隔离级别以及其实现简述](https://zhuanlan.zhihu.com/p/81046323)
2. [深入理解数据库事务](https://zhuanlan.zhihu.com/p/43493165)
3. [事务](https://baike.baidu.com/item/%E4%BA%8B%E5%8A%A1/5945882?fr=aladdin)
4. [数据库事务](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BA%8B%E5%8A%A1/9744607)
5. [SQL92](https://baike.baidu.com/item/SQL92/6333507?fr=aladdin)


