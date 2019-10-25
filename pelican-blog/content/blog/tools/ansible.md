Title:ansible使用记要
Date: 2019-10-24 17:00
Category: tool
Tags: ansible,shell,linux
Summary: ansible使用记要
Status: published

# 背景

最近做db相关的工作,需要构造各种数据源,由于需要在不确定的机器上伪造各种不确定的数据库版本,这个时候我想到了ansible

# 介绍

官方的介绍可以参见:

<iframe allowtransparency="true" title="Wistia video player" allowFullscreen frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" src="https://fast.wistia.net/embed/iframe/qrqfj371b6" width="400" height="225"></iframe>

核心概念图可以参考:

![](/docs/blog/static/15719200978290.jpg)


```
ansible -h
Usage: ansible <host-pattern> [options]

Define and run a single task 'playbook' against a set of hosts
```

先指定 匹配 host 然后再执行操作.

我觉得整个ansible有点像模式匹配,先匹配,再推演.

## 核心概念

## 

# 用法

## 安装

```
pip install -U ansible==2.8.6
```


## 生成项目

这里推荐[ansible-generator](https://pypi.org/project/ansible-generator/)来生成项目,经过测试,这里生成的是满足官方最佳实践的.

```
pip install -U ansible-generator
```

官方的样板工程可以参见 [ansible/ansible-examples](https://github.com/ansible/ansible-examples)

### 生成工程

```
ansible-generate -p testcluster
```
### 生成角色

生成角色需要指定项目名

```
ansible-generate -r pg -p testcluster
```


## 常见用法

### 使用task

task为单个任务,定义方式

```
```

执行方式

```
```

### 使用playbook

定义playbook

```

```

使用playbook

```
ansible all -i vyos.example.net, -c network_cli -u my_vyos_user -k -m vyos_facts -e ansible_network_os=vyos
```

> `-e` 为指定变量值

### 远程命令

```
ansible test -a 'df -h' -i hosts -u admin --extra-vars "ansible_ssh_pass=admin"
```




### 在参数中覆盖变量

```
 --extra-vars "ansible_ssh_user=admin ansible_ssh_pass=admin"
```

### 切换到root

```yaml
-   name: Install antman
    shell: |
        cd /tmp/
    become: true
    become_user: root
```

命令行

```
--extra-vars='ansible_become_pass= XXXXXXX


```
### know host 问题

```
Using a SSH password instead of a key is not possible because Host Key checking is enabled and sshpass does not support this.  Please add this host's fingerprint to your known_hosts file to manage this host.

```

添加`ansible.cfg`

```
[defaults]
host_key_checking = false
```

# 引用

1. [get-started](https://www.ansible.com/resources/get-started)
2. [ansible-github](https://github.com/ansible/ansible)
3. [jdauphant/awesome-ansible](https://github.com/jdauphant/awesome-ansible)
4. [awesome-devops/awesome-ansible](https://github.com/awesome-devops/awesome-ansible)
5. [ansible-generator](https://pypi.org/project/ansible-generator/)
6. [playbooks_best_practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
7. [使用 Ansible 高效交付 Docker 容器](https://www.ibm.com/developerworks/cn/cloud/library/cl-provision-docker-containers-ansible/index.html)
8. [ansilbe-docker_module](https://docs.ansible.com/ansible/2.6/modules/docker_module.html)
9. [Ansible入门](https://getansible.com/advance/playbook/includeyu_ju)
10. [playbooks_roles](https://ansible-tran.readthedocs.io/en/latest/docs/playbooks_roles.html)

