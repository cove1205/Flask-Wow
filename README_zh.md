# <center>**Flask-Wow**</center>

[![Build Status](https://www.travis-ci.com/ganquan881205/Flask-Wow.svg?branch=master)](https://www.travis-ci.com/ganquan881205/Flask-Wow)

## Flask-Wow是什么

Flask-Wow是一个简单的CLI工具，和Django的内置cli类似，可以用来新建flask项目或者添加业务模块

## 依赖

- Python 3.6 +
- click 7.0 +

## 如何使用

- 安装

```bash
sudo pip3 install flask-wow
```

- 卸载

```bash
sudo pip3 uninstall flask-wow
```

### 创建项目

- 在想要创建项目的目录下,执行创建命令,将your_project_name替换成你的项目名称

```bash
flask-wow startproject your_project_name -v
```
- ### 新建app

  进入项目根目录，执行命令

```bash
cd projecet_name

flask-wow startapp your_app_name 
```

- -v或者 --venv 选项可以用来告诉程序是否需要创建python虚拟环境

- 这样一个新的项目就创建完成了，目录结构大致是这样：

```bash
/some_folder
    /your_project_name
        run.py -> 测试用脚本
        wsgi.py -> 生产环境部署用脚本
        __init__.py
        config.py -> 默认配置文件
        handlers.py -> 中间件和全局错误处理
        requirements.txt -> 依赖文件
        /utils  ->  工具函数
        /apps -> 存放业务模块代码
            /demo -> 示例程序
                __init__.py
                views.py
                models.py
    /venv -> 虚拟环境文件夹
```

## ChangeLog

- 0.2.0   添加新建app的功能、重新构建项目目录

- 0.1.0   project init.

## TODO

- 增加测试
- 完善新建项目示例
- 代码优化

## Contribution

有任何意见和建议欢迎开issues或者PR,也可以发送邮件cove@happyeyez.com
