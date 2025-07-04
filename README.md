# Duo小镇开发仓库

## 项目结构

### `app/` 文件夹
- 存放该项目的Django后端代码
- 平时由小林负责

### `vue/` 文件夹
- 存放该项目的Vue前端代码
- 平时由小林和小刘负责

## 运行测试
在`Vue/shell/`文件夹里面找到`run.sh`

执行命令：
```shell
sh run.sh
```
如果是`Windows`系统则需要安装`Git Bash`或者`WSL`
然后执行该命令

## Git操作
- 切换到项目文件夹
```shell
cd Duo小镇/
```

- 进行 Git 注册
```shell
git config --global user.name "名字"
git config --global user.email "邮箱"
```

- 如果电脑里面还没有Duo小镇，进行拉取到本地
```shell
git clone https://gitee.com/duo-studio/duo-town.git
```

- 执行该命令来获取`npm`依赖
```shell
npm install
```

- 编写好了代码后把发送到暂存区(就是相当于一辆快递车)
- git会自动发送已修改的内容：包括修改、删除、添加
```shell
git add .
```

- 填写本次更新内容(相当于写快递名)
```shell
git commit -m "更新内容"
```

- 快递编写好了，告诉小车车我们的快递要发送到哪里？(直接复制)
```shell
git remote add origin https://gitee.com/linsifan123/test.git
```

- OK，小车车启动！发射到远程仓库!
```shell
git push -u origin "master" 
```