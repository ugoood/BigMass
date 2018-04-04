<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day04 Java Web 开发入门](#day04-java-web-开发入门)
  * [1. web 开发相关介绍](#1-web-开发相关介绍)
  * [2. web 服务器](#2-web-服务器)
  * [3. Tomcat服务器启动的问题](#3-tomcat服务器启动的问题)
  * [4. Tomcat目录结构](#4-tomcat目录结构)
  * [5. Web应用程序(虚拟目录映射，缺省web应用)](#5-web应用程序虚拟目录映射缺省web应用)
  * [6. Web应用的组成结构(web.xml，特定文件放入特定目录，否则web应用无法工作)](#6-web应用的组成结构webxml特定文件放入特定目录否则web应用无法工作)
  * [7. 配置虚拟主机](#7-配置虚拟主机)
    * [7.1 配置多个网站](#71-配置多个网站)

<!-- tocstop -->

Author：相忠良
email: ugoood@163.com
起始于：April 1, 2018
最后更新日期：April 2, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day04 Java Web 开发入门

## 1. web 开发相关介绍
web：表示网页。
Internet上供外界访问的Web资源分为两类：
* 静态 web 资源(如 html 页面)：指 web 页面中供人们访问的数据始终不变；
* 动态 web 资源：指 web 页面内容由程序产生，不同时间点人们访问 web 页面看到的内容不同；

静态 web 资源开发技术： html
常用的动态 web 资源开发技术： JSP/Servlet、ASP、PHP等。在 Java 中，动态 web 资源开发技术统称为 Javaweb。

## 2. web 服务器
我们的 web 资源想要为外界用户提供服务需有 web 服务器支持。Tomcat 服务器是免费的，即使用在商领域。
Tocmat官方站点：http://jakarta.apache.org
* tar.gz 对应 Linux OS
* exe 或者 zip 文件对应 Windows OS

教程里用的是`apache-tomcat-6.0.20`。
> 毕竟这教程视频距离现在有好几年了，我们也可用更新的版本，我机器用的是`apache-tomcat-8.5.9`，也不是最新的。

安装服务器时不要装在**中文目录或带空格目录**里，记得要留个备份。
启动服务器：在`C:\apache-tomcat-8.5.9\bin`中找到`startup.bat`双击它启动服务器。
验证：浏览器地址栏中输入`http://localhost:8080/`正常打开表示成功。

各种协议对应的端口：

| 协议 | 端口号 |
| ------- |:-------:|
| http | 80 |
| smtp | 25  |
| pop3 | 110  |
| ftp | 23 |
| https | 443 |

## 3. Tomcat服务器启动的问题
内容较为零散，几乎无先后顺序，如下：
* 需先配置`JAVA_HOME`环境变量。
* 8080端口被占用也无法启动服务器。工具`Fport.exe`可查看被占用端口。
* 测试的时候服务器用`8080`端口，上线后就用`80`端口。http默认访问`80`端口。
* `apache-tomcat-7.0.73\conf\server.xml`文件决定了Tomcat服务器启动方式。
* 认识`URL`:http://www.baidu.com
* 整个叫URL，`www.baidu.com`是主机名，`baidu.com`是域名。买的是域名，在一个域名下可搭建多台主机。如`pan.baidu.com`。
* `Catalina_home`环境变量指示了tomcat在哪里。当我们用`\apache-tomcat-7.0.73\bin\startup.bat`启动服务器后，os会自动寻找`Catalina_home`所指示的tomcat服务器(**无论你的`startup.bat`文件在哪里！**)。实际开发时最好不要配置这个环境变量。

## 4. Tomcat目录结构
bin: 启动和关闭tomcat的脚本文件
conf: 配置文件
lib: tomcat服务器的支持jar包
logs: 日志
temp: 存临时文件
webaaps: 重要，供外界访问的web资源存放地
work: tomcat工作目录

## 5. Web应用程序(虚拟目录映射，缺省web应用)
web应用程序：供浏览器访问的程序，也简称web应用。
web应用所在目录：组成web应用的这些文件，通常用一个目录来组织，这个目录称为web应用所在目录。
web应用开发好后，若想供外界访问，需要把web应用所在目录交给web服务器管理，<font color=red>这个过程称之为虚拟目录的映射</font>。

关于虚拟目录的映射，参照：http://localhost:8080/docs/config/context.html
里面有一句：
In individual files (with a ".xml" extension) in the `$CATALINA_BASE/conf/[enginename]/[hostname]/` directory. The context path and version will be derived from the base name of the file (the file name less the .xml extension). This file will always take precedence over any context.xml file packaged in the web application's META-INF directory.
意味着按照这种方法配置，可不用重启服务器，就能访问到页面。
试验步骤：
1. `c`盘根目录建立`news`目录，在该目录中建立`1.html`并写入内容`aaaaaa`；
2. 在`C:\apache-tomcat-8.5.9\conf\Catalina\localhost`目录下建立`a.xml`并写入`<Context docBase="c:\news"/>`。这时不需再配`path`这个对外访问路径了。`a.xml`中的`a`将作为对外访问路径。也可以再建立一个`b.xml`并写入`<Context docBase="c:\news"/>`，这样的话，同一个 web 应用可映射到两个路径上。
3. 验证：打开浏览器，地址栏输入http://localhost:8080/a/1.html，将显示网页内容。
4. 另外若将`C:\apache-tomcat-8.5.9\conf\Catalina\localhost`目录下建立`aa#bb.xml`写入`<Context docBase="c:\news"/>`,这时，我们可在浏览器中输入`http://localhost:8080/aa/bb/1.html`来访问`1.html`这个 web 资源。

**另一个简洁的配置方法是把`news`目录直接放到`C:\apache-tomcat-8.5.9\webapps`目录中。缺点是 web 应用程序和服务器放在了一起，开发时也许可以这样做，但实际配置中并不建议这样做。**

**再者，当输入`http://localhost:8080`时并没指定访问某web应用，但仍然访问了tomcat的首页，这和缺省有关。** 我们可以将`a.xml`更名为`ROOT.xml`，这样`1.html`这个web应用将成为缺省web应用。当输入`http://localhost:8080/1.html`时即可访问。

**最后，在`C:\apache-tomcat-8.5.9\conf\`** 目录中的 `server.xml`文件中`</Host>`前添加`<Context path="" docBase="c:\news"/>`也可配置 **缺省web应用**，但需<font color=red>重启服务器</font>。

## 6. Web应用的组成结构(web.xml，特定文件放入特定目录，否则web应用无法工作)
开发web应用时，<font color=red>不同类型的文件有严格的存放规则</font>，若违反，web应用将无法工作。
如图：
![1](/assets/1_abvist3wo.png)
自己实际操作一下。

需求：将 mail 这个web应用的 `1.html` 配置成首页。
步骤：
1. 在`webapps`目录中建立mail目录；
2. `/mail`中添加`1.html`并写入内容`我是首页`；
3. `/mail`中添加`WEB-INF`目录，并在`WEB-INF`中建立`web.xml`文件；
4. 在`web.xml`中写如下内容(可复制`C:\apache-tomcat-8.5.9\conf\web.xml`的头和尾):

```xml
<?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
  version="3.1">

    <welcome-file-list>
       <welcome-file>1.html</welcome-file>       
    </welcome-file-list>

</web-app>
```

按上述操作，我们访问`http://localhost:8080/mail/`就能直接访问到`1.html`这个首页。
接下来，我们要把`mail`这个web应用配置成缺省的，我们选择将文件`C:\apache-tomcat-8.5.9\conf\server.xml`中`<Host>`里添加`<Context path="" docBase="C:\apache-tomcat-8.5.9\webapps\mail"/>`。

直接输入`http://localhost:8080`就能出现`1.html`这个欢迎页面。

总结：
<font color=red>若想直接输入`http://localhost:8080`就能出现 mail 这个指定的 web 应用的指定的首页</font>，有2点要做：
1. 配置默认web应用为mail(`server.xml`里或者在`conf\Catalina\localhost`里用建xml文件的方法)；
2. 配置mail应用的首页(在`mail/WEB-INF/`下的`web.xml`中配置，**注意：可参考服务器的`web.xml`**)。

**内容显得凌乱，但直觉上，有个事儿得记住：**
**<font color=red>首页是web应用自己的事，当然应在那个应用的`web.xml`里配置；打开网站，默认哪个应用，这是tomcat服务器的事，当然应在服务器中做配置，既在服务器中的`server.xml`中或在`conf\Catalina\localhost`中建`xml`文件做配置！</font>**

另外，可把`server.xml`中的`8080`改成`80`端口的话，浏览器中输入`http://localhost`就能直接访问到 mail web 应用的`1.html`欢迎页面了。

下面图片展示了`web.xml`的重要作用：

![2](/assets/2_cdt4i02rv.png)

## 7. 配置虚拟主机
配置虚拟主机就是在tomcat服务器中配置一个网站。
1. 可在`server.xml`中添加 Host 元素进行配置，如：`<Host name="site1" appBase="c:\app"></Host>`
2. 配置的主机(网站)想要被外界访问，必须在DNS服务器或windows系统(`C:\Windows\System32\drivers\etc\hosts`)中注册。

### 7.1 配置多个网站
在一台主机上想配2个网站：`www.sina.com`和`www.google.com`
先配`www.sina.com`，假定该网站包含2个web应用`mail`和`news`步骤：
1. `server.xml`中加入一个Host标签：`<Host name="www.sina.com appBase="c:\sina"><Context path="/mail" docBase="c:\sina\mail"/><Context path="/news" docBase="c:\sina\news"/></Host>`
2. 在c盘根目录建立`c:\sina`目录，并分别建立`\mail`和`\news`子目录，并在`\mail`目录中建立`1.html`文件并写入`11111111111`的内容。
3. 因无法修改DNS服务器，只能改自己主机的host文件。把`C:\Windows\System32\drivers\etc\hosts`文件添加`127.0.0.1 www.sina.com`
4. 验证：浏览器中输入`http://www.sina.com/mail/1.html`即可。

谷歌那个网站也做相同配置，读者自己试一试。
