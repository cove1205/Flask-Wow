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

- -v或者 --venv 选项可以用来告诉程序是否需要创建python虚拟环境

- 这样一个新的项目就创建完成了，目录结构大致是这样：

```bash
/your_project_name -> 项目根目录
    run.py -> 测试用脚本
    wsgi.py -> 生产环境部署用脚本
    /requirements -> 依赖配置文件夹，区分开发和生产环境
        requirements_dev.txt
        requirements_prod.txt
    /your_project_name ->
        __init__.py
        config.py -> 默认配置文件
        handlers.py -> 中间件和全局错误处理
        /utils  ->  存放一些工具函数
        /apps -> 存放业务模块代码
            /demo -> 示例程序
                __init__.py
                views.py
                models.py
    /venv -> 虚拟环境文件夹
```

## ChangeLog

- 0.1.0   project init.

## TODO

- 增加测试
- 增加新的命令用来新建业务模块(类似Django中的app)
- 完善新建项目示例
- 代码优化

## Contribution

有任何意见和建议欢迎开issues或者PR,也可以发送邮件cove@happyeyez.com

If you have any ideas or suggestions about this project，please feel free to fork、open issues and send pull requests.
Or send e-mail to cove@happyeyez.com
