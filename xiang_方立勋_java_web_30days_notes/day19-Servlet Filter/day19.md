
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day19 Servlet Filter](#day19-servlet-filter)
  * [1. filter 入门与案例](#1-filter-入门与案例)
  * [2. Filter 案例](#2-filter-案例)
    * [2.1 filter 解决乱码问题](#21-filter-解决乱码问题)
    * [2.2 filter 控制不缓存 jsp 文件](#22-filter-控制不缓存-jsp-文件)
    * [2.3 filter 控制缓存某些文件](#23-filter-控制缓存某些文件)
    * [2.4 filter 实现用户自动登陆](#24-filter-实现用户自动登陆)
  * [3. filter 映射细节](#3-filter-映射细节)
  * [4. 增强request - 完全解决乱码问题的 filter](#4-增强request-完全解决乱码问题的-filter)
  * [5. 未学习部分](#5-未学习部分)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：June 17, 2018
最后更新日期：June 18, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day19 Servlet Filter
建立 day19 web工程。
## 1. filter 入门与案例
Filter 简介：
Filter也称之为过滤器，它是Servlet技术中最激动人心的技术，WEB开发人员通过Filter技术，对web服务器管理的所有web资源：例如Jsp, Servlet, 静态图片文件或静态 html 文件等进行拦截，从而实现一些特殊的功能。例如实现URL级别的权限访问控制、过滤敏感词汇、压缩响应信息等一些高级功能。
Servlet API中提供了一个Filter接口，开发web应用时，如果编写的Java类实现了这个接口，则把这个java类称之为过滤器Filter。通过Filter技术，开发人员可以实现用户在访问某个目标资源之前，对访问的请求和响应进行拦截，如下所示：
![1](/assets/1_oyvtpchth.png)

入门例子：
需求：拦截index.jsp

1.建立`cn.wk.web.filter.FilterDemo1`拦截器：

```java
public class FilterDemo1 implements Filter {

	public void doFilter(ServletRequest request, ServletResponse response,
			FilterChain chain) throws IOException, ServletException {
		System.out.println("haha!!!");
		chain.doFilter(request, response); // 放行
		System.out.println("wowo!!!");
	}

	public void init(FilterConfig filterconfig) throws ServletException {}
	public void destroy() {}
}
```

2.在 web.xml 中配置拦截器：

```xml
<filter>
  <filter-name>FilterDemo1</filter-name>
  <filter-class>cn.wk.web.filter.FilterDemo1</filter-class>
</filter>

<filter-mapping>
  <filter-name>FilterDemo1</filter-name>
  <url-pattern>/index.jsp</url-pattern>
</filter-mapping>
```

3.index.jsp：

```xml
<head>
  <title>Filter入门</title>
</head>

<body>
  <% System.out.println("index!!!"); %>
</body>
```

控制台输出结果为：

```
haha!!!
index!!!
wowo!!!
```

观察结果，了解到：
`web 浏览器 -> web 服务器 -> filter -> index.jsp -> filter -> web 服务器 -> web 浏览器`

filter在开发中的常见应用：
1. filter可以目标资源执行之前，进行权限检查，检查用户有无权限，如有权限则放行，如没有，则拒绝访问；
2. filter可以放行之前，对request和response进行预处理，从而实现一些全局性的设置；
3. filter在放行之后，可以捕获到目标资源的输出，从而对输出作出类似于压缩这样的设置。

**解决乱码问题：**
弄一个filter拦截所有资源：

```xml
<filter>
  <filter-name>FilterDemo1</filter-name>
  <filter-class>cn.wk.web.filter.FilterDemo1</filter-class>
</filter>
<filter-mapping>
  <filter-name>FilterDemo1</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

在FilterDemo1这个filter里写：

```java
public void doFilter(ServletRequest request, ServletResponse response,
    FilterChain chain) throws IOException, ServletException {

  request.setCharacterEncoding("UTF-8");
  response.setCharacterEncoding("UTF-8");
  response.setContentType("text/html;charset=UTF-8");
  chain.doFilter(request, response); // 放行
}
```

这样，所有资源全UTF-8编码，彻底解决乱码问题。

**Filter 链：**
多个filter组成链，顺序由 web.xml 文件中 filter-mapping 的顺序来决定，如下：

filter-mapping 顺序为：

```xml
<filter-mapping>
  <filter-name>FilterDemo1</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>

<filter-mapping>
  <filter-name>FilterDemo2</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

结果为(即filter链里的filter顺序为先 filter1 后 filter2)：

```
filterdemo1之前!!!
filterdemo2之前!!!
index!!!
filterdemo2之后!!!
filterdemo1之后!!!
```

Filter 的生命周期：
filter 的生命周期和 web 应用是一样的。
一个拦截器，服务器中只有1个拦截器对象。不同拦截器有与之对应的不同的拦截器对象。

注意到`public void init(FilterConfig filterconfig) {}`中的`FilterConfig`对象，这是初始化filter的一个对象。这个对象在web.xml中配置。当filter初始化时，web.xml中相应的配置会被自动读取。如下：

```xml
<filter>
  <filter-name>FilterDemo1</filter-name>
  <filter-class>cn.wk.web.filter.FilterDemo1</filter-class>
  <init-param>
    <param-name>xxx</param-name>
    <param-value>yyy</param-value>
  </init-param>
</filter>
```

程序中输出初始化参数：

```java
public void init(FilterConfig filterconfig) throws ServletException {
  String value = filterconfig.getInitParameter("xxx");
  System.out.println(value);
}
```

当服务器启动时，初始化该过滤器同时打印`yyy`。有些内容不想在程序中固定，就可通过这种配置的方式设置。

有时我们想在 doFilter 方法中使用初始化参数，做法是：
1. 在`FilterDemo1`中定义成员变量`private FilterConfig config;`
2. 在 doFilter() 方法中写入`String value = this.config.getInitParameter("xxx");`获得参数值。

## 2. Filter 案例

### 2.1 filter 解决乱码问题

```java
package cn.wk.web.filter.example;
public class CharacterEncodingFilter implements Filter {

	private FilterConfig config;
	private String defaultCharset = "UTF-8"; // <- 默认

	public void doFilter(ServletRequest req, ServletResponse resp,
			FilterChain chain) throws IOException, ServletException {

		// 获取要设置的字符集
		String charset = this.config.getInitParameter("charset");
		if (charset == null)
			charset = defaultCharset;

		HttpServletRequest request = (HttpServletRequest) req;
		HttpServletResponse response = (HttpServletResponse) resp;

		request.setCharacterEncoding(charset);
		response.setCharacterEncoding(charset);
		response.setContentType("text/html;charset" + charset);

		chain.doFilter(request, response);
	}

	public void destroy() {}
	public void init(FilterConfig arg0) throws ServletException {}
}
```

web.xml配置，还配置了初始化参数charset，如下：

```xml
<filter>
  <filter-name>CharacterEncodingFilter</filter-name>
  <filter-class>cn.wk.web.filter.example.CharacterEncodingFilter</filter-class>
  <init-param>
    <param-name>charset</param-name>  <!--charset 设置-->
    <param-value>UTF-8</param-value>
  </init-param>
</filter>

<filter-mapping>
  <filter-name>CharacterEncodingFilter</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

这样，该 web 应用以后不用再考虑乱码问题，且可在 web.xml 文件中的过滤器中灵活设置 charset。

### 2.2 filter 控制不缓存 jsp 文件
常见应用2，故事：
由于 jsp 显示内容来源于 servlet，内容是动态的，所以缓存 jsp 文件没意义。所以，现在要做一个不缓存jsp文件的过滤器。

**控制不缓存的过滤器：**

```java
public void doFilter(ServletRequest req, ServletResponse resp,
    FilterChain chain) throws IOException, ServletException {

  HttpServletRequest request = (HttpServletRequest) req;
  HttpServletResponse response = (HttpServletResponse) resp;

  // 设定3头，不留缓存
  response.setDateHeader("Expires", -1);
  response.setHeader("Cache-Control", "no-cache");
  response.setHeader("Pragma", "no-cache");

  chain.doFilter(request, response);
}
```

web.xml中cache-mapping的配置：

```xml
<filter-mapping>
  <filter-name>NoCacheFilter</filter-name>
  <url-pattern>*.jsp</url-pattern>
</filter-mapping>
```

### 2.3 filter 控制缓存某些文件

常见应用3：控制浏览器缓存页面中的静态资源的过滤器
场景：有些动态页面中引用了一些图片或css文件以修饰页面效果，这些图片和css文件经常是不变化的，所以为减轻服务器的压力，可以使用 filter 控制浏览器缓存这些文件，以提升服务器的性能。

灵活的过滤器：

```xml
<filter>
  <filter-name>CacheFilter</filter-name>
  <filter-class>cn.wk.web.filter.example.CacheFilter</filter-class>
  <init-param>
    <param-name>css</param-name>
    <param-value>10</param-value> <!--css 缓存10分钟-->
  </init-param>
  <init-param>
    <param-name>jpg</param-name>
    <param-value>1</param-value> <!--jpg 缓存1分钟-->
  </init-param>
  <init-param>
    <param-name>js</param-name>
    <param-value>20</param-value> <!--js 缓存1分钟-->
  </init-param>
</filter>

<!--同一个 filter，三种 mapping-->

<filter-mapping>
  <filter-name>CacheFilter</filter-name>
  <url-pattern>*.jpg</url-pattern>
</filter-mapping>

<filter-mapping>
  <filter-name>CacheFilter</filter-name>
  <url-pattern>*.css</url-pattern>
</filter-mapping>

<filter-mapping>
  <filter-name>CacheFilter</filter-name>
  <url-pattern>*.js</url-pattern>
</filter-mapping>
```

`cn.wk.web.filter.example.CacheFilter`代码：

```java
// 控制浏览器缓存的过滤器
public class CacheFilter implements Filter {

	private FilterConfig config;

	public void doFilter(ServletRequest req, ServletResponse resp,
			FilterChain chain) throws IOException, ServletException {

		HttpServletRequest request = (HttpServletRequest) req;
		HttpServletResponse response = (HttpServletResponse) resp;

		// 1. 获取用户想访问的资源
		String uri = request.getRequestURI();

		// 2. 获取该资源的缓存时间
		int expires = 0;
		if (uri.endsWith(".jpg")) {
			expires = Integer.parseInt(this.config.getInitParameter("jpg"));
		} else if (uri.endsWith(".js")) {
			expires = Integer.parseInt(this.config.getInitParameter("js"));
		} else {
			expires = Integer.parseInt(this.config.getInitParameter("css"));
		}

		response.setDateHeader("expires", System.currentTimeMillis() + expires
				* 60 * 1000);

		chain.doFilter(request, response);
	}

	public void init(FilterConfig filterconfig) throws ServletException {
		this.config = filterconfig;
	}
	public void destroy() {}
}
```

### 2.4 filter 实现用户自动登陆
略
## 3. filter 映射细节

<filter-mapping>元素用于设置一个 Filter 所负责拦截的资源。
一个Filter拦截的资源可通过两种方式来指定：**Servlet 名称** 和 **资源访问的请求路径**。
* <filter-name>子元素用于设置filter的注册名称。该值必须是在<filter>元素中声明过的过滤器的名字
* <url-pattern>设置 filter 所拦截的请求路径(过滤器关联的URL样式)
* <servlet-name>指定过滤器所拦截的Servlet名称。

<dispatcher>指定过滤器所拦截的资源被 Servlet 容器调用的方式，可以是 **REQUEST,INCLUDE,FORWARD和ERROR之一**，默认REQUEST。用户可以设置多个<dispatcher> 子元素用来指定 Filter 对资源的多种调用方式进行拦截。

一个资源被调用的方式共有四种：**REQUEST, INCLUDE, FORWARD 和 ERROR。**

例子，如图：
![2](/assets/2_m6gla0hok.png)
**上图中表示：servlet forward(request, response) 到一个jsp页面。此时，若做对jsp拦截器，控制缓存的话，就需在拦截器中设置`<dispatcher>FORWARD</dispatcher>`，才能触发这个拦截器。**

部署案例：

```xml
<filter-mapping>
  <filter-name>testFilter</filter-name>
  <url-pattern>/test.jsp</url-pattern>
</filter-mapping>

<filter-mapping>
  <filter-name>testFilter</filter-name>
  <url-pattern>/index.jsp</url-pattern>
  <dispatcher>REQUEST</dispatcher>
  <dispatcher>FORWARD</dispatcher>
</filter-mapping>
```

## 4. 增强request - 完全解决乱码问题的 filter
下面代码解决了包括post和get请求在内的所有乱码问题。
* **用到了包装模式增强了 request；**
* **用到了 sun 提供的`HttpServletRequestWrapper`包装类，避免自己一个个覆盖不想增强的方法！**

**<font color=blue>注意：`request.setCharacterEncoding("UTF-8");`只解决 post，不能解决 get 乱码问题。
本案例通过重写 getParameter() 方法，调整获得值得编码从 iso8859-1 到 request.getCharacterEncoding() 方法所指定的编码方式完成 get 请求方式下的乱码解决问题。</font>**

```java
//真正解决全站乱码
public class CharacterEncodingFilter2 implements Filter {  	
	public void doFilter(ServletRequest req, ServletResponse resp,
			FilterChain chain) throws IOException, ServletException {

		HttpServletRequest request = (HttpServletRequest) req;
		HttpServletResponse response = (HttpServletResponse) resp;

		request.setCharacterEncoding("UTF-8");  // 只解决 post，不能解决 get
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");

		chain.doFilter(new MyRequest(request), response);   //request.getparameter("password");
	}

	/*
	1.写一个类，实现与被增强对象相同的接口
	2.定义一个变量，记住被增强对象
	3.定义一个构造方法，接收被增强对象
	4.覆盖想增强的方法
	5.对于不想增强的方法，直接调用被增强对象（目标对象）的方法
	 */

	class MyRequest extends HttpServletRequestWrapper{

		private HttpServletRequest request;
		public MyRequest(HttpServletRequest request) {
			super(request);
			this.request = request;
    }

		public String getParameter(String name) {			
			String value = this.request.getParameter(name);
			if(!request.getMethod().equalsIgnoreCase("get")) {return value;}

			if(value==null){return null;}

			try {
				return value = new String(value.getBytes("iso8859-1"),
						request.getCharacterEncoding());
			} catch (UnsupportedEncodingException e) {
				throw new RuntimeException(e);}}}

	public void destroy() {}
	public void init(FilterConfig filterConfig) throws ServletException {}
}
```

不要忘记在 web.xml 中配置这个过滤器，配置方法略。

## 5. 未学习部分
![3](/assets/3_mx0u4eblm.png)
以后再说。
