# FingertipFlying

A Mac app that records the number of keystrokes on the keyboard.


## Usages

1、直接运行

2、将 `FingertipFlying.app` 拷贝到访达里的 `应用程序` 中，这样使用更方便

Tips: 按住 `Command` 键不松，鼠标点击菜单栏图标向右拖动到可以看到的位置，可以避免图标被遮挡导致看不到

软件不联网，也不储存什么文件，只需要获取读键盘的权限就行，软件重启会从零开始重新计数。

## Build


```bash
./setup.sh
```

生成的 app 中会缺少 `libffi.7.dylib` ，需要手动拷贝到 `/Contents/Frameworks/` 里边。

## TODO

- [ ] 去除 Dock 上的图标显示
- [ ] 在本地保存日志，记录每天的次数以及高频按键
- [ ] 自动化打包问题，即不需要手动拷贝依赖
- [ ] 看状态曲线
- [ ] 状态栏变FF或者图标

## About
Keep typing, create anything you want.

Contact Me: yanyuxiangtoday@163.com

### Reference:
FingertipFlying was forked from [201419/CountKey](https://github.com/201419/CountKey)  
CountKey v1.0.0 was made in 2021 by YangShu.  
Contact YangShu: yangshu1109@gmail.com  
