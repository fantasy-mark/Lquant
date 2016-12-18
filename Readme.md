# Lquant简介
===================
1. 目录结构
-------------------
    .
    │  main.py                  # 主程序
    │  Readme.md                # 简介
    │                           # 
    ├─Config                    # 配置文件目录
    ├─Data                      # Tushare及数据库等文件
    ├─GUI                       # 图形界面
    ├─Home                      # 用户目录
    │      IPyhon_NoteBook.py   # 执行开启Hello world之旅!
    │                           # 
    ├─Indicator                 # 指标
    ├─Strategy                  # 策略
    └─Trade                     # 各券商交易API

2. 加入项目, 君约否?
-------------------
###获取源码
    git clone https://github.com/fantasy-mark/Lquant.git

###添加远程仓库
    git remote add origin https://github.com/fantasy-mark/Lquant.git

###提交本地的master分支到远程分支
    git add -A
    git commit -m "干了啥?"
    git push -u origin master

###撤销未push的commit,恢复代码
	git log
	git reset --hard commit_id
###撤销未push的commit,不恢复代码
	git reset commit_id
	
###[简明git教程](http://www.cnblogs.com/schaepher/p/5561193.html)<br/>
###[Readme.md排版](http://mahua.jser.me/)<br/>
