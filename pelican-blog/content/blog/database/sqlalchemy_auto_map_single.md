Title: sqlalchemy automap 和 reflect
Date: 2019-10-31 10:00
Category: database
Tags: database, sqlalchemy
Summary:  sqlalchemy automap 和 reflect
Status: published


# 用法

## 指定表查询

反射部分表

```python
test1_engine = create_engine(test1_db_uri, echo=True)
test2_engine = create_engine(test2_dburi, echo=True)
test1_metadata = MetaData()
test2_metadata = MetaData()
test1_metadata(bind=test1, only=['table1', 'table2'])
test2_metadata(bind=oms_metadata, only=['table1', 'table2', 'table3'])
test1_session = Session(test1_engine)
test2_session = Session(test2_engine)
```

## 查询

```python
session = Session(test1_engine)
Table1 = odc_metadata.tables.get("table1")
test1_session(Table1).filter(id=id).first()

```

