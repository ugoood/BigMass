
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 04 运算符重载](#chapter-04-运算符重载)
	* [1. 运算符重载(友元函数方式)](#1-运算符重载友元函数方式)
	* [2. 运算符重载(成员函数方式，用的较多)](#2-运算符重载成员函数方式用的较多)
	* [3. 自增运算符重载(`++i`效率高，`i++`效率低)](#3-自增运算符重载i效率高i效率低)

<!-- tocstop -->


# Chapter 04 运算符重载
Begin  : 2018.7.12
End	   : 2018.7.12
Author : Xiang
Email  : ugoood@163.com

运算符重载的要求：看的懂，有例子的时候，能根据需求写出运算符重载代码。
智能指针和STL用本节内容较多。

## 1. 运算符重载(友元函数方式)
对象3 = 对象2 + 对象1，如复数的类，字符串的类。用的符号都是 "="，"+" 号，但行为不同，这就涉及到运算符重载。
**只能对已有的运算符重载，不能增加新的运算符；**
**重载的运算符不会改变原先的优先级和结核性。**

运算符重载的形式：
* 成员函数
* 友元函数

C++ 规定，参数说明都是内部类型时，不能重载，如`int* operator + (int, int*); //error`

使用友元函数重载简例：

```cpp {.line-numbers}
class RMB{//人民币类
public:
  RMB(unsigned int d, unsigned int c);
  friend RMB operator + (RMB&, RMB&); // <-- 重点 重载 +

private:
  unsigned int yuan; // 元
  unsigned int jf; // 分
};
```

完整例子：

RMB.h:

```cpp {.line-numbers}
#ifndef _RMB_H_
#define _RMB_H_

typedef unsigned int uint;  // 希望少写字

#include <iostream>
using namespace::std;

class RMB{
	friend RMB operator+(const RMB&, const RMB&);
	friend bool operator>(const RMB&, const RMB&);

public:
	RMB(uint y, uint jf);
	~RMB();

	void display() const{
		cout << "RMB:" << yuan << ".";
		if(jf < 10){cout << "0";}
		cout << jf << endl;
	}

private:
	uint yuan;
	uint jf;
};

#endif
```

RMB.cpp:

```cpp {.line-numbers}
#include "RMB.h"

RMB operator+(const RMB& val1, const RMB& val2){
	uint jf = val1.jf + val2.jf;
	uint yuan = val1.yuan + val2.yuan;
	if(jf >= 100){
		++yuan;
		jf -= 100;
	}
	return RMB(yuan, jf);
}

bool operator>(const RMB& val1, const RMB& val2){
	bool ret = false;
	if(val1.yuan > val2.yuan){
		ret = true;
	}else if(val1.yuan == val2.yuan){
		if(val1.jf > val2.jf){
			ret = true;
		}
	}
	return ret;
}

RMB::RMB(uint y, uint val):yuan(y), jf(val){}
RMB::~RMB(){}
```

main.cpp:

```cpp {.line-numbers}
# include "RMB.h"

int main(){
	RMB val1(2, 50);
	RMB val2(2, 48);

	if(val1 > val2){
		cout << "val1 is more than val2" << endl;
	}

	val1 = val1 + val2;
	val1.display();

	return 0;
}
```

## 2. 运算符重载(成员函数方式，用的较多)
C++规定：**=, (), [], -> 这四种运算符必须使用成员函数的形式重载。**

简例：

```cpp
// file RMB.h
RMB operator+(const RMB&); // + 左边为this，右边为 RMB&
bool operator>(const RMB&);
```

实现时：

```cpp {.line-numbers}
// file RMB.cpp
RMB RMB::operator+(const RMB& val){
	this->jf += val.jf;
	this->yuan += val.yuan;
	if(jf >= 100){
		++yuan;
		jf-=100;
	}
	return RMB(yuan, jf);
}

bool RMB::operator>(const RMB& val){
	bool ret = false;
	if(yuan > val.yuan) ret = true;
	else if(yuan == val.yuan){
		if(jf > val.jf) ret = true;
	}
	return ret;
}
```

## 3. 自增运算符重载(`++i`效率高，`i++`效率低)
`++i　前增量`和`i++ 后增量`的区别：

```cpp
int main(){
	int i = 1;
	int a = ++i; // a 2, i 2　i先增加，再赋值
	int b = i++; // b 2, i 3  i先赋值，再增加
	return 0;
}
```

**基于上面特性，自增运算符重载时，仍要保持语义！**

成员函数形式的重载：

```cpp {.line-numbers}
// file increase.h

class Increase{
public:
	Increase(int x):value(x){}
	Increase& operator++(); //前增量 ++i，就是这种形式，死扣没必要
	Increase operator++(int); //后增量 i++
private:
	int value;
};
```

`++i`效率高，`i++`效率低的原因：

```cpp {.line-numbers}
// file increase.cpp

Increase& Increase::operator++(){
	value++; // 先增
	return *this; // 再返回原对象
}

Increase Increase::operator++(int){
	Increase temp(*this); // 临时对象存放原有对象
	value++; // 原有对象增量修改
	return temp; // 返回原对象
}
```
