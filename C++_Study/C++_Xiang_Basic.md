# My Stuck in C++
Zhong-Liang Xiang
Oct. 1st, 2017

## 0. 迷之 -> 和 .
箭头（->）：左边必须为指针；
点号（.）：左边必须为实体。
e.g.1　class

```c++
class A{
public:
	play();
};

int main(){
	A a;
	a.play();

	A *p;
	p -> play();
}
```

e.g.2 struct
```c++
struct St{
	int n;
};

int main(){
	St st;
	st.n = 0;

	St *st;
	(*st).n = 1;
	//或者
	st -> n = 1; // -> 简化书写
}
```

## 1. 函数　数组　指针相关
### 1.1 定义并简单使用指针
```int a;```
```int *p; \\定义指针```
```p = &a; \\a地址送指向整形数据的指针变量```

```c++
#include<iostream>
using namespace std;
int main() {
	int a, b;
	int *p, *q;
	p = &a;
	q = &b;

	// 0x7ffde76283c8 0x7ffde76283cc
	cout << p << ' ' << q << endl;
	// 0 0
	cout << *p << ' ' << *q << endl;
}
```
### 1.2 函数－操作数组
函数操作数组，一般不仅要传数组头指针，而且要传数组长度．
```c++
int sum_L(int *, int);
int main() {
	int L[] = { 3, 38, 5, 44, 15, 36, 26,
			27, 2, 46, 4, 19, 47, 48, 50 };
	int length = sizeof(L) / sizeof(L[0]);
	int res = sum_L(L, length);
	cout << res << endl;
	return 0;
}

// A指针只接受整型数据地址,
// 因 L 是 int 型数据地址, A = L　就正确．
int sum_L(int *A, int len) {
	int sum = 0;
	for (int i = 0; i < len; i++)
		sum += *(A + i); //　指针操作数组
	return sum;
}
```
### 1.3 函数参数－指针调用
形式参数为指针，与实际参数指向相同的变量. **修改形参，影响实参**.
```c++
void swap(int *, int *);
int main(){
  int a = 2, b = 3;
  cout << a << ' ' << b << endl;
  swap(&a, &b); // here
  cout << a << ' ' << b << endl;
}

void swap(int *a, int *b){ // here
  int temp;
  temp = *a; *a = *b; *b = temp;
}
```
### 1.4 函数参数－引用调用
<font color = red>形参是实参的别名</font>.
```c++
// 函数声明
void swap(int &x, int &y);

int main() {
	// 局部变量声明
	int a = 100;
	int b = 200;

	cout << "交换前，a 的值：" << a << endl;
	cout << "交换前，b 的值：" << b << endl;

	/* 调用函数来交换值 */
	swap(a, b);

	cout << "交换后，a 的值：" << a << endl;
	cout << "交换后，b 的值：" << b << endl;
	return 0;
}

// 函数定义
void swap(int &x, int &y) {
	int temp;
	temp = x; 	/* 保存地址 x 的值 */
	x = y; 		/* 把 y 赋值给 x */
	y = temp; 	/* 把 x 赋值给 y  */
	return;
}
```
## 2. struct A 和 typedef struct A
### 2.1 struct A
```struct A{}```定义一个名为```struct A```的结构体．
下例定义了```struct A```同时，声明了两个变量（注意：不是类型别名）```varA```, ```pA```.
```c++
struct A{
	int num;
	struct A *next;
}varA, *pA; // 声明了struct A类型的变量varA, 指针变量pA;

int main(){
	struct A a, b;
	a.num = 10;
	b.num = 20;
	// pA = a 不对，a并不像函数名或数组名那样来表地址;
	// 相反，a就是普通变量名．
	pA = &a;
	pA->num; //pA为指针变量，所以 ->，否则为"."
}
```
### 2.2 typedef struct A
```typedef struct A{} a, *a```用来为```struct A```类型起**别名**(注意：**不是起变量名**).
```a```是类型名，```*a```是指向```struct A```类型的指针类型名．
e.g.
```c++
// typedef 为　struct B 类型声明了两个别名：
// BNode　struct B 类型别名;
// Head 能用来声明指向struct B对象的指针类.
#include<iostream>
using namespace std;

typedef struct B{
	int b;
	float f;
}BNode, *Head;

typedef int INT;

int main(){
	INT i = 3;

	BNode bn;
	Head head; //head是指针变量，不需*就可定义，因Head已是指针类型
	head = &bn;
	bn.b = 100;
	head->b = 200; //bn和head在修改同一个对象的b域
	cout << "head->b : " << head->b << endl;
	cout << "bn.b : " << bn.b << endl;
}
```

## 3. vector
### 3.1 Initialization
```c
vector<int> v(10, -1); //10个-1
v.size();
v.empty(); //is empty?
```
### 3.2 2-dim Vector Initialization
声明３行４列的数组

```cpp
const int m = 3, n = 4;
vector<vector<int> > A(m); // 3 rows
for(int i = 0; i < m; i++){
	A[i].resize(n); // 4 cols
}
```

### 3.3 v.back() 和　v.push_back()
v.back() 是 vector 最后一个元素的指针;
v.push_back(element) 从队尾压入一个元素;

### 3.4 v.pop_back()
v.pop_back() 队尾处弹出一个元素.

### 3.5 find() 判断是否存在某元素
vector 判断是否存在某元素:

```cpp
if(find(A.begin(), A.end(), A[i]) != A.end()){
	// 若存在 A[i]
	// find() 返回一个指针
}
```
