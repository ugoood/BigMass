
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [Chapter 1, 2 C++ 基础](#chapter-1-2-c-基础)
	* [1. 命名空间 namespace](#1-命名空间-namespace)
	* [2. 引用](#2-引用)
		* [2.1 传递引用给函数](#21-传递引用给函数)
		* [2.2 引用参数传递需注意的问题](#22-引用参数传递需注意的问题)
	* [3. 内联函数(inline) 和 宏定义](#3-内联函数inline-和-宏定义)
	* [4. 默认参数的函数](#4-默认参数的函数)
	* [5. 函数重载](#5-函数重载)
	* [6. 函数模板](#6-函数模板)

<!-- /code_chunk_output -->

# Chapter 1, 2 C++ 基础 - 命名空间 - 函数参数 - 内联函数 - 重载 - 函数模板
Start : 2018.7.3
End	  : 2018.7.6
Autor : Xiang

## 1. 命名空间 namespace
在不同 namespace 中可用相同的变量名字,目的是解决同名问题.

```cpp {.line-numbers}
// 命名空间

#include <iostream>
using namespace::std;

namespace One{
	int M = 200;
	int inf = 10;
}

namespace Two{
	int x;
	int inf = 100;
}

int main(int argc, char *argv[]) {
	using Two::x;
	cout << x << endl;
	cout << One::inf << "我是 One::inf" << endl;
	cout << Two::inf << "我是 Two::inf" << endl;
}
```

关于`using namespace::std`，他使得`cout`和`endl`正常工作。若无 std 命名空间的引入，程序中得这样写才正确：`std::cout`，`std::endl`。

## 2. 引用
主要用在函数参数。
动机：传值，当值是个结构体一类的东西时(值体积很大)，传值需复制，速度慢，占空间多。这时用引用。
引用时给一个变量起别名(小名)，大名小名都指同一个东西。避免了复制。

例子：

```cpp {.line-numbers}
// 引用 reference.cpp

#include <iostream>
using namespace::std;

int main(int argc, char *argv[]) {

	int intOne = 0;
	int intTwo = 2;
	int& r_int_One = intOne;  // int& 声明引用
	// int& r_int_One = intTwo;  // 一个引用不能再指向别处

	intOne = 5;

	cout << intOne << endl;
	cout << r_int_One << endl;

	r_int_One = 7;			  // 对引用的修改就是对变量的修改

	cout << intOne << endl;
	cout << r_int_One << endl;

	// 引用 和 变量 的地址输出
	cout << &(intOne) << endl;
	cout << &(r_int_One) << endl;
}
```

注意：
* void 引用是不合法的，如`void& a`；
* 不能建立数组元素为引用的数组；
* 有空指针，但无空引用。

### 2.1 传递引用给函数
这方式比指针有更清晰的语法。

```cpp
void swap(int& x, int& y){
	int temp;
	temp = x;
	x = y;
	y = temp;
}
```

例子：

```cpp {.line-numbers}
// 引用 reference_fun.cpp

#include <iostream>
using namespace::std;

void foo(int x){ // x 接收了个 副本
	x = 10;
}

void bar(int& x){ // 引用
	x = 10;
}

void zoo(int* p){ // 指针
	*p = 10;
}

int main(int argc, char *argv[]) {

	int a = 1;
	int b = 1;
	int c = 1;

	foo(a);	 // a = 1
	bar(b);	 // b = 10
	zoo(&c); // c = 10

	cout << a << " " << b << " " << c << endl;
}
```

### 2.2 引用参数传递需注意的问题

函数返回值时需产生一个值的副本。
用引用返回值时，不生成副本，提高了效率。

下例子时正确的姿势：

```cpp
int res = 0;

int& func(int x){
	res = r*r;
	return res;
}
```

## 3. 内联函数(inline) 和 宏定义
**动机：当1-5行小程序被多次调用时，应考虑把那个小程序搞成内联函数，以避免函数参数传递过程所带来的开销。**
* 内联函数在编译阶段，被编译器嵌入程序中；
* 内联函数不能有 loop 和 switch 的操作，代码也不宜过长。编译器碰到不符合约定的内联函数时，即使有 inline 关键字，该内联函数也不会生效；
* **宏定义** 感觉就是套用模式，当遇到类似`i++`这样的代码时，会产生程序员意料不到的结果。

**c++ 的内联函数可完全代替 c 语言中的宏定义，且消除 c 中宏定义带来的上述负面影响！**

例子：

```cpp {.line-numbers}
// 内联函数 和 宏定义 对比

#include <iostream>
using namespace::std;

// 2个宏定义
#define MAX(a,b) ((a)>(b)?(a):(b))
#define SQUARE(x) ((x)*(x))

// 3个内联函数
inline int max(int a, int b){
	return a > b ? a : b;
}

inline int square(int x){
	return x * x;
}

inline bool foo(int a, int b){
	return a > b;
}

int main(int argc, char *argv[]) {

	int b = 4, c = 4;
	cout << SQUARE(b++) << endl;  // 宏定义 输出令人费解的 20
	cout << square(c++) << endl;  // 内联函数 输出程序员预料到的 16

	b = 4;
	c = 4;
	cout << SQUARE(b) << endl;  // 16 变得正常了
	cout << square(c) << endl;  // 16

	cout << max(2,1) << endl;

	cout << foo(10,100) << endl;  // 输出 0
}
```

## 4. 默认参数的函数
c++ 可以给函数的参数默认值(c 语言不能？)

例子：

```cpp
int add(int x=5, int y=6, int z=3){
	return x+y+z;
}

int main(){
	add();	  // 3参数都是默认值
	add(1,2); // 第三个参数为默认值
	add(1,2,3);
}
```

注意下面代码：

```cpp
void func(int a=1, int b, int c=3); // error
void func(int a, int b=2, int c=3); // correct
void func(int a, int = 2, int = 3); // correct，写法变化而已
```

调用函数时，也有些规则，但不必记忆。
**总之，只要能避免歧义，就是对的，否则就错!**

## 5. 函数重载
重载过于简单，介绍略。

下面展现了 **重载过程中，默认参数的使用存在可能的二义性**：

```cpp {.line-numbers}
// 重载 - 默认参数的存在可能导致的　二义性
// 本程序报错
#include <iostream>
using namespace::std;

int add(int a){
	return a;
}

int add(int a, int b=3){ // 默认参数函数
	return a+b;
}

int main(int argc, char *argv[]) {
	int a = add(2);
	cout << a << endl;
}
```

>本节提到了 makefile 和 make，说有相应课程，这地方不清楚，先 marked。

**对编译后的结果用`objdump -t 目标文件名`查看。**

## 6. 函数模板
泛型编程：独立于任何特定类型的方式编写代码。

模板包括：
* 类模板
* 函数模板(本节所讲的)

函数模板作用，我感觉类似于 java 中的泛型，既，变量类型是可变的，减少了代码量，是代码更易读懂。用下面例子体会一下。

```cpp {.line-numbers}
// 函数模板 template

#include <iostream>
using namespace::std;

// template 1
template<typename T>
T abs(T x){
	return x < 0 ? -x : x;
}

// template 2
template<typename T, typename D> // 可定义多个　类型变量
D add(T a, D b){
	return a + b;
}

int main(int argc, char *argv[]) {
	int i = -5;
	double d = -5.5;
	cout << abs(i) << endl;		// 5
	cout << abs(d) << endl;		// 5.5
	cout << add(i, d) << endl;  // -10.5
}
```
