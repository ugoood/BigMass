Java笔记
===

```java
package day01;

import java.util.Arrays;

class Banji{
	String name;
	int id;
	int s_num;
	static String nation;

	int getS_num(){
		return this.s_num;
	}

}

class Person {
	// 1. 成员变量
	String name;
	int age;
	static String nation; // static 修饰的成员变量，属于类的



	// 3. constructor
	Person() {
		System.out.println("Person() is running!");

	}

	Person(String name, int age) {
		this();
		this.name = name;
		this.age = age;
	}

	// 2. 成员方法(成员函数)
	void speak() {
		eat();
		speak();
		System.out.println("我是" + name + ", " + "今年" + age + "岁了!");
	}

	void eat() {
		System.out.println("吃饭~");
	}

	static void haha() {
		System.out.println("static态函数 haha()　在执行！");
	}
}

public class Hello {
	public static void main(String[] args) {
		Person p = new Person("张三", 19);
//		Person p1 = new Person("王二麻子", 21);

		Hello ha = new Hello();
		ha.haha();
	}

	void haha() {
		// TODO Auto-generated method stub

	}
}

```




## 1. 基本数据类型

* byte short int long  10
* boolean
* double float   1.5
* char   `a`

## 2. 成员变量和成员函数
1. 成员变量
2. 成员函数
3. static 修饰的　成员变量 表示　该变量属于类　而不是　属于对象
e.g.   Banji.nation = "China";
特点：　可以用类名直接调用，而不需要创建对象
4. static 修饰成员函数  函数属于类
e.g.   
<font color = red>特点：　可以用类名直接调用，而不需要创建对象</font>

**总结：**
	- 非静态的成员变量和函数　需创建对象，由对象来调动
	  p.name;    p.speak();
	- 由 static 修饰的变量，函数．可由类名调动也可由对象调动．
