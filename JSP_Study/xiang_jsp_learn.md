Xiang's Java Server Pages Study
====
阿里云（镜像），包括atom。https://npm.taobao.org/

# jsp Environment Established

## jdk7.0
配置环境变量：
JAVA_HOME, JAVA_JRE, Path, CLASSPATH

## tomcat7.0
配置环境变量：
CATALINA_HOME=C:\apache-tomcat-7.0.73

到tomcat主目录的bin目录中找startup，运行之；关闭是shutdown

测试：explorer地址栏中输入http://localhost:8080

## DIY Your First Website：
- webapps里创建自己的文件夹xiang_home
- 在xiang_home/中创建
	index.jsp
	/WEB-INF/

index.jsp中写入：
```html
<!doctype jsp>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="Generator" content="EditPlus?">
  <meta name="Author" content="">
  <meta name="Keywords" content="">
  <meta name="Description" content="">
  <title>我的第一个jsp页面(My first jsp page)</title>
 </head>
 <body>
	<h1>欢迎来到Xiang的家(Welcome to Xiang's home)</h1>
	<hr>
 </body>
</html>
```

/WEB-INF/中创建 classes 文件夹和 lib文件夹 以及 web.xml文件
web.xml文件的内容是：
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                      http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
  version="3.0"
  metadata-complete="true">

</web-app>
```

最后验证，输入地址http://localhost:8080/xiang_home/index.jsp查看结果（乱码的话，在浏览器空白处右键选择“编码”选项）。

## 认识WEB-INF目录
1. WEB-INF是安全目录，client-site无法访问，而server-site可以访问；
2. web.xml，项目部署文件。原来默认index.jsp为网站默认访问页，想修改，则改web.xml，代码如下：
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                      http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
  version="3.0"
  metadata-complete="true">

<welcome-file-list>
	<welcome-file>/haha.jsp</welcome-file>		
</welcome-file-list>

</web-app>
```
上面代码把默认index.jsp改成了haha.jsp。
3. /classes，存放编译了的字节码文件；
4. /lib, 存放项目用到的jar包。

## MyEclipse10 与 Eclipse 关于JavaWeb开发的配置
- **eclipse仍然可以开发javaweb应用程序，视频1-10有详细过程，但众多网友，包括我在内砸了键盘！太坑了(视频先讲了MyEclipse10的配置，配置了半天（下载MyEclipse10时间挺长的），最后又讲了Eclipse的配置 http://www.imooc.com/video/2931/0)！**。
	* 打开eclipse, 打开javeEE视图,右上角
	* new-->project-->Web-->Dynamic Web Project-->下一步按钮
	* Target runtime 处选择 tomcat7-->下一步按钮
	* 选择Tomcat7安装的主目录   JRE-->选择jdk7.0  然后一顿finish.
	* 在创建好的JavaEE项目中的 WebContent文件夹中创建 index.jsp, 编辑之；
	* 更改index.jsp文件中的字符集，既： charset = UTF-8， 修改标题title, body中增加一个
	```html
	<h1>欢迎来搞javaEE!!</h1>
	```
	* 运行这个project: 点击本工程--> Run As --> Run on Server, 运行完成，并可在浏览器中观察结果。
- 一大块内容，MyEclipse10中搭建Tomcat7。
- 项目的虚拟路径设置
	* 项目名右击
	* 属性
	* MyEclipse
	* Web
	* 修改虚拟路径
- 修改Tomcat Server 默认端口号
	* 到Tomcat主目录中找并修改conf/server.xml文件
	```xml
	<Connector port = "8080"
		protocol = "HTTP/1.1"
		connection Timeout = "20000"
		redirectPort = "8443"
	/>
	```
## MyEclispse2014 for ubuntu14.04 Configuration
1. 安装jdk环境 Java 1.7
2. 下载https://www.genuitec.com/products/myeclipse/download/get/?2014-ga-pro-linux
3. 运行 ./myeclipse-pro-2014-GA-offline-installer-linux.run
4. 下载破解文件http://pan.baidu.com/s/1jG0twlK，并解压文件。
    打开文件 run.bat ，将里面的内容复制到终端（javaw -jar cracker.jar）并修改为Java -jar cracker.jar运行
5. 接下来参照windows破解http://jingyan.baidu.com/album/7082dc1c57eb19e40a89bdcd.html?picindex=8 ，即可完成破解。
