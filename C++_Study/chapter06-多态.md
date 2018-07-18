
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 06 多态(Polymorphism)](#chapter-06-多态polymorphism)
	* [1. 多态(Polymorphism)](#1-多态polymorphism)
	* [2. 纯虚函数与接口类](#2-纯虚函数与接口类)
	* [3. 多态时，多态基类的析构函数必须是 virtual 的(重要)](#3-多态时多态基类的析构函数必须是-virtual-的重要)

<!-- tocstop -->


# Chapter 06 多态(Polymorphism)
Begin  : 2018.7.18
End	   : 2018.7.18
Author : Xiang
Email  : ugoood@163.com

## 1. 多态(Polymorphism)
1. **C++ 用 virtual 修饰函数，让它变为虚函数，以支持多态特性。而 Java 中，所有函数默认为虚函数！**

```cpp {.line-numbers}
// animal.h

#ifndef _ANIMAL_H_
#define _ANIMAL_H_

#include <iostream>
using namespace::std;

class Animal
{
public:
	Animal() {
		cout << "Animal constructing" << endl;
	}
	~Animal() {
		cout << "Animal destructing" << endl;
	}

	void makeSound() const {
		cout << "Animal make sound" << endl;
	}
};

class Dog : public Animal {
public:
	Dog() {
		cout << "Dog constructing" << endl;
	}
	~Dog() {
		cout << "Dog destructing" << endl;
	}

	void makeSound() const {
		cout << "Dog make sound" << endl;
	}
};

class Cat : public Animal {
public:
	Cat() {
		cout << "Cat constructing" << endl;
	}
	~Cat() {
		cout << "Cat destructing" << endl;
	}

	void makeSound() const {
		cout << "Cat make sound" << endl;
	}
};

#endif // !_ANIMAL_H_
};
```

```cpp {.line-numbers}
// main.cpp: 定义控制台应用程序的入口点。

#include "stdafx.h"
#include "animal.h"

void func(const Animal& animal) {
	animal.makeSound();
}

int main()
{
	Dog dog;
	Cat cat;

	func(dog); // error: animal make sound
	func(cat); // error: animal make sound

	dog.makeSound(); // right: dog make sound
	cat.makeSound(); // right: cat make sound

    return 0;
}
```

**上例，若想让 func(dog) 展现多态性质，需在 animal 的类makeSound方法中加入`virtual`关键字，** 虚函数，如下：

```cpp
virtual void makeSound() const {}
```

2. 引用，指针做参数传递，可以展现多态性质，但按值传递(也就是copy一个对象)时无多态性质，例子如下：

```cpp
// 1. 引用 right
void func(const Animal& a){
  a.makeSound();
}

// 2. 指针 right
void foo(Animal* pa){
  pa -> makeSound();
}

// 3. copy, 不报错，但无多态性质
void bar(Animal a){
  a.makeSound();
}
```

3. 多态的另一个例子：

```cpp
Animal* a = new Dog();
a->makeSound(); // 输出 dog make sound, 和 java 一样
```

## 2. 纯虚函数与接口类
类中函数加 virtual，就是 **虚函数**，虚函数定义=0，即为 **纯虚函数**，拥有纯虚函数的类不能创建对象！这和 java 一个样。

**接口：类中所有函数都是纯虚函数，该类叫做接口**。C++ 中没有特定的接口关键字，而 java 有，为 interface。

接口例子：

```cpp
// 接口
class Animal{
  virtual ~Animal()=0; // 纯虚函数
  virtual void makeSound()=0;
};
```

抽象类例子，C++ 中也没有抽象类的关键字：

```cpp
// 抽象类
class Animal{
  virtual ~Animal(); // 虚函数
  virtual void makeSound();
};
```

像 java 一样，C++ 中的接口可通过子类公有继承的方式实现接口，并用多态的形式使用子类对象。

## 3. 多态时，多态基类的析构函数必须是 virtual 的(重要)

**注意：多态父类(即所谓的接口，和抽象类，但在 C++ 中貌似还有一个统称：多态基类或多态父类)的析构函数必须是 virtual 的！** 注意`virtual ~Animal();`和`virtual ~Animal()=0;`。

**<font color=red>通过基类的指针释放子类对象时，若基类析构不是虚函数，则导致内存泄漏！例子如下：<font>**

```cpp
int main(){
  Animal* a = new Cat();
  a -> makeSound();
  delete a; // <-- 注意这
  // 若Animal的析构函数不是虚函数，
  // 此处只调用 Animal 的析构，而不调用 Cat 类的析构，造成内存泄漏。
  // 解决方法：修改 Animal 的析构为虚函数即可！
  a = NULL;
  return 0;
}
```

Java 有祖宗类`Object`，而 C++ 没这种类。C++ 程序员做自己框架的祖宗类时，需把该多态基类的析构函数声明为 virtual 的！
