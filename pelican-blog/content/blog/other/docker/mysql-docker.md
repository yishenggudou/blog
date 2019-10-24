Title: 基于官方镜像mysql开启binlog 杂记
Date: 2019-10-12 20:00
Category: other
Tags: mysql,docker
Summary: mysql 开启binlog
Status: published

# pull

```
docker pull mysql:5.7
docker run --name mysql5.7 -p3306:3306 -p33060:33060  -e MYSQL_ROOT_PASSWORD=A6A6A6 -d mysql:5.7
```

# 更新配置

```
docker exec mysql5.7 bash -c "echo 'log-bin=/var/lib/mysql/mysql-bin' >> /etc/mysql/mysql.conf.d/mysqld.cnf"
docker exec mysql5.7 bash -c "echo 'server-id=123454' >> /etc/mysql/mysql.conf.d/mysqld.cnf"
docker exec mysql5.7 bash -c "echo 'max_allowed_packet=5G' >> /etc/mysql/mysql.conf.d/mysqld.cnf"
```

# 重启

```
docker restart mysql5.7
```

# 访问

```
mysql -h127.0.0.1 -P3306 -uroot -pA6A6A6
```

# 修正时区

```sql
SELECT NOW()

SET GLOBAL time_zone = '+8:00';
```

# 修正其他

```sql
SET GLOBAL max_allowed_packet=1073741824;
SHOW VARIABLES LIKE 'max_allowed_packet';
```

```
SHOW SESSION VARIABLES LIKE '%timeout%';
SHOW SESSION VARIABLES LIKE 'wait_timeout';
SET session wait_timeout=60000;
set global wait_timeout=180000;
```


# binlog

```sql
show variables like 'log_%'; 
```

# 

