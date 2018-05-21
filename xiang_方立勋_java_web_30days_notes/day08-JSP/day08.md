
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day08 JSP](#day08-jsp)
  * [1. jsp 入门和 jsp 运行原理](#1-jsp-入门和-jsp-运行原理)
  * [2. jsp 语法](#2-jsp-语法)
    * [2.1 jsp 模板元素：jsp 页面中的 html 内容。它定义了网络基本骨架，即定义了页面结构和外观。](#21-jsp-模板元素jsp-页面中的-html-内容-它定义了网络基本骨架即定义了页面结构和外观)
    * [2.2 jsp 脚本表达式：<%= %>，作用是用于向浏览器输出数据。](#22-jsp-脚本表达式-作用是用于向浏览器输出数据)
    * [2.3 jsp 脚本片段：](#23-jsp-脚本片段)
    * [2.4 jsp 声明](#24-jsp-声明)
    * [2.5 jsp 注释](#25-jsp-注释)
    * [2.6 jsp 指令](#26-jsp-指令)
    * [2.7 jsp 的乱码问题解决](#27-jsp-的乱码问题解决)
    * [2.8 jsp 语法 - include 指令](#28-jsp-语法-include-指令)
  * [3. jsp 九大隐式对象简介](#3-jsp-九大隐式对象简介)
    * [3.1 jsp 九大隐式对象 - out 对象](#31-jsp-九大隐式对象-out-对象)
    * [3.2 jsp 九大隐式对象 - pageContext 对象(jsp 中最重要的对象，代表 jsp 页面的运行环境)](#32-jsp-九大隐式对象-pagecontext-对象jsp-中最重要的对象代表-jsp-页面的运行环境)
  * [4. jsp 常用标签](#4-jsp-常用标签)
  * [5. jsp 映射](#5-jsp-映射)
  * [6. 页面美化专题-div和css基础及案例](#6-页面美化专题-div和css基础及案例)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：April 26, 2018
最后更新日期：May 1, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day08 JSP
## 1. jsp 入门和 jsp 运行原理
![1](/assets/1_43kiib219.png)

案例：新建 day08 web 工程，建立 1.jsp 文件，代码如下：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>jsp入门(输出时间)</title>
  </head>

  <body>
   	 当前时间值是：
    <%
    	Date date = new Date();
    	out.write(date.toLocaleString());
    %>

  </body>
</html>
```

浏览器输入`http://localhost:8080/day08/1.jsp`，查看结果。输出的网页源码为：

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>jsp入门(输出时间)</title>
  </head>

  <body>
   	 当前时间值是：
    2018-4-27 11:44:50

  </body>
</html>
```

看下面内容，找原因，为啥网页变成上面那样。

查看`C:\apache-tomcat-8.5.9\work\Catalina\localhost\day08\org\apache\jsp\_1_jsp.java`的代码片段：

```java
public final class _1_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

    ...

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;

      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\r\n");
      out.write("<html>\r\n");
      out.write("  <head>\r\n");
      out.write("    <title>jsp入门(输出时间)</title>\t\r\n");
      out.write("  </head>\r\n");
      out.write("  \r\n");
      out.write("  <body>\r\n");
      out.write("   \t 当前时间值是：\r\n");
      out.write("    ");

    	Date date = new Date();
    	out.write(date.toLocaleString());

      out.write("\r\n");
      out.write("    \r\n");
      out.write("  </body>\r\n");
      out.write("</html>\r\n");

      ···
```

从上面例子看出，jsp 文件被 tomcat 翻译成了 servlet 程序。
人们长时间实践结果总结出的 servlet 和 jsp 的最佳实践是：servlet 写逻辑，产生数据；jsp 做数据展示。

通过上面的代码，看到jsp常用的对象有：
* request
* response
* session
* application
* page

## 2. jsp 语法
简单、枯燥但有效！
* jsp 模板元素
* jsp 脚本表达式
* jsp 脚本片段
* jsp 注释
* jsp 指令
* jsp 标签
* jsp 内置对象
* 如何查找 jsp 页面中的错误

### 2.1 jsp 模板元素：jsp 页面中的 html 内容。它定义了网络基本骨架，即定义了页面结构和外观。
### 2.2 jsp 脚本表达式：<%= %>，作用是用于向浏览器输出数据。
![2](/assets/2_qgtnpsai5.png)

示例如下：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>jsp入门(输出时间)</title>
  </head>

  <body>
   	 当前时间值是：
    <%
    	Date date = new Date();
    	String time = date.toLocaleString();
    	/* out.write(date.toLocaleString()); 2种输出方式*/
    %>
    <%=time %>

  </body>
</html>
```

### 2.3 jsp 脚本片段：
![3](/assets/3_pch3vhk5w.png)
![4](/assets/4_u89dl4ih3.png)

```html
<%int x=10; %>
aaa
<%out.print(x); %>
```

之所以能相互访问，是因为它们都在同一个 servlet 程序的 service 方法里。

![5](/assets/5_55bflumdl.png)

### 2.4 jsp 声明
![6](/assets/6_r8bwhdu2e.png)

```html
<%
  // 这是不行的
  public void run(){
  }
%>
```

```html
<%！
  // 这个就可以
  public void run(){

  }
%>
```

上面的 jsp 声明，将翻译到 servlet 外面去，成为独立的方法。jsp 声明中可以写静态代码块。

### 2.5 jsp 注释
`<%-- jsp 注释--%>`
而这个`<!-- html 注释 -->`。若在 jsp 片段中用了 html 注释，这个注释内容会传给浏览器，即使浏览器不显示。

### 2.6 jsp 指令
![7](/assets/7_fjyrst7fv.png)
![8](/assets/8_9sjzoc35p.png)
![9](/assets/9_93qjv59ix.png)
![10](/assets/10_29fpbtw0y.png)
![11](/assets/11_i6zx3umds.png)

关于 errorPage 属性，jsp 出异常时，跳转到errorPage所指示的位置。如下：

抛异常的页面 `/5.jsp`：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" errorPage="/errors/error.jsp"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>errorPage属性展示</title>
  </head>

  <body>
    <%
    	int x = 1/0;    	
    %>
  </body>
</html>
```

出错致歉页面`/errors/error.jsp`：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>    
    <title>My JSP 'error.jsp' starting page</title>
  </head>

  <body>
   	 对不起，出错了 <br>
  </body>
</html>
```

浏览器访问`http://localhost:8080/day08/5.jsp` 查看结果。

<font color = red>我们还可通过 web.xml 对整个 web 应用的错误处理做 **全局的配置！** 配置如下：</font>

web.xml 添加内容如下：

```xml
<error-page>
  <exception-type>java.lang.ArithmeticException</exception-type>
  <location>/errors/error.jsp</location>
</error-page>

<error-page>
  <exception-code>404</exception-code>
  <location>/errors/404.jsp</location>
</error-page>

<error-page>
  <exception-code>500</exception-code>
  <location>/errors/500.jsp</location>
</error-page>
```

上面代码还给出了 404 错误码的展示页面。 出500错误时，输出“对不起，服务器内部出错”。

**<font color = red>网站开发结束，上线部署时，这些东西一定要配上。</font>**

**方立勋老师提示，此时 error.jsp 页面大小不要超过1KB，否则不会出现实验效果。**

另外 errorPage 优先级高于 web.xml 中的错误处理。

**<font color = red>`isErrorPage="true|false"` ：默认为false。 若某 jsp 页面为错误处理页面，应设置这个属性为 true。此时，异常对象会传给该错误处理页面，随后该页面可将异常记录在 log 中。</font>**

![12](/assets/12_dh254mibv.png)

### 2.7 jsp 的乱码问题解决
Tomcat 6 以上的服务器，jsp 中不会出现乱码问题。

### 2.8 jsp 语法 - include 指令
包含，分静态包含和动态包含2种。

静态包含，又叫编译时包含，它包含的所有jsp会编译成1个servlet

涉及3个jsp文件：6.jsp，head.jsp，foot.jsp，代码如下：

6.jsp：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>jsp包含</title>
  </head>

  <body>
	<%@ include file="/public/head.jsp" %>
	aaaaaaaaaa<br/>
	<%@ include file="/public/foot.jsp" %>    
  </body>
</html>
```

/public/head.jsp：

```html
<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
    我是 head <br/>
```

/public/foot.jsp：

```html
<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
    我是 foot <br/>
```

动态包含，也称运行时包含。包含的内容被编译成3个jsp文件。

```html
<body>
<% request.getRequestDispatcher("/public/head.jsp").include(request, response); %>
<% response.getWriter().write("aaaaaaaaaaaaa<br/>"); %>
<% request.getRequestDispatcher("/public/foot.jsp").include(request, response); %>  
</body>
```

## 3. jsp 九大隐式对象简介
jsp 九大隐式对象：
* request
* response
* session
* application
* config
* page
* exception
* out
* pageContext

out 和 pageContext 是 jsp 独有的对象。

### 3.1 jsp 九大隐式对象 - out 对象
例子：
8.jsp:

```html
<body>
<%
  out.write("hahahahaha");
  response.getWriter().write("woowowowowo");
%>
</body>
```

和

```html
<body>
hahahahaha
<%
  response.getWriter().write("woowowowowo");
%>
</body>
```

输出均为：`woowowowowo hahahahaha`。建议用jsp输出只用 out 对象。输出那结果的原因就是 out 带缓冲。

### 3.2 jsp 九大隐式对象 - pageContext 对象(jsp 中最重要的对象，代表 jsp 页面的运行环境)
![13](/assets/13_lrbod276l.png)
![14](/assets/14_s7qpv7nl9.png)

pageContext(又称 page 域)域只在当前 jsp 页面有效，它是 web 开发中 4 个域(其他3个：request(请求范围可用), session(会话范围可用), ServletContext(web 应用程序范围内都可用))中，范围最小的域。
> 查看 Jsp API

pageContext 对象的方法：
* setAttribute(String name, Object value)
* getAttribute(String name)
* removeAttribute(String name)

pageContext 访问其他域的方法：
* setAttribute(String name, int scope)
* getAttribute(String name, int scope)
* removeAttribute(String name, int scope)

代表各个域的常量：
* PageContext.APPLICATION_SCOPE
* PageContext.SESSION_SCOPE
* PageContext.REQUEST_SCOPE
* PageContext.PAGE_SCOPE

**<font color=red>findAttribute 方法，重点，查找各个域中的属性。</font>**

```java
pageContext.findAttribute("data");
```

**<font color=red>findAttribute() 依次查找 `page -> request -> session -> application` 这4个域，若找不到，返回`null`。</font>**
**<font color=red>EL表达式`${data}`就相当于执行了`pageContext.findAttribute("data");`</font>**



例子：
pageContext 对象成为管理其他域的入口。12.jsp，如下：

```html
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>pageContext 对象访问其他域</title>
  </head>

  <body>
	<%
		request.setAttribute("data", "aaa");
		/* pageContext 对象成为管理其他域的入口 */
		String data = (String)PageContext.getAttribute("data", pageContext.REQUEST_SCOPE);
		out.write(data);
	%>    
  </body>
</html>
```

pageContext 其他常用发法：forward 和 include，如下：

```html
<%
  pageContext.forward("1.jsp");
  pageContext.include("/foot.jsp");  
%>
```

## 4. jsp 常用标签
Jsp 标签(Jsp Action)：也叫 jsp 动作元素，它用于在 jsp 页面中提供业务逻辑功能，避免在 jsp 页面中直接编写 java 代码(造成 jsp 页面难以维护)。

jsp 常用标签包括：
* `<jsp:forward>`
* `<jsp:include>` 动态包含
* `<jsp:param>` 带数据给别人

关于 `<jsp:forward>` 和 `<jsp:include>` 的例子，14.jsp：

```html
<body>
    <jsp:forward page="/index.jsp"></jsp:forward>
    <jsp:include page="/public/foot.jsp"></jsp:include> <%-- 动态包含 --%>
</body>
```

<jsp:param> 用来带数据给别人，例如：

```html
<body>
    <jsp:forward page="/servlet/ServletDemo1">
      <jsp:param value="xxxx" name="username"/>
    </jsp:forward>
</body>
```

cn.wk.web.servlet.ServletDemo1 获取传来的数据，代码如下：

```java
public class ServletDemo1 extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {

		String username = req.getParameter("username");
		System.out.println(username);
	}
}
```

浏览器访问 14.jsp，控制台输出`xxxx`。

另外，value 中也可传入脚本表达式，如下：

```html
<% int x = 10 %>
<jsp:param name="abc" value="<%=x%>"/>
```

## 5. jsp 映射
jsp 映射：就是把1个 jsp 映射到一个 web 地址上去。它和 servlet 程序映射是同样道理。需在 web.xml 文件中配置。

如下：

```xml
<servlet>
  <servlet-name>xxx</servlet-name>
  <jsp-file>/14.jsp</jsp-file>
</servlet>

<servlet-mapping>
  <servlet-name>xxx</servlet-name>
  <url-pattern>/15.html</url-pattern>
</servlet-mapping>
```

## 6. 页面美化专题-div和css基础及案例
用到再学
