
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 07 类模板](#chapter-07-类模板)
  * [1. 类模板](#1-类模板)

<!-- tocstop -->


# Chapter 07 类模板
Begin  : 2018.7.18
End	   : 2018.7.18
Author : Xiang
Email  : ugoood@163.com

## 1. 类模板
泛型编程：
* 独立于任何特定类型；
* 模板表达了特定的逻辑结构，和数据类型无关。

1. 函数模板例子：

```cpp {.line-numbers}
#include <iostream>
using namespace::std;

namespace wk{ // 定义命名空间

template<typename T> // 函数模板
T min(T a, T b){
  return (a < b) ? a : b;
}
}

int main(){
  int a = 10, b = 9;
	int c = wk::min(a, b);
	cout << c << endl;

	double aa = 10.0, bb = 9.1;
	double cc = wk::min(aa, bb);
	cout << cc << endl;
  return 0;
}
```

2. 类模板例子：
**<font color=red>类和具体的数据类型已经没有关系了！</font>**
**<font color=blue>模板类</font>** (是类，且是类模板的实例化，就是参数被实际类型替代，但模板类不是对象！)是 **<font color=green>类模板</font>** (是模板，不是类)的实例化。

```cpp {.line-numbers}
// 类模板 Example.h
#ifndef _EXAMPLE_H_
#define _EXAMPLE_H_

namespace wk {

	class Test {}; // 自定义类

	template <typename T> // or <class T> 定义类模板
	class Example {
	public:
		Example(T val) :m_val(val) {}  // <-- 注意 T
		~Example() {}

		void set(T val) {
			m_val = val;
		}

		T get() const {
			return m_val;
		}

	private:
		T m_val;
	};
}

#endif
```

main.cpp代码：

```cpp {.line-numbers}
#include "Example.h"
using namespace std;
#include <iostream>

using namespace wk;

int main(){ // 模板类是类模板的实例化
  Example<int> e(1);  // <-- 1. 注意这 使用类模板时，加 <int>
	int data = e.get();
	cout << data << endl;

	Example<double> ee(1.1); // <-- 2. double
	double d = ee.get();
	cout << d << endl;

	Test t;
	Example<Test> eee(t); // <-- 3. 自定义类型也没问题
}
```

提到类模板的 **特化和偏特化**，用到时再说。
