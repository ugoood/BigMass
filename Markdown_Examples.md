
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Markdown示例](#markdown示例)
* [1、段落](#1-段落)
  * [1.1、段落标题](#11-段落标题)
* [一级标题](#一级标题)
  * [二级标题](#二级标题)
    * [三级标题](#三级标题)
  * [1.2、加粗、斜体](#12-加粗-斜体)
  * [1.3、列表](#13-列表)
    * [1.3.1 无序列表示例：](#131-无序列表示例)
    * [1.3.2 有序列表示例：](#132-有序列表示例)
    * [1.3.3 多级列表示例](#133-多级列表示例)
    * [1.3.4 列表项目有多个段落](#134-列表项目有多个段落)
  * [1.4、区块引用](#14-区块引用)
    * [1.4.1 普通区块](#141-普通区块)
    * [1.4.2 嵌套区块](#142-嵌套区块)
  * [1.5、链接、图片](#15-链接-图片)
    * [1.5.1 链接](#151-链接)
    * [1.5.2 图片](#152-图片)
* [2、代码](#2-代码)
  * [2.1、关键词](#21-关键词)
  * [2.2、代码段](#22-代码段)
* [3、表格等复杂情况](#3-表格等复杂情况)
* [4、其他](#4-其他)
  * [4.1  表格](#41-表格)
    * [4.2 字体、字号、颜色](#42-字体-字号-颜色)
* [5. Reference](#5-reference)
* [Other Confusion Materals](#other-confusion-materals)
  * [1.markdown相关材料](#1markdown相关材料)
  * [2.markdown画图Demo](#2markdown画图demo)
  * [3.markdown公式编辑](#3markdown公式编辑)
  * [4.引用](#4引用)
  * [6.ToPDF](#6topdf)
  * [7.TOC](#7toc)

<!-- tocstop -->


Markdown示例
==========
# 1、段落
## 1.1、段落标题

根据原文中的文档标题可以对应设置标题。

# 一级标题
## 二级标题
### 三级标题

## 1.2、加粗、斜体

*单星号* => 单星号
_单下划线_ => 单下划线
**双星号** => 双星号
__双下划线__ => 双下划线

## 1.3、列表

### 1.3.1 无序列表示例：

* item1
* item2
* item3


### 1.3.2 有序列表示例：

1. item1
1. item2
1. item3

### 1.3.3 多级列表示例
注意：第二行**+**前按**Tab键**。

* item1
  + item1.1
  + item1.2
* item2
  + item2.1
  + item2.2
注意：多级列表只支持2层。

### 1.3.4 列表项目有多个段落
注意：正文前有四个空格或制表符

* 第一段

  正文

* 第二段

## 1.4、区块引用

### 1.4.1 普通区块
与标准的markdown语法一致：

> 这是一段文字
> 第二行
> 第三行

### 1.4.2 嵌套区块

> 第一层

>> 嵌套第二层

> 还是第一层

## 1.5、链接、图片

注意：链接中如果带有特殊符号，比如 & 需要用转义字符进行标示\\&。

### 1.5.1 链接
与markdown标准语法兼容。示例：

This is [an example](http://example.com/ “Title”) inline link.
[This link](http://example.net/) has no title attribute.

### 1.5.2 图片
图片示例：

![GitHub Mark](http://github.global.ssl.fastly.net/images/modules/logos_page/GitHub-Mark.png "GitHub Mark")

[马克飞象](http://maxiang.info/)
>专为印象笔记打造，输入完直接保存到印象笔记。也有Chrome的拓展应用。
![](http://cl.ly/image/401z311c3t1w/Image%202014-05-09%20at%2010.25.38%20PM.png)

建议：翻译时，可以直接引用原文链接。在提交到Importnew时，可以通过 上传或插入 功能将图片上传并插入到文章。

# 2、代码
## 2.1、关键词

可以通过“标记需要突出的关键词或变量，例如

`public` => public
`main(String[] args)` => main(String[] args)

## 2.2、代码段

这里与普通markdown语法有些区别。Java代码示例：

```java
public class JavaDemo{
    int i;
    public static void main(String[] args){
        System.out.println("Hello, I am writing a java code in Atom");
    }
}
```
Python代码示例：
```python
print("Hello, Atom!")
```

类似的，通过将brush参数进行替换可以支持其他语言。
支持的常用语言包括java, xml, shell, html, diff。例如替换为xml：
其他支持的语言有：*actionscript3, applescript, bash, c, csharp, cpp, css, coldfusion, delphi, diff, erlang, groovy, html, javafx, javascript, php, pascal, patch, perl, text, powershell, python, ruby, rails, sql, sass, scala, shell, vb, vbnet, xhtml, xml, xslt*。

推荐开启显示行号。如果不需要显示行号，可以设置 **得上网找**。
# 3、表格等复杂情况

markdown的主要设计目标是简洁，通过支持html代码实现对各种复杂情况的处理。
如果需要加入表格等复杂的界面，可以直接嵌入html代码。

表格示例：

<table border=”1″>
  <tr>
    <td>row 1, cell 1</td>
    <td>row 1, cell 2</td>
  </tr>
  <tr>
    <td>row 2, cell 1</td>
    <td>row 2, cell 2</td>
  </tr>
</table>

效果 =>
row 1, cell 1 	row 1, cell 2
row 2, cell 1 	row 2, cell 2

# 4、其他
<!-- 注释 -->

## 4.1  表格
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### 4.2 字体、字号、颜色

<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=12 face="黑体">黑体</font>
<font color=#00ffff size=3>null</font>
<font color=gray size=5>gray</font>

# 5. Reference
http://blog.csdn.net/u011419965/article/details/50536937



Other Confusion Materals
====================
This Atom start with:
http://blog.csdn.net/mduanfire/article/details/50278591

安装markdown-preview-enhanced后，需**重启Atom**.

1.markdown相关材料
---------------
+ http://wowubuntu.com/markdown/  正常的markdown 语法

+ http://knsv.github.io/mermaid/#using-the-mermaid-init-call figure

+ https://atom.io/packages/markdown-preview-enhanced   usage

2.markdown画图Demo
----------
```{mermaid}
graph LR
A-->B
```
```{mermaid}
sequenceDiagram
　　　participant Alice
　　　participant Bob
　　　Alice->John:Hello John, how are you?
　　　loop Healthcheck
　　　　　John->John:Fight against hypochondria
　　　end
　　　Note right of John:Rational thoughts <br/>prevail...
　　　John-->Alice:Great!
　　　John->Bob: How about you?
　　　Bob-->John: Jolly good!
```

3.markdown公式编辑
---------------
$$x=a^2+sin(b)+ln(e)$$
$a^2$

4.引用
-------
> i am kate.

I am a text.

>>I am f

5.
----
+ bird
+ magic

1. hello
2. he

- bb
- dd
* cc
* aa

6.ToPDF
-----
Markdown to PDF

7.TOC
----
通过 ```cmd-shift-p``` 然后选择 ```Markdown Preview Enhanced: Create Toc``` 命令来创建 ```TOC```。
