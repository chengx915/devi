# centos7修改默认启动方式

## 1.`vim /etc/inittab  ` 查看命令行模式与图形模式软连接的名称

`multi-user.target: analogous to runlevel 3 #命令行模式`

`graphical.target: analogous to runlevel 5 #图形模式`

## 2.使用命令`systemctl`，查看和更改启动模式

查看当前默认启动模式

`systemctl get-default `

更改启动模式为多用户命令行模式

`systemctl set-default multi-user.target `

更改启动模式为图形模式

`systemctl set-default graphical.target`

其实这个命令只是更改了一个软链接，`/etc/systemd/system/default.target`是一个软链接文件，所链接的文件就是各启动模式的配置文件，
多用户命令行模式的文件是`/usr/lib/systemd/system/multi-user.target`，
图形模式则是`/usr/lib/systemd/system/graphical.target`
