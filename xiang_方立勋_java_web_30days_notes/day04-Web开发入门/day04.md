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
  * [8. web资源访问流程](#8-web资源访问流程)
  * [9. 打包 web 应用 war](#9-打包-web-应用-war)
  * [10. 配Context元素的reloadable属性为true，让tomcat自动加载更新后的web应用](#10-配context元素的reloadable属性为true让tomcat自动加载更新后的web应用)
  * [11. Tomcat 体系结构](#11-tomcat-体系结构)
  * [12. 软件密码学基础和配置 https 连接器](#12-软件密码学基础和配置-https-连接器)
    * [12.1 软件密码学基础](#121-软件密码学基础)
    * [12.2 配置 https 连接器](#122-配置-https-连接器)
  * [13. Tomcat管理平台](#13-tomcat管理平台)
  * [14. HTTP协议](#14-http协议)
  * [15. HTTP请求](#15-http请求)
    * [15.1 HTTP 的 get 和 post 请求](#151-http-的-get-和-post-请求)
    * [15.2 HTTP 的 请求头的解释](#152-http-的-请求头的解释)
  * [16. HTTP响应](#16-http响应)
    * [16.1 响应头的解释](#161-响应头的解释)
    * [16.2 响应头 - Range头，断点续传](#162-响应头-range头断点续传)

<!-- tocstop -->

Author：相忠良
email: ugoood@163.com
起始于：April 1, 2018
最后更新日期：April 13, 2018

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

## 8. web资源访问流程
当我们在浏览器中输入`http://www.sina.com/mail/1.html`后，在浏览器中看到了返回的结果。这个过程是怎样的呢？如下：
1. ie->windows的host文件： 查询windows,获取主机名对应的ip；
2. ie->dns服务器：查询dns,获取主机名对应的ip;
3. ie->sina的web服务器：用查询到的ip连sina服务器并发送http请求；
4. sina的web服务器从请求信息中可获得客户机 **想访问的主机名**；
5. sina的web服务器从请求信息中可获得客户机 **想访问的web应用 mail**；
6. sina的web服务器从请求信息中可获得客户机 **想访问的web资源 1.html**；
7. sina的web服务器->web资源1.html：sina的web服务器读取相应主机下的、web应用下的web资源；
8. **sina的web服务器用读取到的web资源的数据，创建出一个http响应**；
9. sina的web服务器->ie：服务器回送http响应；
10. ie浏览器收到http响应，解析出资源数据并显示。

## 9. 打包 web 应用 war
将web应用打成 war 包，方便部署，且服务器对 war 包自动解压。
以google的news这个web应用为例，将其打成 `news.war`：
在dos命令行模式下，进入`c:\google`目录，输入`jar -cvf news.war news`生成`news.war`包。当我们把`news.war`发布到tomcat服务器的`webapps`目录下时，服务器会将其自动解压。

## 10. 配Context元素的reloadable属性为true，让tomcat自动加载更新后的web应用
如在`server.xml`文件中：

```xml
<Host name="www.google.com" appBase="c:\google">
  <Context path="" docBase="c:\google\mail" reloadable="true" />
</Host>
```

这种方式开发时用，部署时不用。web应用小时用，大时不用。
注意：
在`conf\context.xml`中配的`Context`元素会被服务器中所有应用所共享，reloadable一般不应在这里配置。<font color=red>这里是全局性的配置</font>。

## 11. Tomcat 体系结构
如图：
![3](/assets/3_ll3eiw7rx.png)
**<font color=red>`Server -> Service -> 启动多个 Connector 响应客户端请求 -> Engine -> Host -> Context`</font>**
可查看`server.xml`感受上述过程。上图就是根据`server.xml`画出来的。

## 12. 软件密码学基础和配置 https 连接器
### 12.1 软件密码学基础
涉及以下概念：
公钥，私钥：公钥加密的东西，私钥解；私钥加密的东西，公钥解；公钥加密的东西，公钥解不开；私钥加密的东西，私钥解不开。
CA：是一个可信任的机构。密码学领域里必须有一个信任点。网站向社会提供的公钥需由CA认证，才会被浏览器(也就是用户)认可。
数字证书：由CA认证过的公钥；
**数字签名：数据发送者通过自己的私钥将数据摘要加密，连同用数字证书加密好的数据一同发送给接收者。前提是接收者有发送者的数字证书(既公钥)。数字签名的目的是向接收者证明，这份文件是发送者发出的，如：接收者用发送者的数字证书若能解开数据摘要a，说明该信的确为发送者发出的，解开数据摘要a后，接收者用自己的私钥解开信件获取原始数据，再用md5算法得到数据摘要b，若 a==b，说明文档没被篡改，且确实是由指定的发送者发出。**
摘要，md5算法：要传输的数据通过md5算法生成数据摘要。

故事：
客户打开我们做的网站，在客户的浏览器上输入银行的用户名和密码，这得加密啊，咋整？按照上面提到的各种概念，对号入座。
为了客户的用户名和密码的安全，需加密后通过网络传输到我们的web服务器。这就需在我们的web服务器上配置公钥(数字证书，但做实验的话，这证书不会通过CA认证，既这根本不是个数字证书)，并把这个数字证书通过网络传给客户。客户得到证书后，发送的用户名和密码或其他信息就都是经过证书加密的信息了。我们的web服务器通过那个成对的私钥解密传过来的信息即可。这是单方加密，实际开发中用的是双方加密。

实际操作在下节。

### 12.2 配置 https 连接器
本节涉及2个任务：
1. 为我们的web服务器生成一个数字证书；
2. 为我们的web服务器配置一个加密的连接器(https Connector)；

生成数字证书：java 自带的工具 `keytool -genkey -alias tomcat -keyalg RSA`
密码“123456”，操作如图：
![4](/assets/4_xo63h31jf.png)
最终生成了`.keystore`的密钥库。我的机器来说，该文件存放在`C:\Users\ugooo`目录下。

配加密的web服务器：
将`.keystore`转移到tomcat服务器的`conf\`目录下。
打开`server.xml`添加一个加密的`Connector`，代码如下：

```xml
<Connector port="8443" protocol="HTTP/1.1"
          maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
          clientAuth="false" sslProtocol="TLS" keystoreFile="conf/.keystore" keystorePass="123456" />
```

注意上面代码中的`keystoreFile="conf/.keystore" keystorePass="123456"`表明了密匙库位置和开启密匙库的密码。这些属性信息都可在 Tomcat 主页的 Configuration 中的 Connector 中查询得到。
重启服务器后，浏览器输入`https://localhost:8443/`，查看效果(涉及到安装证书)。

## 13. Tomcat管理平台
进入tomcat首页，点击 **Tomcat Manager**。
设置用户名和密码：
在`conf\`目录下，打开`tomcat-users.xml`文件，在`<tomcat-users>`元素下添加如下代码：

```xml
<role rolename="tomcat"/>
<role rolename="role1"/>
<role rolename="manager-status"/>
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<role rolename="manager-jmx"/>
<user username="tomcat" password="123456" roles="tomcat,manager-status,manager-gui,manager-script,manager-jmx"/>   
```

用户名tomcat，密码123456。这时打开Tomcat Manager，输入用户名密码即可进入管理平台。

## 14. HTTP协议
HTTP：Hypertext Transfer protocol(超文本传输协议)，它是<font color=red>TCP/IP协议的一个应用层协议(意思是：http协议是工作在tcp/ip协议之上的，即得先用tcp/ip协议连接上后，http协议才可工作)</font>，用于定义WEB浏览器与WEB服务器之间交换数据的过程。

HTTP协议与平台无关。

1.html代码如下：

```html
aaaaaaaa
<img src="1.jpg">
<img src="2.jpg">
<img src="3.jpg">
```

当在浏览器中输入1.html的网址，按回车后，服务器共受了浏览器4次请求。

## 15. HTTP请求
### 15.1 HTTP 的 get 和 post 请求
![5](/assets/5_lpbuzi3sl.png)
![6](/assets/6_ct6mf91j4.png)

post请求带数据给服务器，方法就是用表单，如下html代码：

```html
<form action="/1.html" method="post">
	<input type="text" name="username">	<input type="submit" value="提交">
</form>
```

get请求带数据给服务器，如下html代码(点击超链接时，带数据给服务器)：

```html
<a href="/2.html?username=aaaaa">点点</a>
```

### 15.2 HTTP 的 请求头的解释
![7](/assets/7_g0qxt7bc3.png)
![8](/assets/8_4vf93ycgd.png)
其中的 If-Modified-Since 表示客户机缓存了这个页面的时间，通常用于与服务器那个页面的刷新时间的比对，若早于服务器那个页面的刷新时间，说明客户机缓存过的这个页面较老，服务器会重新传最新的页面给客户机。否则就不传了，这样就能减轻web服务器的压力。

## 16. HTTP响应
故事：我们平时打开网页有时候数据显示在页面，有时会打开一个下载对话框，这都是客户机根据服务器回送的响应中的响应头作出的对应动作。
<font color=blue>重要直觉：服务器可以通过响应头，控制客户机浏览器的行为！</font>
![9](/assets/9_m5blv3rij.png)
![10](/assets/10_8ocp2ro2m.png)
302：你请求我，我要你去找别人(服务器会回送1个location头，让你去找location头所指示的地址)；
307和304：服务器不给你所请求的资源了，它让你找你去自己机器上的缓存找你要的资源；
404：一定是客户机地址写错了，即你请求的资源服务器没有；
403：客户机没权限访问服务器的那个资源(服务器有那个资源);
500: 服务器端出问题了。

### 16.1 响应头的解释
响应头的解释
![11](/assets/11_7ms66rf31.png)

### 16.2 响应头 - Range头，断点续传
![12](/assets/12_8owwptsgx.png)
