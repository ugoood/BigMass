Emergency for Xiang When Using Ubuntu
====
date: Feb 11th, 2017
author: Xiang
I've spent one full day to solve this little porblem that I met today. I am going to install ```appdirs for python```, finally it worked. Don't taunt to me! :)
1. for os installation comming from Ubuntu（https://launchpad.net/ubuntu）.
```sudo apt-get install/delete python-appdirs  # install or delete```
```sudo apt-get install python3-appdirs```
for python liabary stemming from PyPI（https://www.python.org/）
```pip install/uninstall numpy     # for python2.7```
```pip3 install numpy     # for python3.x, there are not disturbing between pip and pip3 when we used them.```

2. details for above information: http://www.linuxdiyf.com/linux/13091.html
most usful information are shown as following:
```
$ sudo apt-get install/delete package
$ sudo apt-get -f install             #修复安装
$ sudo apt-get dist-upgrade           #升级系统
$ sudo apt-get upgrade                #更新已安装的包
$ apt-get source package              #下载该包的源代码
$ sudo apt-get build-dep package      #安装相关的编译环境
$ sudo apt-get clean && sudo apt-get autoclean  #清理无用的包
```

pip需要安装才能使用，配合virtualenvwrapper会锦上添花。安装过程如下（适用Ubuntu 10.10及以上版本）:
```
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install --upgrade pip
$ sudo pip install --upgrade virtualenv
```

3. When we install a source package(after unpack .gz file and go into that direcotrory), e.g. appdirs-1.4.0, in the package, we notice setup.py file existing, we do as follows:
    ```
    $ sudu python setup.py install
    ```
    Please do not follow the **stupid way** when we come across #3 issue: ```$ ./configure   $ make   $ makefile```
