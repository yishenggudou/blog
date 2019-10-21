Title: Tmux使用记要
Date: 2019-10-21 17:00
Category: tool
Tags: tmux,shell,linux
Summary: Tmux使用记要
Status: published

# 背景

你有没有遇到,工作项目很多


# 笔记

## 安装

```
brew install tmux
brew install tmuxinator
```

## 使用

## 快捷键
![](/docs/blog/static/15716458229325.jpg)
![](/docs/blog/static/15716458509555.jpg)


## 最佳实践

编辑 `xcloud.yaml`

```yaml
session_name: x-cloud
windows:
  - window_name: x-cloud
    layout: tiled
    shell_command_before:
      - cd ~/                    # run as a first command in all panes
    panes:
      - shell_command:           # pane no. 1
          - sshpass -p 123123 ssh  -o=ProxyCommand="ssh -p 22  guide@10.10.10.1 nc -w 1 %h %p" -p 22 root@10.10.10.101          # run multiple commands in this pane
      - sshpass -p 123123 ssh  -o=ProxyCommand="ssh -p 22  guide@10.10.10.1 nc -w 1 %h %p" -p 22 root@10.10.10.102         # pane no. 2
      - ssh guide@10.10.10.1
      - ssh -D 19999  -C -f -q -N guide@10.10.10.1
```

使用

```bash
tmuxp load sessions/xcloud.yaml.yaml
```


# 引用

1. [awesome-tmux](https://github.com/rothgar/awesome-tmux)
2. [tmuxp-zh](https://tmuxp-zh.readthedocs.io/zh_CN/latest/about.html)
3. [libtmux](https://github.com/tmux-python/libtmux)
4. [十分钟学会 tmux](https://www.cnblogs.com/kaiye/p/6275207.html)
5. [tmux的超绝便利](https://segmentfault.com/a/1190000015143625)

