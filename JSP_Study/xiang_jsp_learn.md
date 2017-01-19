Xiang's Java Server Pages Study
====
阿里云（镜像），包括atom。https://npm.taobao.org/

# 1. Java Web Introduction
## jsp Environment Established

* jdk7.0
配置环境变量：
JAVA_HOME, JAVA_JRE, Path, CLASSPATH

* tomcat7.0
配置环境变量：
```shell
CATALINA_HOME=C:\apache-tomcat-7.0.73
```
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
	* 更改index.jsp文件中的字符集，既：charset = UTF-8，修改标题title, body中增加一个
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

# 2. JSP Basic Grammar
> 1. page command
> 2. Jsp annotation
> 3. Jsp script
> 4. Jsp declaration
> 5. Jsp expression
> 6. Jsp pages life cycle
> 7. Stage project
## page指令
page指令有language import contentType等字段。
```xml
<%@ page language="java" import="java.util.*" contentType="text/html; charset=utf-8"%>
```
- 在MyEclispse2014中，命令提示是：**alt+/**
## Jsp注释
	- <!-- html注释 --> //客户端查看源代码时，注释可见
	- <%-- JSP注释 --%> //客户端不可见
	- ```xml
		//单行注释   /* */多行注释
		```

	-	```xml
		<% //单行    /*多行*/  %>
		```

## Jsp脚本
在JSP页面中执行的java代码。
Grammar:
```xml
<%java代码%>
```
e.g.
```xml
<% out.println("欢迎大家学习javaee开发"); %>
```

## Jsp声明
在Jsp页面中定义**变量**或者**方法**。
Grammar:
```xml
<%! java code %>
```
e.g.
```xml
<%!
  	String s = "张3"; //declare a string var.
  	int add(int a, int b){
  		return a+b;
  	}
%>
```

## Jsp表达式
Grammar:
<%= 表达式 %> //注意：表达式不以分号结束
e.g.
```xml
	<%!
  		String s = "张3"; //declare a string var.
  		int add(int a, int b){
  			return a+b;
  		}
  	%>

    <%
    	out.println("欢迎大家学习javaee开发");
			out.println(s);//调用生明里的s
    %>
    <br>
    你好，<%=s %><br> //表达式
    x+y=<%=add(10,22) %> //表达式
```

## Jsp页面的生命周期
本节说了个
```
C:\apache-tomcat-8.5.9\work\Catalina\localhost\test\org\apache\jsp
```
其中，\work目录是服务器存放java源文件和字节码文件的地方。当第一个client访问该jsp页面时，该页面将被编译，jsp页面在服务器更新时，有人访问的话，也会重新编译。否则，不再编译。
视频未解释清楚的一个方法，如下：
当用户第一次请求一个jsp页面时，首先被执行的方法是jspInit(), 一个initiate方法, 答案是不对， 是构造方法~！ 什么玩意~
```xml
	<%
		//ctrl+/自动import所需类
    	SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
    	String s = sdf.format(new Date());
    %>
```
## 阶段项目
打印99乘法表
```xml
<%!
  		String mul(){
  			String s = "";
  			for(int i = 1; i <= 9; i++){
  				for (int j=1; j <= i; j++)
  				{
  					s += i+" * "+j+" = "+(i*j)+"&nbsp;&nbsp;&nbsp;&nbsp;";
  				}
  				s += "<br>";
  			}
  			return s;
  		}
  	%>
    <h1>99乘法表</h1>
   	下面是99乘法表<br>
   	<%=mul() %>
```

```xml
<%!  		  		
  		void printmt(JspWriter out) throws Exception {//注意和上例的区别
  			for(int i = 1; i <= 9; i++){
  				for (int j=1; j <= i; j++)
  				{
  					out.println(i+"*"+j+"="+(i*j)+"&nbsp;&nbsp;&nbsp;&nbsp;");
  				}
  				out.println("<br>");
  			}
  		}
  	%>
    <h1>99乘法表</h1>
   	下面是99乘法表<br>
   	<%printmt(out); %> //再注意这里。
```

# 3. Jsp内置对象(上)
本章内容：

>1. 内置对象简介
>2. 四种作用域范围
>3. out
>4. request/response
>5. session
>6. application
>7. 其他内置对象
>8. 项目案例
## 内置对象简介
JSP内置对象是Web容器创建的一组对象，不使用__new__创建之，就可使用的内置对象。
e.g.
```xml
int[] value={60,70,80};
for(int i:value){
	out.println(i); //out是内置对象
}
```
JSP有九大内置对象：
* out
* request/response
* session
* application
* 不太常用的：page, pageContext, excption, config.
client(可以认为是浏览器)发request, web server 接收到request, 然后response.
## 四种作用域范围

## out
out对象是JspWriter类的实例，经常用于向客户端（浏览器）输出内容。
out对象的常用发法：
* void println() 打印字符串
* void clear() 清除buffer的内容，如果在flush后调用，会抛出异常
	- void clearBuffer() 同上，但在flush后调用不会抛出异常
* void flush() 冲厕所技能，它将buffer内的内容输出到客户端
* int getBufferSize() 返回buffer字节数大小，若不设buffer则为0
* int getRemaining() 返回buffer还剩多少可用
* boolean isAutoFlush() 缓冲区满时，是自动清空还是抛出异常
* void close() 关流
e.g.
```xml
<body>
		 <h1>out内置对象</h1>
	<%
		out.println("<h2>静夜思</h2>");
		out.println("床前明月光<br>");
		out.println("疑是地上霜<br>");
		out.flush();
		//在flush()之后，用out.clear()，服务器会抛出异常;
		out.println("举头望明月<br>");
		out.println("低头思故乡<br>");
	%>
	缓冲区大小：<%=out.getBufferSize() %><br>
	缓冲区剩余大小：<%=out.getRemaining() %><br>
	是否自动清空缓冲区：<%=out.isAutoFlush() %><br>
</body>
```
### get 与 post 区别
```xml
<form name="regForm" action="动作" method=“提交方式”>
</form>
```
表单提交方式有两种：get和post
* get: 提交的数据在url中可以看到，数据最多不超过2KB。适合提交小数据量，安全性低的数据。如：搜索、查询；
* post: 提交信息会封装在 HTML HEADER 内。适合数据量大，安全性高的数据。如：注册、修改、上传等功能。
下面的例子将展现上面所述的特性：
e.g.
建立login.jsp:
```xml
<body>
    <h1>用户登录</h1>
    <hr>
    <form action="dologin.jsp" name="loginform" method="post"> <!--试一试post-->
      <table>
    	<tr>
    		<td>用户名：</td>
    		<td><input type="text" name="username"/></td>
    	</tr>
    	<tr>
    		<td>密码：</td>
    		<td><input type="password" name="password"/></td>
    	</tr>
    	<tr>
    		<td colspan="2"><input type="submit" value="登录"></td>
    	</tr>
      </table>
    </form>
  </body>
```
建立dologin.jsp:
```xml
<body>
    <h1>登录成功</h1>
    <hr>
</body>
```
这样，服务器端就获得了用户提交的信息，具体是什么情况？ 看下节。

## request/response

## session

## application

## 其他内置对象

## 项目案例
