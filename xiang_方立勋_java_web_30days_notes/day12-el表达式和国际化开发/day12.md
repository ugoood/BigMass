
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day12 EL 表达式和国际化开发](#day12-el-表达式和国际化开发)
  * [1. EL(Expression Language) 表达式简介](#1-elexpression-language-表达式简介)
    * [1.1 执行运算](#11-执行运算)
    * [1.2 获取web开发常用对象(el 中定义了11个隐式对象)](#12-获取web开发常用对象el-中定义了11个隐式对象)
    * [1.3 使用 EL 调用 Java 方法](#13-使用-el-调用-java-方法)
    * [1.4 sun 公司 el 函数库 - 处理字符串](#14-sun-公司-el-函数库-处理字符串)
  * [2. 国际化开发](#2-国际化开发)
  * [3. MessageFormat 字符串批量国际化](#3-messageformat-字符串批量国际化)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：May 12, 2018
最后更新日期：May 16, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day12 EL 表达式和国际化开发
建工程day12。
## 1. EL(Expression Language) 表达式简介
作用：
* 获取数据
* 执行运算
* 获取web开发常用对象
* 调用java方法

### 1.1 执行运算
看下面例子即可。

2.jsp 示例代码：

```js
<%
  request.setAttribute("username","aaa");
  request.setAttribute("password","123");
%>

${username=='aaa' && password=='123'}  <%--网页中输出true--%>

<br />-------------empty 运算符----------------<br />
<%
  request.setAttribute("list", null); // 为 null
  // request.setAttribute("list", new ArrayList()); //为 "空"
%>
${empty(list)} <%--很好用！！--%>
<%--上面2中情况都能判断，且返回true，empty通常配合<c:if> jstl标签使用，单独使用则毫无意义--%>

<br />-------------el 支持二元运算符----------------<br />
${user!=null ? user.name:''} <%--很好用！！--%>

<br />--------------二元运算符(数据回显)--------------<br />

<%
  request.setAttribute("gender", "female");
%>

<%-- 点点会自动放在“女”上 --%>
<input type="radio" name="gender" value="male"
  ${gender=='male'?'checked':''}>男
<input type="radio" name="gender" value="female"
  ${gender=='female'?'checked':''}>女

<%
  request.setAttribute("likes", new String[]{"dance", "sing"});
%>
<%-- 此处涉及 el 函数，后面再弄 --%>
<input type="checkbox" name="likes" value="">唱歌
<input type="checkbox" name="likes" value="">跳舞
<input type="checkbox" name="likes" value="">足球
<input type="checkbox" name="likes" value="">篮球
```

### 1.2 获取web开发常用对象(el 中定义了11个隐式对象)
![1](/assets/1_zzh9veabt.png)
![2](/assets/2_l7udjhryr.png)

3.jsp 示例代码：

```js
<head>
  <title>隐式对象</title>
</head>

<body>
  ${pageContext}<br /> <%-- pageContext 是 el 的隐式对象 --%>

  <br />------------使用 el 表达式访问指定的域------------<br />
  <%
    pageContext.setAttribute("aa", "123");

  %>
  ${aa} <br /> <%--从4个域里找 --%>
  ${pageScope.aa} <br /> <%--从指定域里找         拿到pageContext 的 map 集合 --%>

  ${sessionScope.user != null} <br /> <%--应该在session中检测用户是否登录，而不是在4个域里检测--%>

</body>
```

**param 隐式对象(经常被使用)：**

```js
<br />---------获取保存了所有请求参数的 Map 对象---------<br/>
${param.name}
```

上述代码也在 3.jsp 文件中。当我们在浏览器输入`http://localhost:8080/day12/3.jsp?name=aaa`来访问3.jsp时，`${param.name}`将获得参数`name`的值并返回该值的字符串形式。

**param 隐式对象经常用到数据回显**，有下图所示的场景：
![3](/assets/3_0ec4ct5lv.png)

上图中，用户提交的表单在servlet出校验失败后，需跳回到表单页面，`${param.username}`可直接将用户所填的用户名拿到并显示。**即使表单一般是 post 请求**，但也有与之对应的 Request Map 用来存储参数。


**paramValues 隐式对象，可获取多个值**，如下：

```js
<br />---------获取参数的多个值---------<br/>
${paramValues.name[0]}
${paramValues.name[1]}
```

浏览器输入`http://localhost:8080/day12/3.jsp?name=aaa&name=bbb`查看结果。

**header 隐式对象获取请求头的 Map 对象：**

```js
<br />---------获取请求头的 Map 对象---------<br/>
${header.Host} <br />
${header.Cookie} <br />
${header['Accept-Language']} <br />
```

**headerValues 隐式对象获取同名头的多个值，与 paramValues 类似。**

**cookie 隐式对象**
`${cookie.JSESSIONID}`获取的是cookie对象，经查servlet api，发现该对象有针对 name 和 value 的 setter，getter方法。故该对象有 name 属性和 value 属性。

```js
<br />---------获取cookie---------<br/>
${cookie.JSESSIONID.name} <br />
${cookie.JSESSIONID.value}
```

**initParam 隐式对象**
该对象保存了该 web 应用的初始化参数的 map 对象。

如，在 web.xml(`<context-param>`配置整个web应用的初始化参数) 文件中添加：

```xml
<context-param>
  <param-name>xx</param-name>
  <param-value>yyy</param-value>
</context-param>
```

在jsp文件中，我们可用 initParam 隐式对象获取上面配置的初始化参数，如下：

```js
<br />---------获取整个web应用的初始化参数---------<br/>
${initParam.xx} <br />
```

浏览器中输入`http://localhost:8080/day12/3.jsp?name=aaa&name=bbb`查看结果。

### 1.3 使用 EL 调用 Java 方法
用 el 调用 java 方法有两个条件：
1. el 只能调用静态方法；
2. java类的静态方法需在TLD文件中描述。
还包含1步，就是需在 jsp 文件中用 taglib 指令导入标签库。

TLD文件需放置到 WEB-INF 中或该目录下除了 classes 和 lib 目录之外的任意子目录中。
关于TLD文件的编写，如下图：
![4](/assets/4_sz7k2ukyj.png)

完整例子：
先弄个普通java类，并编写一个静态方法，如下 ELDemo.java：

```java
package demo;
public class ELDemo {
	public static String show(String str){
		return str;
	}
}
```

再在 WEB-INF 目录下建个 my.tld 文件(找个别的tld文件，抄头尾)，如下：
修改uri, name, function-class, function-signature即可。

```xml
<?xml version="1.0" encoding="UTF-8"?>

<taglib xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-jsptaglibrary_2_0.xsd"
	version="2.0">
	<description>A tag library exercising SimpleTag handlers.</description>
	<tlib-version>1.0</tlib-version>
	<short-name>SimpleTagLibrary</short-name>
	<uri>/my</uri>

	<function>
		<description>el调java类示例</description>
		<name>show</name>
		<function-class>demo.ELDemo</function-class>
		<function-signature>java.lang.String show( java.lang.String )</function-signature>
	</function>
</taglib>
```

建立 4.jsp，并在文件里用 taglib 指令导入标签库，如下：

```js
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib uri="/my" prefix="my" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>el 调 java 静态方法的示例</title>
  </head>

  <body>
    ${my:show("Hello!!!") }
  </body>
</html>
```

浏览器中输入`http://localhost:8080/day12/4.jsp`查看结果。

### 1.4 sun 公司 el 函数库 - 处理字符串
这么多函数记是记不住的。只记一点：处理字符串，就找 fn.tld 查。

sun公司提供的el函数库，在jstl的 META-INF 文件夹内，找 fn.tld 文件，可查询到。

jsp 页面中，用指令`<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>`导入sun公司自带 el 函数库。

el 函数库：
* `fn:toLowerCase`
* `fn:toUpperCase`
* `fn:trim` 删除首位空格
* `fn:length`函数返回一个 **集合或数组** 大小，或返回一个 **字符串中的字符个数，返回int类型**
* 还有好多，都在下面例子里

例子 5.jsp：

```js
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>sun 公司 el 函数库 - 处理字符串</title>
  </head>

  <body>
    <br />---------- fn:toLowerCase -----------<br />
    ${fn:toLowerCase("AAAA")}

    <br />---------- fn:length -----------<br />

    <% request.setAttribute("arr", new String[5]); %>
    ${fn:length(arr)}

    <%
    	List list = new ArrayList();
    	list.add("aa");
    	list.add("bb");
    	request.setAttribute("list", list);
    %>

   	<c:forEach var="i" begin="0" end="${fn:length(list)}">
   		${list[i]}
   	</c:forEach>

   	<br />---------- fn:split 字符串分割 -----------<br />
   	${fn:split("www.baidu.com",".")[1] }

   	<br />---------- fn:join 字符串连接 -----------<br />
    ${fn:join(fn:split("www,baidu,com",","),".")}

    <br />---------- fn:indexOf 搜索字符串出现的位置 -----------<br />
    ${fn:indexOf("www.baidu.com","du")}

    <br />---------- fn:contains 是否包含某串 -----------<br />
    ${fn:contains("aaabbbccc","bc")}

    <br />---------- 重要的回显例子 -----------<br />
    <%
		request.setAttribute("likes", new String[]{"dance", "sing"});
	%>
	<input type="checkbox" name="likes" value="sing" ${fn:contains(fn:join(likes,","),"sing")?'checked':''}>唱歌
	<input type="checkbox" name="likes" value="dance" ${fn:contains(fn:join(likes,","),"dance")?'checked':''}>跳舞
	<input type="checkbox" name="likes" value="basketball" ${fn:contains(fn:join(likes,","),"basketball")?'checked':''}>篮球
	<input type="checkbox" name="likes" value="football" ${fn:contains(fn:join(likes,","),"football")?'checked':''}>足球

	<br />---------- fn:startsWith 检测以啥开头 -----------<br />
	<br />---------- fn:replace 替换 -----------<br />
	<br />---------- fn:substring 截取子串 -----------<br />
	<br />---------- fn:substringAfter 截 某串第一次出现之后的子串  对应的是fn:substringBefore-----------<br />
	${fn:substringAfter("www.baidu.com",".")} <%-- 返回 baidu.com --%>

	<br />---------- fn:escapeXml 转义-----------<br />
	${fn:escapeXml("<a href=''>点点</a>")}

  </body>
</html>
```

**<font color=red>用户登录回显案例</font>**，如下：

6.jsp:

```js
<%@ page language="java" import="java.util.*, demo.User" pageEncoding="UTF-8"%>
<%@ taglib uri="/my" prefix="my"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>用户登录回显</title>
  </head>

  <body>

  	<%
  		User user = new User();
  		user.setUsername("张三");
  		session.setAttribute("user", user);
  	%>

    ${user!=null?my:add("欢迎您：",user.username):''}

  </body>
</html>
```

javabean 文件，demo.User:

```java
package demo;

public class User {
	private String username;

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}
}
```

包含静态方法的类，用于自定义 el 函数的类，demo.MyEL：

```java
package demo;

public class MyEL {
	public static String add(String str1, String str2) {
		return str1 + str2;
	}
}
```

自定义 el 函数 add 的注册文件，WEB-INF/my.tld 文件：

```xml
<?xml version="1.0" encoding="UTF-8"?>

<taglib xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-jsptaglibrary_2_0.xsd"
	version="2.0">
	<description>A tag library exercising SimpleTag handlers.</description>
	<tlib-version>1.0</tlib-version>
	<short-name>SimpleTagLibrary</short-name>
	<uri>/my</uri>

	<function>
		<description>el调java类示例</description>
		<name>show</name>
		<function-class>demo.ELDemo</function-class>
		<function-signature>java.lang.String show( java.lang.String )</function-signature>
	</function>

	<function>
		<description>连接2个字符串</description>
		<name>add</name>
		<function-class>demo.MyEL</function-class>
		<function-signature>java.lang.String add( java.lang.String, java.lang.String )</function-signature>
	</function>
</taglib>
```

如此，my:add 这个 el 自定义函数(字符串连接功能)就可在6.jsp中正常使用，并实现用户登录回显功能。

## 2. 国际化开发
就是外国人来访问，看到外语页面，中国人来访问，看到中文页面。学国际化开发，是为做框架做准备的。
国际化又称 i18n: internationalization。
![5](/assets/5_gzei1f40k.png)
![6](/assets/6_ftcf39dib.png)
![7](/assets/7_nhfb2al5p.png)
![8](/assets/8_pgr16e03i.png)

实验：

在day02项目中的src目录中建立`cn.wk.resource`资源包。并在包下建立三个资源文件，名字如下：
* `MessageResource_en.properties` 英文资源；
* `MessageResource_zh.properties` 中文资源；
* `MessageResource.properties` 默认资源，注意命名。

三个文件内分别填入(我很懒，写在一个代码片段里了)：

```
username=username
password=password

username=\u7528\u6237\u540D
password=\u5BC6\u7801

username=username
password=password
```

![9](/assets/9_6q8a7ld8h.png)

下面代码将对上面的资源文件做操作，如下：

cn.wk.i18n.Demo1 文件：

```java
package cn.wk.i18n;

import java.util.Locale;
import java.util.ResourceBundle;

public class Demo1 {

	public static void main(String[] args) {
		// 资源包的 base name  "cn.wk.resource.MessageResource"
		ResourceBundle bundler = ResourceBundle.getBundle(
				"cn.wk.resource.MessageResource", Locale.CHINESE);
		String username = bundler.getString("username");
		String password = bundler.getString("password");

		System.out.println(username);
		System.out.println(password);
	}
}
```

页面静态资源国际化的例子 login.jsp：
做本例前，需将资源包中的3个资源文件，添加`submit=submit`，`submit=提交`这样的东西。

```js
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>页面静态数据国际化</title>
  </head>

  <body>

  	<a href="/day12/login.jsp?language=zh">中文</a>
  	<a href="/day12/login.jsp?language=en">English</a>

  	<%
  		String language = request.getParameter("language");
  		if(language==null || language.equals("")){
  			language = "zh";
  		}

  		Locale locale = new Locale(language);  		
  		ResourceBundle bundle = ResourceBundle.getBundle("cn.wk.resource.MessageResource", locale);
  	%>

    <form action="">
    	<%=bundle.getString("username")%>:<input type="text" name="username"><br />
    	<%=bundle.getString("password")%>:<input type="text" name="password"><br />
    	<input type="submit" value=<%=bundle.getString("submit") %>>    	
    </form>

  </body>
</html>
```

![10](/assets/10_7m41d6581.png)
![11](/assets/11_hco5yf35d.png)
![12](/assets/12_0ewwb3v5k.png)
![13](/assets/13_10tmz320c.png)

例子1： 使用 DateFormat 格式化输出 日期 时间

```java
package demo;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class Demo2 {
	/**
	 * 使用 DateFormat 格式化输出 日期 时间
	 * */
	public static void main(String[] args) {
		Date date = new Date();
		DateFormat df = DateFormat.getDateInstance(DateFormat.FULL,
				Locale.CHINA);
		String str = df.format(date); // 2018年5月16日 星期三
		System.out.println(str);

		df = DateFormat.getDateTimeInstance(DateFormat.FULL, DateFormat.FULL,
				Locale.CHINA);
		str = df.format(date); // 2018年5月16日 星期三 下午09时33分01秒 CST
		System.out.println(str);

		// 默认的 DateFormat 格式化输出器
		df = DateFormat.getInstance();
		System.out.println(df.format(date)); // 18-5-16 下午9:34
	}
}
```

例子2： 使用 DateFormat 反向把一个字符串格式化成一个日期对象

```java
package demo;

import java.text.DateFormat;
import java.text.ParseException;
import java.util.Date;
import java.util.Locale;

public class Demo3 {
	/**
	 * 使用 DateFormat 反向把一个字符串格式化成一个日期对象
	 * @throws ParseException
	 * */

	public static void main(String[] args) throws ParseException {

		String str = "2018年5月16日 星期三 下午09时33分01秒 CST";

		// 根据字符串日期 定 short medium long full 和 Locale
		DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
				DateFormat.FULL, Locale.CHINA);
		Date date = df.parse(str);
		System.out.println(date); // Wed May 16 21:33:01 CST 2018
	}
}
```

![14](/assets/14_3kpbp6ur5.png)
![15](/assets/15_i3uhifli5.png)

例子3：

```java
package demo;

import java.text.NumberFormat;
import java.text.ParseException;
import java.util.Locale;

public class Demo4 {

	// NumberfFormat 数字，货币转换
	public static void main(String[] args) throws ParseException {
		// 数字转货币
		int price = 18;  // $18.00 ￥18.00 18,00 €
		NumberFormat nf = NumberFormat.getCurrencyInstance(Locale.FRANCE);
		System.out.println(nf.format(price));

		// 货币转数字
		String s = "￥18.00";
		nf = NumberFormat.getCurrencyInstance(Locale.CHINA);
		double num = nf.parse(s).doubleValue();
		System.out.println(num);

		// 百分比
		double d = 0.1;
		nf = NumberFormat.getPercentInstance();
		System.out.println(nf.format(d)); // 10%
	}
}
```

## 3. MessageFormat 字符串批量国际化

![16](/assets/16_jancxvs3b.png)
![17](/assets/17_ex61a4jkr.png)
![18](/assets/18_42bt8w2fs.png)
![19](/assets/19_j25g58pdc.png)

例子, 注意字符串中格式控制的这种东西`{0, time, short}`：

```java
package demo;

import java.text.MessageFormat;
import java.util.Date;
import java.util.Locale;

public class Demo5 {
	public static void main(String[] args) {

		String pattern = "At {0, time, short} on {0, date}, a hurricance destroyed {1} houses and caused {2, number, currency} of damage.";
		MessageFormat format = new MessageFormat(pattern, Locale.CHINA);
		Object params[] = { new Date(), 99, 100000 };
		String message = format.format(params);
		System.out.println(message);
	}
}
```
