<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day05 Servlet 开发和 ServletConfig 与 ServletContext 对象](#day05-servlet-开发和-servletconfig-与-servletcontext-对象)
  * [1. Servlet 开发入门 - hello world](#1-servlet-开发入门-hello-world)
  * [2. Servlet 的调用过程和生命周期](#2-servlet-的调用过程和生命周期)
  * [3. 使用 Eclipse 开发 Servlet](#3-使用-eclipse-开发-servlet)
  * [4. HttpServlet 和一些开发细节](#4-httpservlet-和一些开发细节)
  * [5. Servlet 开发的一些重要细节](#5-servlet-开发的一些重要细节)
  * [6. Servlet的线程安全](#6-servlet的线程安全)
    * [6.1 Servlet的线程安全的产生及同步锁解决方案(然并卵方案)](#61-servlet的线程安全的产生及同步锁解决方案然并卵方案)
    * [6.2 Servlet的线程安全可行解决方案(结论：还得用 6.1 的解决方案)](#62-servlet的线程安全可行解决方案结论还得用-61-的解决方案)
  * [7. ServletConfig 对象 - 用于封装 servlet 的配置信息](#7-servletconfig-对象-用于封装-servlet-的配置信息)
  * [8. ServletContext 对象(为整个 web 应用而生)](#8-servletcontext-对象为整个-web-应用而生)
    * [8.1 获取 ServletContext 对象](#81-获取-servletcontext-对象)
    * [8.2 ServletContext 域](#82-servletcontext-域)
    * [8.3 ServletContext 域 - Servlet 转发技术](#83-servletcontext-域-servlet-转发技术)
    * [8.4 ServletContext 域 - 读取 Web 应用资源文件 - .properties 属性文件](#84-servletcontext-域-读取-web-应用资源文件-properties-属性文件)
  * [9. Web 应用中普通 Java 程序如何读取资源文件？ - 通过类装载器](#9-web-应用中普通-java-程序如何读取资源文件-通过类装载器)
    * [9.1 通过类加载器获取更新后的资源](#91-通过类加载器获取更新后的资源)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：April 14, 2018
最后更新日期：April 18, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day05 Servlet 开发和 ServletConfig 与 ServletContext 对象
## 1. Servlet 开发入门 - hello world
Servelet 是动态 web 资源开发技术。html 是静态 web 资源开发技术。Jsp 是另一种动态web资源开发技术，但 jsp 里面就是 Servelet。所以应先搞明白 Servelet。

sun公司提供了一个servlet接口，用户若想开发一个动态web资源，需完整下面2个步骤：
1. 编写一个 java 类，实现 servlet 接口；
2. 把开发好的 java 类部署到 web 服务器中。

快速入门：用servlet向浏览器输出"hello servlet"。
阅读 J2EE 的 servlet api 文档，解决2个问题：
1. 输出 "hello servlet" 的 java 代码应该写在 servlet 的那个方法内？
2. 如何向 IE 浏览器输出数据？

查看 api 后，做实验。
过程如下：
1.在tomcat webapps 中新建 day05 目录， 然后再web应用中建立`WEB-INF/classes`目录；
2.在classes目录中新建一个`FirstServlet.java`；

```java
package cn.wk;

import java.io.*;
import javax.servlet.*;

// GenericServlet已经覆盖了Servlet接口中的方法，继承它，用起来方便
public class FirstServlet extends GenericServlet{
  // 服务器接受客户请求并给出响应，我们需重写 service 方法
	public void service(ServletRequest req,
		ServletResponse res)
	throws ServletException,java.io.IOException{

    // 向浏览器输出的流
		OutputStream out = res.getOutputStream();
    //OutputStream是字节流，故用getBytes()把字符转字节
		out.write("hello servlet!!!".getBytes());
	}
}
```

<font color=red>注意到，servlet 程序是跑在 web 服务器中，受 web 服务器调用的。服务器会给 servlet 程序的`service`方法送来一个客户发来的 request, 向客户发 “hello servelt!!!”响应的话，应由servlet程序中`service`方法中的`ServletResponse`对象去处理。我猜测`OutputStream`输出流由servlet程序发给web服务器，再由web服务器封装后，输出给客户的浏览器。</font>

3.编译servlet程序`FirstServlet.java`。其中需在cmd下将`servlet-api.jar`添加到classpath中。我机器例子：`C:\apache-tomcat-8.5.9\webapps\day05\WEB-INF\classes>set classpath=%classpath%;C:\apache-tomcat-8.5.9\lib\servlet-api.jar`
然后编译：`C:\apache-tomcat-8.5.9\webapps\day05\WEB-INF\classes>javac -d . FirstServlet.java`

4.在WEB-INF目录中新建web.xml文件，并配置servlet的对外访问路径，内容抄自`C:\apache-tomcat-8.5.9\conf\web.xml`文件，并做修改。如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
  http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
  version="3.1">

  <servlet>
    <!-- 名字 -->
    <servlet-name>FirstServlet</servlet-name>
    <!-- 位置 -->
    <servlet-class>cn.wk.FirstServlet</servlet-class>        
  </servlet>

  <!-- 配置servlet的对外访问路径 -->
  <servlet-mapping>
    <!-- 名字 -->
    <servlet-name>FirstServlet</servlet-name![1](/assets/1_8545p1xk4.png)
    <!-- 对外路径 -->
    <url-pattern>/FirstServlet</url-pattern>
  </servlet-mapping>

</web-app>
```

5.启动tomcat,开启浏览器，访问`http://localhost:8080/day05/FirstServlet`查看结果。

## 2. Servlet 的调用过程和生命周期
![1](/assets/1_7ghqddtw8.png)
**生命周期：servlet第一次被访问时被创建一个实例对象，web服务器会调用init方法完成对象初始化，service方法会执行，用来响应客户端的请求，当web服务器关闭时或者当前web应用被删掉时，web服务器会调用destroy方法，从web容器中移除该servlet对象。**

## 3. 使用 Eclipse 开发 Servlet
![2](/assets/2_6ko92cs11.png)
步骤：
1.新建一个 Web Project，不直接点 Finish，点下一步勾选上 web.xml；
2.src目录下新建一个`ServletDemo1`的类并继承`GenericServlet`实现类；
3.把`apache-tomcat-8.5.9-src`源码attached到项目中去，然后在`ServletDemo1`中写入：

```java
public class ServletDemo1 extends GenericServlet {
	@Override
	public void service(ServletRequest req, ServletResponse res)
			throws ServletException, IOException {
		res.getOutputStream().write("hello servlet!!!!!".getBytes());
	}
}
```

4.这个servlet程序外界无法访问，需用`web.xml`配置对外访问路径，添加如下内容：
<font color=red>注意：要想获得这种类名`cn.wk.ServletDemo1`，需将`ServletDemo1.java`点开，然后右键点击类名，再点 copy qualified name 按钮获取类全名！</font>

```xml
<servlet>
	<servlet-name>ServletDemo1</servlet-name>
	<servlet-class>cn.wk.ServletDemo1</servlet-class>
</servlet>

<servlet-mapping>
	<servlet-name>ServletDemo1</servlet-name>
	<url-pattern>/ServletDemo1</url-pattern>
</servlet-mapping>
```

5.想发布这个web应用，需先为Eclipse集成一个tomcat服务器(我用的是 tomcat 8)，如下：
windows->preference->myeclipse->servers->tomcat->tomcat 8.x
然后选择 tomcat 8 所在目录，再点 **Enable**，其他默认，点确定即可。

6.点击屏幕上方的 Deploy MyEclipse J2EE Project to Server 按钮，把本工程部署到服务器；
7.点击屏幕上方的启动服务器按钮(选择tomcat 8.x)；
8.浏览器中输入`http://localhost:8080/day05/ServletDemo1`查看结果。

**实际开发中要想建 servlet 程序，直接右键 new 一个 servlet 即可，Eclipse 直接在 web.xml 中把`<servlet>`元素和`<servlet-mapping>`元素写好了！**

## 4. HttpServlet 和一些开发细节
![3](/assets/3_du71fv705.png)

**写sevlet程序继承`HttpServlet`就行了，再根据想处理的请求复写`doGet()`或者`doPost()`等方法就可以了，不必再复写`service()`方法了,读api看下`HttpServlet`就会完全明白了！**

实验，在day05项目中cn.wk包下直接建立名为`ServletDemo2`的servlet程序，如下：

```java
public class ServletDemo2 extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.getOutputStream().write("Hello, HttpServlet!!!!".getBytes());
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}
}
```

web.xml中对于该资源的外部访问路径就不用配了，Eclipse 已经给咱配好了。
浏览器中输入`http://localhost:8080/day05/servlet/ServletDemo2`查看结果。

**注意：servlet程序重命名后(按F2重命名，而不能在程序中改！)，相关引用该类的程序也自动修改，但web.xml中的名字没改，得手动修改！！！方立勋老师特意强调：写servlet程序要小心，写错名字的话，web.xml中的内容有很多地方需修改，工程很大的话，就是灾难了！**

> 可在MyEclipse目录下查找`Servlet.java`修改模板，使得doGet和doPost方法变清爽，但我没成功。

## 5. Servlet 开发的一些重要细节
拷贝别人的工程后，可能涉及到修改web访问路径。方法：`Eclipse中右击点属性->MyEclipse->找Web->修改Web Context-root`。

配置servlet程序的访问地址URL:
![4](/assets/4_s27qd8q87.png)

一个servlet程序可以有多个URL，还涉及到通配符:
![5](/assets/5_o71u6qdbt.png)

例子，修改day05工程下的 web.xml 如下：

```xml
<!-- servlet注册 -->
	<servlet>
		<servlet-name>ServletDemo1</servlet-name>
		<servlet-class>cn.wk.ServletDemo1</servlet-class>
	</servlet>
	<servlet>
		<servlet-name>ServletDemo2</servlet-name>
		<servlet-class>cn.wk.ServletDemo2</servlet-class>
	</servlet>

	<!-- servlet URL 映射 -->
	<servlet-mapping>
		<servlet-name>ServletDemo1</servlet-name>
		<url-pattern>/ServletDemo1</url-pattern>
	</servlet-mapping>

	<servlet-mapping>
		<servlet-name>ServletDemo2</servlet-name>
		<url-pattern>/servlet/ServletDemo2</url-pattern>
	</servlet-mapping>

	<servlet-mapping>
		<servlet-name>ServletDemo2</servlet-name>
		<url-pattern>/1.html</url-pattern>
	</servlet-mapping>

	<servlet-mapping>
		<servlet-name>ServletDemo2</servlet-name>
		<url-pattern>/*</url-pattern>
	</servlet-mapping>

	<servlet-mapping>
		<servlet-name>ServletDemo2</servlet-name>
		<url-pattern>*.html</url-pattern>
	</servlet-mapping>
```

多个通配符表达的url，涉及到具体匹配哪一个servlet程序的问题(了解):
![6](/assets/6_y9gqd2gb7.png)

Servlet 引擎： Web 服务器中用来调 servlet 程序的那个程序。 Servlet 程序不能单独运行。

servlet程序的init()和destroy():
![7](/assets/7_t8nh5h0id.png)

实验，新创建了一个`ServletDemo3.java`的 servlet 程序，并覆盖了`init()`和`destroy()`。结果显示客户 **第一次访问** 该servlet程序时，web容器执行`init()`，当 **服务器关闭或该servlet程序从web容器被移除** 时，web容器执行该servlet程序的`destroy()`：

```java
public class ServletDemo3 extends HttpServlet {

	@Override
	public void init() throws ServletException {
		super.init();
		System.out.println("init");
	}

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.getOutputStream().write("Hello ServletDemo3!!!".getBytes());
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}

	@Override
	public void destroy() {
		super.destroy();
		System.out.println("destroy");
	}
}
```

为`ServletDemo3`设置启动服务器就创建对象并执行`init()`方法。在 web.xml的`<servlet>`元素里设置`<load-on-startup>`元素，并设置其内容为`1`，如下：

```xml
<servlet>
	<servlet-name>ServletDemo3</servlet-name>
	<servlet-class>cn.wk.ServletDemo3</servlet-class>

	<load-on-startup>1</load-on-startup>
</servlet>
```

**`<load-on-startup>1</load-on-startup>`里的1表示优先级，越小优先级越高，但必须是正整数。**
该技术用在随服务器的启动，启动某些框架上。

**缺省的 Servlet 程序**：

```xml
<servlet-mapping>
  <servlet-name>ServletDemo3</servlet-name>
  <url-pattern>/</url-pattern>
</servlet-mapping>
```

注意上面代码`<url-pattern>/</url-pattern>`中只有`/`,意味着其他servlet都不支持的 url 由这个缺省的`ServletDemo3` servlet程序来处理！即 **处理别人都不处理的请求**！

<font color=red>注意：即使我们没配置该web应用的缺省servlet程序，web容器也会为我们弄一个缺省的servlet程序。如果我们配置了，服务器为我们准备的缺省servlet程序会被覆盖。程序员自己不要把某个servlet弄成缺省的，因为html文件将无法访问。如：`http://localhost:8080/day05/1.html`将访问自己设置的缺省servlet程序。</font>

## 6. Servlet的线程安全
### 6.1 Servlet的线程安全的产生及同步锁解决方案(然并卵方案)
静态成员变量要慎用，可能导致 **线程安全问题** 或 **内存溢出**，如：

```java
public class Person{
  public static List<String> list = new ArrayList<String>();
}
```

若 Person 类随服务器启动而加载，另一个 Demo 类访问 Person 类，当有很多用户用 Demo 类代码访问 Person 类时均向`list`添加数据，静态成员`list`会无限变大，最终可能导致内存溢出，Demo 代码如下：

```java
public class Demo{
  public static void main(String[] args) {
    Person p = new Person();
    p.list.add("aaa");
  }
}
```

下面代码有线程安全问题：

```java
// 线程安全问题
public class ServletDemo4 extends HttpServlet {
	int i = 0;

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		try {
			Thread.sleep(1000 * 3);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		i++;
		response.getOutputStream().write((i + "").getBytes());
	}
}
```

开两个浏览器窗口，同时访问`http://localhost:8080/day05/servlet/ServletDemo4`会出线程安全问题。
加上同步锁，解决了线程安全问题，代码如下：

```java
// 线程安全问题
public class ServletDemo4 extends HttpServlet {
	int i = 0;

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.getOutputStream().write((i + "").getBytes());
		i++;

		try {
			Thread.sleep(1000 * 5);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		response.getOutputStream().write((i + "").getBytes());
	}
}
```

加同步锁解决线程安全问题：

```java
// 加同步锁
public class ServletDemo4 extends HttpServlet {
	int i = 0;

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		synchronized (this) {
			response.getOutputStream().write((i + "").getBytes());
			i++;
			try {
				Thread.sleep(1000 * 5);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			response.getOutputStream().write((i + "").getBytes());
		}
	}
}
```

**以上线程安全问题的解决方案是不行的，最后一个用户访问这个页面等1年？**

### 6.2 Servlet的线程安全可行解决方案(结论：还得用 6.1 的解决方案)
接口中没有任何定义，这种接口是标记接口，如：`Serializable`，`Cloneable`以及本节所涉及的`SingleThreadModel`。
但这试验我没做出来，达不到开2个ie窗口，都显示结果为1的效果，代码如下：

```java
public class ServletDemo4 extends HttpServlet implements SingleThreadModel {
	int i = 0;

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		i++;
		try {
			Thread.sleep(1000 * 8);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		response.getOutputStream().write((i + "").getBytes());
	}
}
```

Java中的谚语：<font color=red>子类在覆盖父类的方法时，不能抛出比父类更多的异常。</font>想法是：子类比父类强。

## 7. ServletConfig 对象 - 用于封装 servlet 的配置信息
Web 服务器会给 Servlet 传各种对象，我们编写的 Servlet 程序接收这些对象后，解析它，再搞对应的操作，如图：
![8](/assets/8_35pf5jstw.png)

认识 ServletConfig 对象：
![9](/assets/9_ewbrmg5o6.png)

**问题：为什么要在 web.xml 这个配置文件里添加 servlet 所需的数据，而不是在 servlet 程序里写入数据？**
实际开发中，有一些东西不适合在 servlet 程序中写死，这类数据就可以通过 **配置的方式** 配给 servlet 程序，例如：
* servlet 采用哪个码表；
* servlet 连接哪个数据库；
* servlet 用哪个配置文件(用 Struts 举的例子)。

举实际的例子，`ServletDemo5`如下：

```java
// ServletConfig 对象：用于封装 servlet 的配置信息
public class ServletDemo5 extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// 得到指定的
		String value = this.getServletConfig().getInitParameter("config");
		System.out.println(value);

		// 得到所有的
		Enumeration e = this.getServletConfig().getInitParameterNames();
		while (e.hasMoreElements()) {
			String name = (String) e.nextElement();
			String value_ = this.getServletConfig().getInitParameter(name);
			System.out.println(name + " = " + value_);
		}
	}
}
```

修改 web.xml，想该 servlet 注册中添加配置数据，如下：

```xml
<servlet>
		<servlet-name>ServletDemo5</servlet-name>
		<servlet-class>cn.wk.ServletDemo5</servlet-class>

		<!-- 配置 ServletConfig -->
		<init-param>
			<param-name>charset</param-name>
			<param-value>UTF-8</param-value>
		</init-param>

		<init-param>
			<!-- 配置数据库连接地址 -->
			<param-name>url</param-name>
			<param-value>jdbc:mysql://localhost:3306/test</param-value>
		</init-param>

		<init-param>
			<param-name>username</param-name>
			<param-value>root</param-value>
		</init-param>

		<init-param>
			<param-name>password</param-name>
			<param-value>root</param-value>
		</init-param>

		<init-param>
			<!-- 本 servlet 读哪个配置文件 -->
			<param-name>config</param-name>
			<param-value>/struts-config.xml</param-value>
		</init-param>

</servlet>
```

浏览器中输入`http://localhost:8080/day05/servlet/ServletDemo5`，则控制台中输出结果为：

```
config = /struts-config.xml
username = root
charset = UTF-8
config = /struts-config.xml
password = root
url = jdbc:mysql://localhost:3306/test
```

## 8. ServletContext 对象(为整个 web 应用而生)
**产生：web 服务器有多少 web 应用，服务器就创建多少个 ServletContext 容器！**
**销毁：停服务器或者删除了某 web 应用，对应的 Context 容器们或容器会被销毁。**

### 8.1 获取 ServletContext 对象
ServletContext 用来操作整个该 servlet 程序所在的 web 应用全局性资源的。
![10](/assets/10_95h9h99qe.png)

获取 ServletContext 对象：

```java
// ServletContext 示例
public class ServletDemo6 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// 获取 ServletContext 对象
		ServletContext context = this.getServletContext();
	}
}
```

### 8.2 ServletContext 域
![11](/assets/11_hova0xjpn.png)

ServletContext 域，表达了以下几点意思：
1. 这是一个容器；
2. ServletContext 域代表这个容器的作用范围时 **整个特定的 web 应用，如day05这个应用**；

下面的例子，**实现了 day05 这个 web 应用范围内的，`ServletDemo7`和`ServletDemo8`这2个servlet程序的数据共享**。

```java
public class ServletDemo7 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String data = "aaa";

		// 向 Context 容器内添加 全web应用域 都能共享的数据
		this.getServletContext().setAttribute("data", data);
	}
}
```

```java
public class ServletDemo8 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// 获取 ServletContext 对象
		ServletContext context = this.getServletContext();
		// 获取 Context 容器内的数据
		String value = (String) context.getAttribute("data");
		// 向浏览器输出
		response.getOutputStream().write(value.getBytes());
	}
}
```

浏览器中输入`http://localhost:8080/day05/servlet/ServletDemo7`，再开一个小窗，地址栏中输入`http://localhost:8080/day05/servlet/ServletDemo8`，在当前的这个浏览器中会出现`ServletDemo7`输出到`ServletContext`域中的共享数据`aaa`。

我们可以在 web.xml 文件中写`<context-param>` **为整个 web 应用做配置**，如下：

```xml
<!-- 为当前整个web应用做的配置 -->
<!-- 所有servlet都可通过ServletContext容器访问下面的数据 -->
<context-param>
  <param-name>data</param-name>
  <param-value>xxxx</param-value>
</context-param>
```

然后建一个servlet程序，输出Context容器中内容即可，`String value = this.getServletContext.getAttribute("data")`，输出这个`value`即可。

**问题：什么情况下，需为整个 web 应用配置初始化参数？**
上百个 servlet 都需连数据库的话，难道上百个servlet配置都用`ServletConfig`来配？这时就得用这个 **代表全局的`ServletContext`容器来配置**。

### 8.3 ServletContext 域 - Servlet 转发技术
**Servlet的转发和重定向**
转发：你向我借钱，我没有，我帮你去找他；
重定向：你向我借钱，我没有，你自己去找他！

**Servlet 只适合产生数据，不适合美化输出，输出得靠html和css。这时就用到转发，既servlet产生的数据转发到 jsp，由 jsp 负责输出数据，这时将大量使用到转发。**

例子，`ServletDemo10`产生的数据转发到`1.jsp`：

```java
// 通过 ServletContext 实现请求转发
public class ServletDemo10 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String data = "aaaaaaaaa";

		// 把数据带给1.jsp(只是演示，正常的话不能用context域，要通过request域)
		this.getServletContext().setAttribute("data", data);

		RequestDispatcher rd = this.getServletContext().getRequestDispatcher("/1.jsp");
		rd.forward(request, response);
	}
}
```

```xml
<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<base href="<%=basePath%>">

<title>My JSP '1.jsp' starting page</title>

<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
<meta http-equiv="description" content="This is my page">
<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

</head>

<body>
	<!-- 这里开始写代码 -->
	<h1>
		<font color="red">
		<%
			String data = (String)application.getAttribute("data");
			out.write(data);
		%>
		</font>
	</h1>
	<!-- 结束 -->
</body>
</html>
```

打开浏览器输入`http://localhost:8080/day05/servlet/ServletDemo10`查看结果。

### 8.4 ServletContext 域 - 读取 Web 应用资源文件 - .properties 属性文件
一般不管理servlet程序，管理的是 web 应用的其他资源文件。

实际应用场景：
众多servlet程序要访问数据库，则一般来说，数据库相关信息要用资源文件保存。
有两种文件用来保存数据库配置信息：
**`.properties`文件(信息无关联用这个)和`.xml`文件(信息有关联用这个)**。
连接数据库的这种信息，认为是平行信息(无关联信息)，故应用`.properties`文件保存。

试验，涉及2文件，`ServletDemo11`和`db.properties`(**该文件在`/src`目录下**)：

`db.properties`内容如下：

```
url=jdbc:mysql://localhost:3306/test
username=root
password=root
```

ServletDemo11内容如下：
注意：
**读取`.properties`文件是重点，且不要用`FileInputStream`对象读，因为它默认的相对路径起始处为 java 虚拟机所在的位置。**

<font color = blue>注意观察路径：`/WEB-INF/classes/db.properties`。
当`ServletDemo11`执行时，工程里的`src/db.properties`文件早已部署到`/WEB-INF/classes/db.properties`了，所以应写这个路径！</font>

```java
// 通过 ServletContext 读取资源文件 方法1
public class ServletDemo11 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// FileInputStream 这么用是不行滴
		// FileInputStream in = new
		// FileInputStream("/WEB-INF/classes/db.properties");
		// 此处最好不要用 FileInputStream 对象，需好用 ServletContext 去读
		InputStream in = this.getServletContext().getResourceAsStream(
				"/WEB-INF/classes/db.properties");

		Properties props = new Properties(); // map
		props.load(in);

		String url = props.getProperty("url");
		String username = props.getProperty("username");
		String password = props.getProperty("password");

		System.out.println(url);
		System.out.println(username);
		System.out.println(password);
	}
}
```

浏览器输入`http://localhost:8080/day05/servlet/ServletDemo11`，则控制台输出结果为：

```
jdbc:mysql://localhost:3306/test
root
root
```

也可以这样读取：

```java
// 通过 ServletContext 读取资源文件 方法2
public class ServletDemo11 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// 获取资源绝对路径后，可用 FileInputStream
		String path = this.getServletContext().getRealPath(
				"/WEB-INF/classes/db.properties");
		// 获取文件名
		String filename = path.substring(path.lastIndexOf("\\") + 1);
		System.out.println("当前读取到的资源名称是： " + filename);

		FileInputStream in = new FileInputStream(path);
		Properties props = new Properties(); // map
		props.load(in);

		String url = props.getProperty("url");
		String username = props.getProperty("username");
		String password = props.getProperty("password");

		System.out.println("当前读取到的资源数据是：");
		System.out.println(url);
		System.out.println(username);
		System.out.println(password);
	}
}
```

## 9. Web 应用中普通 Java 程序如何读取资源文件？ - 通过类装载器
故事：若 servlet 程序想访问数据库，正常情况应通过 dao 层访问，而不是直接访问。而 dao 层的类基本上是普通 java 程序，而不是 servlet 程序。问题是：普通的 java 程序，如何访问当前 web 应用中的某个 web 资源(如：想访问 `src/db.properties`)？

这就要通过类装载器来完成。
**类装载器：当前web应用有一个类装载器，装载了所有当前web应用下的类的字节码文件。可通过该web应用下的任意java程序，获得这个类装载器。通过这个类装载器，找到要访问的资源，获得对应的输入流对象！**

<font color=red>通过类加载器加载的文件，不能太大，否则内存溢出。因为类加载器也要把整个要加载的文件放入内存。</font>

试验，涉及3个文件：要访问的资源`src/db.properties`(与上节内容相同)，`ServletDemo12.java`和一个普通 java 程序`UserDao.java`。

`ServletDemo12.java`如下：

```java
// servlet调用其他普通java程序，这个普通java程序需通过 类加载器 读取web资源文件
public class ServletDemo12 extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		UserDao dao = new UserDao();
		dao.update();
	}
}
```

`UserDao.java`位于`cn.wk.dao`包里，涉及到静态代码块和类加载器，代码如下：

```java
package cn.wk.dao;

import java.io.InputStream;
import java.util.Properties;

public class UserDao {

	private static Properties dbconfig = new Properties();
	// 类加载时 就获得资源
	static {
		try {
			// 类加载器
			InputStream in = UserDao.class.getClassLoader()
					.getResourceAsStream("db.properties");

			dbconfig.load(in);

		} catch (Exception e) {
			// 认为访问不到资源，是重大错误，而不是异常，故抛出错误
			throw new ExceptionInInitializerError(e);
		}
	}

	public void update() {
		System.out.println(dbconfig.getProperty("url")); // map
	}
}
```

浏览器输入`http://localhost:8080/day05/servlet/ServletDemo12`，然后在控制台查看结果。

### 9.1 通过类加载器获取更新后的资源
故事：服务器开启后，当有人修改了`db.properties`资源文件后，再通过类装载器直接获得资源时，无法获得最新的，原因是类装载器里的字节码文件随服务器启动后只加载1次。如下代码：

```java
public class UserDao {
	public void update() throws IOException {

		// 以下代码虽然可以读取资源文件的数据，但无法获取更新后的数据
		Properties dbconfig = new Properties();
		InputStream in = UserDao.class.getClassLoader().getResourceAsStream(
				"db.properties");
		dbconfig.load(in);
		System.out.println(dbconfig.getProperty("url")); // map
	}
}
```

正确姿势：

```java
public class UserDao {
	public void update() throws IOException {

		// 通过类装载的方式得到资源文件的位置，再通过传统方式读取资源文件的数据
		// 这样可以读取资源更新后的数据
		String path = UserDao.class.getClassLoader()
				.getResource("db.properties").getPath();
		FileInputStream in = new FileInputStream(path);
		Properties dbconfig = new Properties();
		dbconfig.load(in);
		System.out.println(dbconfig.getProperty("url")); // map
	}
}
```
