Python Learning
===
author: Xiang

# virtualev
>整理自http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被<code>pip</code>安装到Python3的<code>site-packages</code>目录下。
virtualev可以让每一个project拥有**各自独立Python运行环境**的隔离器。
假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：
Xiang已在ubuntu14.04环境下安装
```ruby
sudo pip install virtualenv
```
step1, 创建目录:
```ruby
mkdir myproject
cd myproject
```
step2, 创建一个独立的Python运行环境,命名为 <code>venv</code> :
```ruby
 virtualenv --no-site-packages venv
```
参数 <code>--no-site-packages</code> 使得安装在系统Python环境中的所有第三方包都不会复制过来，这样，我们就在<code>venv</code>目录下得到了一个不带任何第三方包的“**干净**”的Python运行环境。
step3, 用<code>source</code>进入该环境：
```ruby
source venv/bin/activate
```
在<code>venv</code>环境下，用 <code>pip</code>安装的包都被安装到<code>venv</code>这个环境下，系统Python环境不受任何影响。也就是说，<code>venv</code>环境是专门针对myproject这个应用创建的。

**final step**, 退出当前的<code>venv</code>环境，使用<code>deactivate</code>命令：
```ruby
deactivate
```
