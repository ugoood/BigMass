# C++ Trick
Begin  : 2018.7.7
End	   : 2018.7.7
Author : Xiang
Email  : ugoood@163.com

本文档记录了在 ubuntu16.06 环境下学习 c++ 中遇到的一些我不知道的小东西。
## 1. strip 命令让文件变小
ubuntu 中有个 strip 命令，可把 c++ 编译好的程序变小。假设我们有个编译好的 c++　文件，名为 test，在 terminal 中操作如下：

```
ls -alh test // 查看大小
strip test
ls -alh test // 再查看大小
```

## 2. file 命令查看文件属性
ubuntu 中 file 命令查看文件属性。如`file test`显示test文件属性如下：


test : ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=902762c9cd77c8943c977e6c918a93aed126ba14, stripped
