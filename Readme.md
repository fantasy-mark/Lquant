# Lquant简介
===================
1. 目录结构
-------------------
    .
    │  main.py                    # 主程序
    │  Readme.md                  # 简介
    │                             #
    ├─Config                      # 配置文件目录
    ├─Data                        # Tushare及数据库等文件
    ├─GUI                         # 图形界面
    ├─Home                        # 用户目录
    │      IPyhon_NoteBook.py     # 执行开启Hello world之旅!
    │                             #
    ├─Indicator                   # 指标
    ├─Strategy                    # 策略
    └─Trade                       # 各券商交易API

2. 加入项目, 君约否?
-------------------
### 获取源码
    git clone https://github.com/fantasy-mark/Lquant.git

### 添加远程仓库
    git remote add origin https://github.com/fantasy-mark/Lquant.git

### 提交本地的master分支到远程分支
    git add -A
    git commit -m "干了啥?"
    git push -u origin master

### 撤销未push的commit,恢复代码
	git log
	git reset --hard commit_id
### 撤销未push的commit,不恢复代码
	git reset commit_id

### 强制以本地仓库覆盖远程某分支仓库(已push公开情况)
```bash
# 配合上面reset撤销commit来操作
git push origin branch_name --force
```
### 回滚某提交
    git checkout commit_id

### 查看仓库中文件
	git ls-files

### 分支策略（简易版）
```bash
# origin/master分支用于版本发布
# origin/develop分支用于主开发, 若无创建一个
git branch develop
git push -u origin develop

# 若已有origin/master, 则直接拉下来
git pull origin deveplo
```
```bash
# 创建并切换本地临时分支fix-bug, 进行本地开发
git branch fix-bug
git checkout fix-bug

git add -A
git commit -m 'XXX'
```
```bash
# 切换到develop分支, 把fix-bug分支合并进develop分支, push
git checkout develop
git merge --no-ff fix-bug
git push origin develop
# 本地临时分支用法就可以删除了
git branch -d some-feature
```
### 打标签,用于版本发布
	git tag
	git tag -a 0.1_161219_beta commit_id
	git push origin 0.1_161219_beta
	
### [简明git教程](http://www.cnblogs.com/schaepher/p/5561193.html)<br/>
### [分支管理策略](http://www.cnblogs.com/cnblogsfans/p/5075073.html)<br/>
### [Readme.md排版](http://mahua.jser.me/)<br/>
### [上传github后乱码](https://my.oschina.net/u/178116/blog/386095)<br/>
