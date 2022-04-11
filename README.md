# Lensi
## 简介

+ Lensi安装`pip install lensi`
+ Lensi CLI为360 qq scoop choco winget hippo的聚合命令行工具。
+ Lensi 现更新到0.1.2 （更新内容：upgrade命令）
+ PS. 本人即将面临中考，暂时没有长期维护打算
## 使用方法
+ CLI的制作为python fire模块
+ 主要命令: (简介) [具体参数(可选参数)] (备注)
  ```
  clean(清除Download缓存) [lensi clean]
  download(只下载文件，并打开文件夹) [lensi download <app_name> (<app_source>)]
  info(显示软件的详细信息) [lensi info <app_name> (<app_source>)]
  init(消除整个lensi文件夹) [lensi init]
  install(正常安装软件) [lensi install <app_name> (<app_source>)]
  list(显示由lensi安装的软件) [lensi list]
  search(搜索功能，聚合搜索) [lensi search <app_name> (<app_source> <limmit_num>)]
  set(一些设置) [lensi set <set_options>] (具体设置看下文，lensi set显示所有设置)
  uninstall(卸载软件(软件范围是电脑中的所有软件)) [lensi uninstall <app_name>]
  upgrade(更新软件(只限通过lensi下载安装的软件)) [lensi upgrade (<app_name>)] (之间lensi upgrade代表更新所有）
  ```
+ 各个命令具体参数使用help可查看
+ 设置（备注）：
```
[Lensi]
qq_num = 1（qq搜索个数，默认1）
360_num = 1（360搜索个数，默认1）
Scoop_num = 1（Scoop搜索个数，默认1）
Winget_num = 1（Winet搜索个数，默认1）
Choco_num = 1（Choco搜索个数，默认1）
DAI(DeletedAfterInstalled) = True
（下载安装包后自动删除，默认开启）
SO(SimplyOpen) = True
（安装包只是简单的打开，默认开启，若关闭则有不部分exe msi自动静默安装，zip自动解压并创建桌面（开始菜单）快捷方式等测试性功能）
ES(EnableScoop) = True
（Scoop搜索是否开启，默认开启，运行时会检测是否装有Scoop，若没有则自动调为False）
EC(EnableChoco) = True
（Choco搜索是否开启，默认开启，运行时会检测是否装有Choco，若没有则自动调为False）
EW(EnableWinget) = True
（Winget搜索是否开启，默认开启）（Choco，Winget开启可能会延长搜索时间）
SIP(ScoopInstallPath) = D:\Scoop
（Scoop安装路径，默认在“ D:\Scoop”）（lensi自动解析Scoop\buckets文件夹，加快Scoop搜索速度）
NI(NormalInstall) = qq
（lensi install <app_name>不加app_source的默认源，默认qq）
（The available source is : qq(q) 360(b) scoop(s) hippo(h) choco(c) winget(w)）
WT(Waittime) = 3
（搜索等待时间，默认3，若为0或负数则为等待所有源搜索完毕）
HAF(HowAccurateFuzzywuzzy) = 80
（更新，卸载所用检测是否存在这个软件的参数，默认80，可以调到80以上更加准确，但有可能查找不到）
```