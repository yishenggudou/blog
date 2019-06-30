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

## py 工程

常见我们要新建一个 py 工程建议使用 https://github.com/audreyr/cookiecutter

可以参见 标签为 [python](https://github.com/audreyr/cookiecutter#python) 部分的模板

### 安装cookiecutter

```
pip install -U cookiecutter
```

### 生成模板

```
➜  x-schema-migration git:(master) ✗ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
You've downloaded /Users/timger/.cookiecutters/cookiecutter-pypackage before. Is it okay to delete and re-download it? [yes]: yes
full_name [Audrey Roy Greenfeld]: yishenggudou
email [audreyr@example.com]: yishenggudou@gmail.com
github_username [audreyr]: yishenggudou
project_name [Python Boilerplate]: Easy useful schema migration tool
project_slug [easy_useful_schema_migration_tool]: xschema       
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: 
pypi_username [yishenggudou]: 
version [0.1.0]: 
use_pytest [n]: y
use_pypi_deployment_with_travis [y]: 
add_pyup_badge [n]: y
Select command_line_interface:
1 - Click
2 - No command-line interface
Choose from 1, 2 [1]: 2
create_author_file [y]: 
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 6

```

将会看到生成的文件

```
➜  x-schema-migration git:(master) ✗ ls
venv    xschema
```

## 发布包到官方仓库



