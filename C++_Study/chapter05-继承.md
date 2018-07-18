
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 05 继承(inheritance)](#chapter-05-继承inheritance)
	* [1. 公有继承](#1-公有继承)
	* [2. 私有继承和保护继承](#2-私有继承和保护继承)
	* [3. 多重继承(避免使用)](#3-多重继承避免使用)

<!-- tocstop -->


# Chapter 05 继承(inheritance)
Begin  : 2018.7.12
End	   : 2018.7.14
Author : Xiang
Email  : ugoood@163.com

OOP 三大特性:
* 封装 encapsulation
* 继承 inheritance
* 多态 polymorphism

**画类图工具 astah**

## 1. 公有继承
C++ 有三种继承方式：
* 公有继承 重点 默认公有继承
* 私有继承
* 多重继承

公有继承：

```cpp
class Teacher : public Person{
	// 私有继承为 private
	// 略
};
```

具体例子，Animal类 Cat类 Dog类，1个父类，２个子类，如下：

```cpp {.line-numbers}
// animal.h

#ifndef _ANIMAL_H_
#define _ANIMAL_H_

#include <string>
#include <iostream>
using namespace::std;

namespace wk{ // 命名空间

class Animal{
public:
	Animal(int age, string location);
	~Animal();

	void setAge(int age);
	int getAge() const;

	string getLocation() const{
		return m_location;
	}

protected:
	void setLocation(string location){
		cout << "Animal setLocation" << endl;
	}

	string m_location;  //<--子类可访问父类protected的成员

private:
	int m_age;
};

class Cat : public Animal{
public:
	Cat(int age, int color, string location);
	~Cat();

	void setCatLocation(string location);

	void setColor(int color);
	int getColor() const;

private:
	int m_color;
};

/*
class Dog : public Animal{
public:
	Dog(int age, int weight);
	~Dog();

	int getWeight() const;
	void setWeight();

private:
	int m_weight;
};
*/

}

#endif
```

```cpp {.line-numbers}
// animal.cpp

#include "animal.h"

#include <iostream>
using namespace::std;

namespace wk{

/******** Animal **********/

Animal::Animal(int age, string location)
	:m_age(age), m_location(location)
{
	cout << "Animal constructing" << endl;
}

Animal::~Animal(){
	cout<<"Animal destructing" << endl;
}

int Animal::getAge() const{
	return m_age;
}

void Animal::setAge(int age){
	m_age = age;
}
/***********************/


/******** Cat **********/

Cat::Cat(int age, int color, string location)
	:Animal(age, location), m_color(color)  // <-- 注意这，用父类初始化 age 的写法！！！
{
	cout << "Cat constructing....." << endl;
}

Cat::~Cat(){
	cout << "Cat destructing....." << endl;
}

void Cat::setColor(int color){
	m_color = color;
}

int Cat::getColor() const{
	return m_color;
}

void Cat::setCatLocation(string location){
// 子类可访问父类 protected 的成员，不能访问private成员
	Animal::setLocation(location);
}
/**********************/


/******** Dog **********/
/*
Dog::Dog(int age, int weight)
	:Animal(age), m_weight(weight)
{
	cout << "Dog constructing....." << endl;
}

Dog::~Dog(){
	cout << "Dog destructing....." << endl;
}

void Dog::setWeight(int weight){
	m_weight = weight;
}

int Dog::getWeight() const{
	return m_weight;
}
*/

}
```

```cpp {.line-numbers}
//main.cpp

#include "animal.h"
using namespace::wk;

int main(){

	Cat cat(1,1);
	cat.setAge(2);
	cat.setColor(2);

	/*
	Dog dog(2,2);
	dog.setAge(3);
	dog.setWeight(3);
	*/

	return 0;
}
```

我也不知道 Dog 类为啥报错!
子类可访问父类 public 和 protected 的成员，但不能访问 private 的成员。
生成子类对象时：构造父 -> 构造子
析构时：析构子 -> 析构父

## 2. 私有继承和保护继承
私有继承：
1. 父类的 public, protected 成员都以 **private** 身份出现在私有继承的子类中，但父类的 private 成员不可直接访问。
2. 子类的成员函数可以直接访问父类的 public 和 protected 成员，不能访问 private 成员。
3. **通过子类的对象不能直接访问父类中的任何成员。**

保护继承：上述条款的 private 换成 protected即可。保护继承很少见，语法上存在。

## 3. 多重继承(避免使用)
例子：

```cpp {.line-numbers}
class Bed{};
class Sofa{};

class SleeperSofa:public Bed, public Sofa{ // 多重继承
public:
	SleeperSofa(){}
	void foldOut(){cout<<"折叠沙发床.\n";}
};
```

多重继承的对象拥有父类们的非 private 成员。
