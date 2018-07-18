
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [Chapter 03 类与对象](#chapter-03-类与对象)
	* [1. 类和对象在c++中的简单例子](#1-类和对象在c中的简单例子)
	* [2. 函数参数为类类型变量 - 指针，引用(效果同 java)两种方式指向类的某对象](#2-函数参数为类类型变量-指针引用效果同-java两种方式指向类的某对象)
	* [3. Encapsulation](#3-encapsulation)
	* [4. 构造函数](#4-构造函数)
		* [4.1 构造函数的初始化列表](#41-构造函数的初始化列表)
	* [5. 析构函数](#5-析构函数)
	* [6. 标准库类型 string](#6-标准库类型-string)
	* [7. static 静态成员](#7-static-静态成员)
	* [8. 动态内存分配1](#8-动态内存分配1)
	* [9. 动态内存分配2(重点中的重点)](#9-动态内存分配2重点中的重点)
	* [10. 拷贝构造函数1(copy constructor)](#10-拷贝构造函数1copy-constructor)
	* [10. 拷贝构造函数2(copy constructor 和赋值运算符重载)](#10-拷贝构造函数2copy-constructor-和赋值运算符重载)
	* [11. const 关键字 - 常量](#11-const-关键字-常量)
	* [12. 友元(friend)函数与友元类](#12-友元friend函数与友元类)
	* [13. 案例 - 单例设计模式](#13-案例-单例设计模式)
	* [14. valgrind 内存检测工具](#14-valgrind-内存检测工具)

<!-- /code_chunk_output -->

# Chapter 03 类与对象
Begin  : 2018.7.6
End	   : 2018.7.12
Author : Xiang
Email  : ugoood@163.com

## 1. 类和对象在c++中的简单例子
java 纯面向对象的。
c++ 结构化 + 面向对象
c 结构化

类和对象的简单例子：

```cpp {.line-numbers}
// 类

#include <iostream>
using namespace::std;

// 类定义
class Car{
// 成员变量
private:
	int price;
	int id;

// 成员函数
public:
	void show(){
		cout << price << " : " << id << endl;
	}

	void setPrice(int p){
		price = p;
	}

	void setID(int i){
		id = i;
	}
};

int main(int argc, char *argv[]) {
	Car c;
	c.setPrice(1000);
	c.setID(1);
	c.show();
	cout << sizeof(c) << endl;  // 4+4
	return 0;
}
```

也可将类定义，与main所在文件分开。

下面例子包含3个文件：
* car.h   类定义，类似java的接口
* car.cpp　类实现
* main.cpp　调用 car.h 就能使用 Car 类的对象

car.h如下：

```cpp {.line-numbers}
#ifndef _CAR_H
#define _CAR_H

class Car{
private:
	int price;
	int id;

public:
	void show(); // 显示 price 和 id
	void setPrice(int p);
	void setID(int i);
};

#endif
```

car.cpp如下：

```cpp {.line-numbers}
#include<iostream>
using namespace::std;

#include "car.h"

void Car::show(){
	cout << this -> price << " : " << this -> id << endl;
}

void Car::setPrice(int price){
	this -> price = price; // this 表示当前对象，同java
}

void Car::setID(int id){
	this -> id = id;
}
```

main.cpp如下：

```cpp {.line-numbers}
#include <iostream>
using namespace::std;

#include "car.h"

int main(){
	Car c;
	c.setPrice(1000);
	c.setID(1);
	c.show();
	cout << sizeof(c) << endl;  // 4+4
	return 0;
}
```

**控制台中输入`g++ car.cpp main.cpp -o test`进行编译，输入`./test`查看结果。**

**上述代码中，`#include "car.h"`类似于 java 中的 import，将 car.h 中定义的 Car 类导入当前文件中。这样，在当前文件中(main.cpp)就可以直接使用 Car 这个类了。**

**<font color=red>下面这种组织方式，感觉更适合我：</font>**

car.h：

```cpp {.line-numbers}
#ifndef _CAR_H
#define _CAR_H

#include <iostream>
using namespace::std;

class Car{

private:
	int price;
	int id;

public:
	Car(int price, int id){ // 有参构造函数
		this -> price = price;
		this -> id = id;
	}

	void show(){
		cout << price << " : " << id << endl;
	}
};

#endif
```

main.cpp：

```cpp {.line-numbers}
#include "car.h"

int main(){
	Car c(2022,30);
	c.show();

	return 0;
}
```


## 2. 函数参数为类类型变量 - 指针，引用(效果同 java)两种方式指向类的某对象

修改上节的 main.cpp 如下：

```cpp {.line-numbers}
#include <iostream>
using namespace::std;

#include "car.h"

// 通过指针指向本类对象的成员
void foo(Car* pcar){  // <-- 注意这
	pcar -> show();
}

int main(){
	Car c;
	c.setPrice(1000);
	c.setID(1);

	foo(&c); // c++ 真够烦的了

	return 0;
}
```

上面内容很烦！

**c++ 中也可用引用来表达某个对象，这个用法就和 java 一样了。**

```cpp {.line-numbers}
#include <iostream>
using namespace::std;

#include "car.h"

// 通过指针指向本类对象的成员
/*
void foo(Car* pcar){
	pcar -> show();
}
*/

// 通过引用，效果同 java
void foo(Car& car){
	car.show();
}

int main(){
	Car c;
	c.setPrice(1000);
	c.setID(1);

	foo(c); // c++ 这回就他x的和　java 一样方便了

	return 0;
}
```

## 3. Encapsulation
Encapsulation：成员变量和成员函数封装在类中，具体实现被隐藏。其余略。

## 4. 构造函数

```cpp {.line-numbers}
// 构造函数

#include <iostream>
using namespace::std;

class Car{

private:
	int price;
	int id;

public:
	Car(int price, int id){ // 有参构造函数
		this -> price = price;
		this -> id = id;
	}

	void show(){
		cout << price << " : " << id << endl;
	}
};

int main(int argc, char *argv[]) {
	Car c(10000, 1);  // <- 注意
	c.show();
	return 0;
}
```

### 4.1 构造函数的初始化列表
初始化列表中数据的初始化顺序要和声明中顺序一致，如下：

```cpp {.line-numbers}
#include<iostream>
using namespace;

class Student{
	public:
		Student(int ssID=0) : id(ssID), score(100){ // <- 重点
			cout << "构造函数初始化列表例子" << endl;
		}

	private:
		int id;
		int score;
}
```

## 5. 析构函数
对象生命周期结束时，析构函数将执行，回收该对象所占资源。
析构函数不能重载。形式如下：

```cpp {.line-numbers}
class Student{
	public:
		Student(int id){
			this -> id = id;
		}

		~Student(){  // < -- 析构函数
			cout << "I am destructor!!" << endl;
		}		

	private:
		int id;
		int score;
}
```

## 6. 标准库类型 string
内容比较简单，用下面例子说明：

```cpp {.line-numbers}
#include<string>  // <-- 导入这个类
#include<iostream>
using namespace::std;

int main(){
	string a("hello");
	string b(a);
	string c(10,'c');
	string d = "ddddd";

	cout << a.empty() << endl;
	cout << a.size() << endl;
	cout << a[0] << endl;
	cout << a + b << endl;	// 连接

	a = d;			// 赋值
	cout << a << endl;

	cout << (c==d) << endl; // 俩串是否相等
}
```

## 7. static 静态成员
静态成员属于类，不属于对象，静态成员可通过类直接调用。
说白了 static 修饰的成员是共享资源(全体中国人国籍都是中国)。

* 成员变量和成员函数用 static 修饰；
* 成员变量和成员函数调用时用`类名::变量或函数名`方式，如`People::nation`。

```cpp {.line-numbers}
#include<iostream>
#include<string>
using namespace::std;

class Person{

	public:
		// static string nation = "aa";  // 1. 类中竟不允许初始化static成员变量
		static string nation;  //类定义中，不能对static变量初始化，好奇怪，不知道c++为啥这样设置
		static void show(){
			cout<<"show : " << Person::nation << endl;
		}
};


string Person::nation = "China"; // 2. 必须在全局变量中对static成员变量初始化，在main()中初始化也不行！

int main(){

	Person::nation = "Japan"; // 3. 此处，若无第16行代码，这就报错了！
	Person::show();
	cout << Person::nation << endl;

	Person p;
	cout << p.nation << endl;
	p.nation = "US";
	cout << p.nation << endl;
	cout << Person::nation << endl;　// 4.　24-28行代码的执行，和java相同

	return 0;
}
```

在 static 这个问题上，与 java 相比的所有疑惑，都在上面代码的注释中。感觉 c++ 好奇怪。

## 8. 动态内存分配1
局部变量什么的是在栈(stack)上搞事情。

动态内存分配是在堆(heap)上搞事情，如下：
c++ new/delete -> 运算符
c  malloc/free -> 函数调用

```cpp {.line-numbers}
#include<iostream>
using namespace std;

#include "stdlib.h"

class Test{

	public:

	// 构造
	Test(int val = 0)
		: m_val(val)  // 初始化成员变量
	{
		cout << "Test() run...." << endl;
	}

	// 析构
	~Test(){
		cout << "~Test() run...." << endl;
	}

	private:
		int m_val;
};

int main(){
	////////// c++ 的　new/delete 属于堆中操作  ////////////
	{
	Test a;  // 1. 栈中生成对象
	}  // 2. 析构被调用，a　对象 在此被释放

	cout << "meet }" << endl;

	Test* b = new Test();  // 3. heap 中生成对象

	cout << "没调用 delete 前，b　不会被释放，即使 b 遇到了 ｝,必须手动 delete" << endl;

	delete(b);  // 4. 手动 delete 释放 heap 中对象
	b = NULL;	// 5. b=NULL 这是规范

	b = new Test(100);  // 6. 初始化对象的 field
	delete(b);
	b = NULL;
	////////////////////////////////////////////////////////


	////////// c 中的 malloc/free 属于栈中操作  ////////////
	int* p = (int*)malloc(sizeof(int));  // c语言：int型指针变量p 指向栈中int大小的内存区域
	free(p);
	p = NULL;
	///////////////////////////////////////////////////////


	////////// c++ 生成对象数组  ////////////
	Test* pArray = new Test[2];  // new 2 次

	delete[] pArray;  // delete 2 次
	// delete pArray;  // <-- 小心！！！编译不报错，run 时报错
	///////////////////////////////////////////////////////

	return 0;
}
```

## 9. 动态内存分配2(重点中的重点)
1. bss段：**存放没有初始化或初始化为 0 的全局变量**，生命周期为程序开始－结束，较长，故 ***编码规范*** 中要求尽量不要搞很多全局变量。
**下面程序编译结果为 8.4k，strip 后大小为 6.2k。**

```cpp
int bss_array[1024*1024] = {0};
int main(){return 0;}
```

2. data段：存放初始化为 **非零的全局变量**。
**下面程序编译结果为 4.1M。即使 strip 大小也不变。**

```cpp
int bss_array[1024*1024] = {1};
int main(){return 0;}
```

3. 静态成员变量
静态成员变量是和全局变量放一起，至于时 bss段 还是 data段 我懒得验证。

4. rodata区存放常量数据。
常量不一定放在 rodata　中，有些立即数直接和指令一起放在代码区；
字符串常量，编译器会去重，保证只有一个副本(类似java字符串常量池)；
字符串被编译器自动放入 rodata 中；
const 关键字修饰的全局变量也放在 rodata 中

**下列描述了 rodata 存放的常量无法修改，可以赋值字符串到某内存区域，在修改某字符，如下：**
> 感觉 rodata 区里的内容就是无法修改，所谓常量，就是进入了该区。像下面的字符串常量 hello，就进入了 rodata 区，无法修改了。想改的话只能 copy rodata 区的常量 "hello" 到非 rodata 区，如栈中，再随便改！

```cpp {.line-numbers}
#include<iostream>
#include<stdlib.h>  // malloc
#include<string.h>  // strcpy
using namespace std;

int main(){
	char* p = "hello";
	for(int i=0; i<5; i++){
		cout << p[i] << endl;
	}
	cout << "-----------" << endl;
	// p[1] = 'x';  // <-- 1. 不能给字符串常量赋值 程序崩溃

	//  2. 办法是 把字符串 copy 到内存某区域，我觉得下面时 stack 区
	char* pp = (char*)malloc(5);
	memset(pp, 0, 5);  // init 0
	strcpy(pp, p);  // copy from p to pp

	pp[1] = 'x';  // < -- 这就没问题了

	cout << "-----------" << endl;
	for(int i=0; i<5; i++){
		cout << pp[i] << endl;
	}
	return 0;
}
```

5. **stack(栈)区内的局部变量，我们不用维护。当栈中的变量退出其作用域时，栈内局部变量所占存储单元会被自动释放，不需我们管理。**
6. **heap(堆):程序员用 malloc/new 申请的内存区或创建的对象，会在 heap 中分配空间，此时需程序员自己管理内存，释放时用相应的 free/delete 函数或命令。**　堆这么麻烦(需程序员自己管理内存的申请和释放)为什么我们还得用它？那是为了多个程序互相传递数据资源，我们不可能把所有代码都写在同一个函数中(也就是同一个栈中)。另外栈空间可能很小(人家说的，天知道这是为啥)。
7. 整个程序所占用的内存时随着对象们的创建和销毁动态变化的。(c++ 挺复杂呢，她得由程序员决定 heap 中对象的创建与 **销毁**，那程序员编蒙了咋办？程序员需对对象的生命周期有相对精准的把握，小程序还行，大型程序的话这岂不是噩梦？Java倒是不用程序员管理对象的销毁，那也就是说，java 编出来的程序可能在 c++ 大神看来，效率很低)
8. 变量的作用域决定了对象的生命周期。
9. 全局对象在 main 之前被创建，main 退出后被销毁。

**体现生命周期的例子：**

```cpp {.line-numbers}
#include<iostream>
using namespace std;

class A{
public:
	A(){cout << "A() run........" << endl;}
	~A(){cout << "~A() run........" << endl;}
};

class B{
public:
	B(){cout << "B() run........" << endl;}
	~B(){cout << "~B() run........" << endl;}
};

A globalA;  // 1. 全局变量 main之前生成，main 结束时销毁
B globalB;

void foo(){
	cout << "foo() ----------->>>" << endl;
	A localA;
	static B localB; // 2. 这里颠覆了我对 static 的认知！这只体现了 静态变量和常量一起在常量区，和java中的 类.静态成员　几乎毫无关系了。
	cout << "foo() <<<-----------" << endl;
}

int main(){
	cout << "main() ----------->>>" << endl;
	foo();
	foo();
	cout << "main() <<<-----------" << endl;
	return 0;
}
```

**查看结果：**

```
A() run........　全局
B() run........　全局
main() ----------->>>
foo() ----------->>>
A() run........　局部
B() run........　静态局部
foo() <<<-----------
~A() run........　局部，但静态局部 localB 并没销毁
foo() ----------->>>
A() run........ 局部
foo() <<<-----------
~A() run........　局部
main() <<<----------- main结束
~B() run........　静态局部 localB 销毁
~B() run........　全局
~A() run........　全局
```

10. **通过 new 创建的对象，一直存在，直到被 delete 销毁。易造成内存泄露。**
11. **<font color=red>拷贝构造函数: 隐藏在中间的临时变量的创建和销毁，生命周期很短，易出问题。</font>**

## 10. 拷贝构造函数1(copy constructor)
拷贝构造函数，它是一个特殊的构造函数，用来制造某特定对象的副本。

copy constructor 例子：

```cpp
Student(const Student& s){ // <--- copy constructor 的固定样式
	strcpy(this -> name, s.name); // 假设Student对象有 name 和 id 两个成员变量
	this -> id = s.id;
}
```

拷贝构造函数调用的时机是：
1. 给 Student 对象赋 Student 对象，如：

```cpp
Student joe("joe",111);　// 假设 Student 类有这个构造函数
Student john = joe; // <-- copy constructor 被调用
```

2. 给函数参数传对象时，如下种形式：

```cpp
void foo(Student stu){}
int main(){
	foo(joe);  // <-- copy constructor 被调用
	// foo　接受了 joe 对象的一个副本，原 joe 对象不会受影响！！！
	return 0;
}
```

另一种样式(不会调用 copy constructor)：

```cpp
void boo(const& Student stu){}
int main(){
	boo(joe);  // <-- copy constructor 　不　被调用
	// 这个 joe 和　原来的 joe 是同一个 joe，
	// 但 boo 函数无法对传来的对象进行修改，因为 stu 声明了 const
	return 0;
}
```

3. 返回值是 Student 对象时，如：

```cpp
Student bar(){
	Student tom("tom", 112);
	return tom;
}
```

有2个关于 copy constructor 的事需说明：
* 4种东西，程序员不定义的话，编译器会默认定义 - 构造，析构，拷贝构造函数，赋值运算符。
* 拷贝构造函数就像下面的东西一样自然：

```cpp
int i = 100;
int j = i; // 改j不影响i, 把i的副本给了j
且
void foo(int val){}
foo(j) 时，不影响 i
```

## 10. 拷贝构造函数2(copy constructor 和赋值运算符重载)
**若类数据成员无指针，基本上就不需定义 copy constructor 和赋值运算符！！！**

浅copy：默认的 copy constructor，使得 两个指针指向同一个资源(对象)；
深copy: 程序员自己定义，一般要另外在堆中申请资源(原资源也在堆中)，使得2个对象指向不同的内存区域，但内容相同。

```cpp {.line-numbers}
#include<iostream>
using namespace std;

class A{
public:
	int age;
	string name;
	A(){}

private:
	// A(const A& a){}; // <--- copy construction 为私有，谁调它将报错
	// A operator=(const A& other){}; // <--- 赋值运算符为私有，28行将报错
};

int main(){

	A a;
	a.age = 10;
	a.name = "hello";

	A *b = &a;  // a,b 指向相同对象
	cout << b-> name << b-> age << endl;
	cout << b << endl;
	cout << &a << endl;

	A c;
	c = a;  // c 是 a 的副本，既 c 和 a 指向不同内存区域
	cout << c.age << c.name << endl;
	cout << &c << endl;

	return 0;
}
```

何时需定义 copy constructor？
* 类数据成员有指针；
* 类数据成员管理资源(如打开一个文件)。

表象上看：若一个类需要析构函数来释放资源，则它也需要一个 copy constructor。

**<font color=red>为啥时上面那样？自己理解：</font>**
1. 上例子中，c = a，用的是默认赋值运算符。默认赋值运算符和默认 copy constructor 一样，有一种相同的行为，那就是：
2. 都建立副本，且副本中所有成员变量值相同(要不咋叫副本呢)。那问题来了：
3. 若成员变量有指针，假设时数组指针，指向一片内存区域，那么
4. c 和 a 都有值相同的指针变量。既，c 和 a 里的那个指针成员变量指向同一个地方。
5. c 就不算是一个真正的副本了, 因为 c 和 a 指向相同的内存区域。我们不想这样，怎么办？
6. 答案就是重写 copy constructor 和 赋值运算符！怎么写？
7. 很简单，那就是在 copy constructor 和 赋值运算符 中重写申请与原对象指针所指内存区大小相同的内存区，再把原对象内存区内的内容逐个复制到副本中刚刚申请的内存区域内。比如：原对象中有int(10)大小的数组，那副本中也申请int(10)大小的数组，再把原对象数组中的内容依次传送到副本对象的数组中(**数组是用指针指向的，既原对象和副本对象都有指针类型的数据成员**)。

## 11. const 关键字 - 常量
例子：

```cpp
const int BUFFER_SIZE = 512; // c++
#define BUFFER = 512; // c
```

1. 指一个不该被改动的对象。

const 限定指针类型(应付面试)：
* const 在星号左边，表被指物是常量；
* const 在星号右边，表指针自身是常量；

e.g.

```cpp
int a = 1, b = 0;
const int* p = &a;
// 说的是 *p 所值物是常量，说白了就是不能用*p去修改a的值
// 限制了指针p的行为

p = &b; // 这没问题

```

```cpp
int a = 1, b = 0;
int* const p = &a; // 指针自身是常量
*p = 100; // ok
p = &b;　// error
```

2. **const 数据成员必须使用初始化列表进行初始化。**

```cpp {.line-numbers}
Class A{
public:
	A();
	~A(){}
private:
	const int val; //常量数据成员
};

A::A()
		:val(0) // ok 必须使用初始化列表
{
	// val = 0; //error
}

int main(){
	A a;
	return 0;
}
```

3. const 成员函数：显示表明该函数不会修改数据成员，使得类清晰。

```cpp
class Data{
public:
	const int getValue() {return val;} // const 成员函数
	Data():val(10){}

private: int val;
};
```

4. 控制使用指针和引用传递的实参被意外修改。
例子：

```cpp
class Person{};

void foo(Person p){} // 副本

void bar(const Person& p){}　// 无副本，read-only 操作原对象
```

**<font color=red>注意：</font>**
- **foo 和 bar 相同点为都不会对原对象修改，因为：**
- **foo 里建立了 Person 对象的副本**
- **bar 里不建副本，使用原对象(省略了copy和析构过程，效率高)。**
- **即使bar使用原对象，但也无法修改原对象(因const修饰)，也保证了原对象的不变性。**

## 12. 友元(friend)函数与友元类
目的：为编程方便。
故事：
* 在某些情况下，允许特定的非成员函数访问一个类的私有成员，同时仍阻止一般的访问；
* 友元机制允许一个类将对其非公有成员的访问授予指定的函数或类；
* 友元关系是授予的：
	- 为了让类B成为类A的友元，类A必须显式声明类B是他的友元
* 友元关系是不对称的；
* 友元会破坏封装。

友元例子：

```cpp {.line-numbers}
// class X 中声明了 Y 是它的友元(friend)

class X; //前置声明

class Y{
public:
	void f(X*);  // 用友元时，得用指针，或引用
	// void b(X);  // 不能复制X对象的副本<-- error

private:
	X* pX; // <-- also ok
};

class X{
public:
	friend void g(X*, int); // global friend
	friend void Y::f(X*); // class member friend
	friend class Z; // Entire class Z is X's friend
	friend void h();

private: int i;
};

class Z{
public:
	Z():(j = 99){}
	void g(X* x);
private:
	int j;
};

Z::g(X* x){
	x -> i += j;
}

// global
void h(){
	X x;
	x.i = 100; // Direct data manipulation
}
```

## 13. 案例 - 单例设计模式
就是一个类保证只对外提供一个对象。

singleton.h：

```cpp {.line-numbers}
#ifndef _SINGLETON_H_
#define _SINGLETON_H_

class Singleton{

public:
	static Singleton* getInstance();  // to get a single instance
	void doSomething();  // 普通公有函数
	void destroy();  // destroy this instance

private:
	Singleton();  // constructor
	~Singleton();  // deconstructor

	Singleton(const Singleton&);  // copy constructor
	Singleton& operator=(const Singleton&);  // assignment operator

	static Singleton* instance;  // a single instance
};

#endif
```

singleton.cpp：

```cpp {.line-numbers}
#include "singleton.h"
//#include <singleton.h>  //error

#include <iostream>
using namespace::std;

Singleton* Singleton::instance = NULL; // 静态成员变量必须在类外初始化

Singleton::Singleton(){  // constructor
	cout << "Singleton instance" << endl;
}

Singleton::~Singleton(){}  // deconstructor

Singleton* Singleton::getInstance(){
	Singleton* ret = instance;
	if(instance == NULL){
		instance = new Singleton();
		ret = instance;
	}
	return ret;
}

void Singleton::doSomething(){
	cout << __func__ << ", " << __LINE__ << endl;
}

void Singleton::destroy(){
	delete this;
	instance = NULL;
	cout << "The singleton instance is destroied!!!" << endl;
}
// g++ -c singleton.cpp   "-c" 表示只编译，不链接，生成 .o　字节码文件

```

main.cpp:

```cpp {.line-numbers}
#include "singleton.h"

int main(){
	Singleton* s = Singleton::getInstance();
	s -> doSomething();
	s -> destroy();
	s -> doSomething();  // 莫名其妙，仍能调用该实例
	return 0;
}
```

编译，链接过程如下：

```
g++ -c singleton.cpp  // 编译
g++ -c main.cpp  // 编译
g++ singleton.o main.o -o test // 链接生成可执行文件 test
./test  // 执行 test
```

## 14. valgrind 内存检测工具
valgrind可检测出申请的空间是否被释放，同一空间是否被多次释放等问题。这种问题编译时时检测不到的，可能运行结果也正确，但程序本身实际上有错误。

```cpp {.line-numbers}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 下面代码有2个问题
// 1. 10个地方只能存9个char
// 2. p　最后没有 free
// 编译没问题，也可执行，但代码有问题，可用valgrind工具检测

int main(){
	char* p = NULL;
	p = (char *)malloc(10);
	strcpy(p,"0123456789");
	return 0;
}

/* right */
/*
int main(){
	char* p = NULL;
	p = (char *)malloc(10);
	strcpy(p,"012345678");
	free(p);
	p = NULL;
	return 0;
}
*/

/************valgrind 使用方法************************

0. sudo apt-get install valgrind  安装 valgrind 工具

1. gcc -Wall -g　main.cpp -o test
Wall 输出所有警告
g 使用debug版

2. 当前目录新建 valgrind.sh，并写入：
valgrind --tool=memcheck --show-reachable=yes --leak-check=yes $1
$1 表示可执行文件

3. 把 valgrind.sh 变成可执行文件，命令：chmod +x vlagrind.sh

4. ./valgrind.sh ./test 查看结果
**************************************************/
```
