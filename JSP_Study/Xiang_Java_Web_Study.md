Xiang's Java Web Study
===
深度学习研究院_大规模机器学习工程师

>职责要求:
-硕士以上学位
-在以下至少一个领域有深入的研究：
（1）统计机器学习（如深度神经网络、Boosting、图模型、概率统计、最优化方法等）
（2）计算机视觉（如图像识别理解、人脸检测识别、目标检测和跟踪、OCR、增强现实、图像质量评价、图像分割增强等）
（3）语义理解检索 (如知识图谱表示、结构化预测、语义解析、信息检索、知识挖掘等）
-熟悉和掌握C/C++和脚本语言编程(如Shell, Python, Perl等)
-熟悉大规模并行计算的基本原理并具有实现并行计算算法的基本能力
-有机器学习/视觉技术研发/信息检索等相关实践经验者优先
-具有良好的沟通能力，和良好的团队合作精神


# day01
## Break point (BR) in MyEclipse:
> f5: step into
  f6: step over
  f7: step return
  drop to frame: jump to the first line of local method.
  resume: jump to the next BR. It'll finish the hole program if the next BR doesn't exist.
  watch: to watch a variable's value.

BR注意的问题：
1. BR调试完成后， 要在breakpoints视图清除所有断点；
2. BR调试完成后， 一定要记得结束运行断点的jvm。

## Eclipse 快捷键
1. 重置透视图
2. 更改大小写 ctrl+shift+X
3. 查看类继承关系 ctrl+t
4. 查看所有快捷键 ctrl+shift+L

## junit测试框架
java代码正确与否可用junit测试， e.g.
新建Person类：
```java
public class Person {
		public void run(){
		System.out.println("run!!");
	}
		public void eat(){
		System.out.println("eat!!");
	}
}
```
建一个测试类：
```java
import org.junit.Test;
public class Demo1 {
	@Test //想要测试，方法上面写 @Test
	public void testRun() {
		Person p = new Person();
		p.run();
	}
	@Test
	public void testEat(){
		Person p = new Person();
		p.eat();
	}
}
```
用junit运行上面的Demo1测试类。注意，想要测试，要在方法上面写一个**注解** *@Test*

测试代码加上 *@Before* 测试代码之前运行 和 *@After* 测试代码之后运行, 用途看下例：
```java
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class Demo1 {
	private Person p;

	@Before
	public void before() {
		System.out.println("before");
		p = new Person();
	}

	@Test
	public void testRun() {
		p.run();
	}

	@Test
	public void testEat() {
		p.eat();
	}

	@After
	public void after() {
		System.out.println("after");
		p = null;
	}
}
```
运行结果：
```
before
eat!!
after
before
run!!
after
```
而，下面的例子，加了 *@BeforeClass* 和 *@AfterClass* ，注意方法得 **static**:
```java
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class Demo2 {

	@BeforeClass //注意 方法得 static
	public static void beforeClass() {
		System.out.println("beforeClass");
	}

	@Test
	public void testRun() {
		Person p = new Person();
		p.run();
	}

	@Test
	public void testEat() {
		Person p = new Person();
		p.eat();
	}
	@AfterClass //注意 方法得 static
	public static void afterClass() {
		System.out.println("afterClass");
	}
}
```
结果：
```
beforeClass
eat!!
run!!
afterClass
```
结论：*@BeforeClass* 是在测试类**加载**时运行； *@AfterClass* 是在测试类**销毁**时运行。

junit的 *Assert* 类里的方法(有好多，判断各种类型数组是否相等，etc.), 如下：
```java
@Test
public void testRun() {
		//p.run();
		//Assert.assertArrayEquals(new int[] {1,1}, new int[] {1,2}); 返回false
		Assert.assertEquals("1", p.run());  //判断actural值p.run()返回值是否和expected值相同
}
```
同时，得在Person中，把run()修改为：
```java
public String run(){
		System.out.println("run!!");
		return "1";
}
```

## JDK 5.0 新特性  1.0 1.1 1.2 1.3 1.4
* 静态导入
	- e.g. import static java.lang.System.out; import static java.util.Arrays.\*;
* 自动装箱/拆箱
	```java
	Integer i = 1;  //装箱
	int j = i;  //拆箱

	List list =  new ArrayList();
	list.add(1);
	int j = (Integer)list.get(0);
	```
* 增强for循环 (仅能使用在数组和实现了 *iterable* 借口的对象中，如Set, List对象可以，Map不可以)
```java
public class Demo5 {

	@Test
	public void test1() {
		Map map = new LinkedHashMap(); // 有序Map,重要！
		map.put("1", "aaa");
		map.put("2", "bbb");
		map.put("3", "ccc");

		// Traditional method 1: 获得key set
		Set set = map.keySet();
		Iterator it = set.iterator();
		while (it.hasNext()) {
			String key = (String) it.next();
			String value = (String) map.get(key);
			System.out.println(key + " : " + value);
		}
	}

	@Test
	public void test2() {
		Map map = new LinkedHashMap();
		map.put("1", "aaa");
		map.put("2", "bbb");
		map.put("3", "ccc");

		// Traditional method 2: 获得Map Entry, 一个(key, value)的set
		Set set = map.entrySet();
		Iterator it = set.iterator();
		while (it.hasNext()) {
			Map.Entry entry = (Entry) it.next();
			String key = (String) entry.getKey();
			String value = (String) entry.getValue();
			System.out.println(key + " : " + value);
		}
	}

	@Test
	public void test3() {
		Map map = new LinkedHashMap();
		map.put("1", "aaa");
		map.put("2", "bbb");
		map.put("3", "ccc");

		// 增强for访问Map 1 : 获得key set
		for(Object obj : map.keySet()){
			String key = (String) obj;
			String value = (String) map.get(key);
			System.out.println(key + " : " + value);
		}
	}

	@Test
	public void test4() {
		Map map = new LinkedHashMap();
		map.put("1", "aaa");
		map.put("2", "bbb");
		map.put("3", "ccc");

		// 增强for访问Map 2 : 获得Map Entry, 一个(key, value)的set
		for(Object obj : map.entrySet()){
			Map.Entry entry =(Entry) obj;
			String key = (String) entry.getKey();
			String value = (String) entry.getValue();
			System.out.println(key + " : " + value);
		}
	}
}
```
注意，增强for只适合**读**数组数据，不适合修改数组或集合内数据
```java
@Test
	public void test() {
		int[] arr = { 1, 2, 3 };

		for (int i : arr) {
			// arr[i] = 10; 增强for只适合读数组数据，不适合修改数组或集合内数据
			System.out.println(i);
		}

		for (int i = 0; i < arr.length; i++) {
			arr[i] = 10;
			System.out.println(arr[i]);
		}
	}
```
* 可变参数
```java
//可变参数
public class Demo6 {

	@Test
	public void testSum() {
		sum(1, 2, 3, 4, 5, 6);
	}

	public void sum(int... nums) {
		// 把可变参数看成**数组**
		int sum = 0;
		for (int i : nums) {
			sum += i;
		}
		System.out.println("sum = " + sum);
	}

	public void sum1(int j, int... nums) {
		// void sum1(int... nums, int j)这么写不对，
		// 而这样就对int j, int...nums
		int sum = 0;
		for (int i : nums) {
			sum += i;
		}
	}

	@Test
	// 可变参数使用时，要注意的问题：
	// 下面的细节， **要小心**！ Arrays.asList(可传多个对象)，
	// 并且 Arrays.asList()返回一个包含众多对象的数组
	public void bb() {
		int nums[] = { 1, 2, 3, 4, 5 };
		List list = Arrays.asList(nums);
		System.out.println(list);
		// 返回[[I@7c8a5ff0]，意味着把nums看成一个对象
	}

	@Test
	public void bb1() {
		Integer nums[] = { 1, 2, 3, 4, 5 }; // 注意 *Integer*
		List list = Arrays.asList(nums);
		System.out.println(list);
		// 返回[1, 2, 3, 4, 5]，意味着1,2,3,4,5其中的每一个都是对象
	}
}

```
* 枚举 反射 内省
```java
//枚举
public class Demo1 {

	@Test
	public void test() {
		//print(Grade.B);
		print(Grade.A);
	}

	public void print(Grade g) {// 成绩限定在 A B C D E
		String score = g.getValue();
		System.out.println(score);
	}
}

/*class Grade {
	// java 5.0 之前限定ABCDE的方法
	private Grade() {}

	public static final Grade A = new Grade();
	public static final Grade B = new Grade();
	public static final Grade C = new Grade();
	public static final Grade D = new Grade();
	public static final Grade E = new Grade();
}*/

/*enum Grade {// 相当于上面定义的Grade类
	A, B, C, D, E; // 相当于上面的对象
}*/

enum Grade {
	// A("100-90") 相当于 Grade A = new Grade("100-90");
	// 此例表现出，如何用enum的构造函数，方法和字段，封装更多的信息
	A("100-90"), B("89-80"), C("79-70"), D("69-60"), E("59-0");
	private String value;

	private Grade(String value) {
		this.value = value;
	}

	public String getValue() {
		return this.value;
	}
}
```
> day01-10

下例是**带抽象方法**的枚举：
```java
//带抽象方法的枚举
public class Demo2 {

	@Test
	public void test() {
		print(Grade1.A);
	}

	public void print(Grade1 g) {
		String score1 = g.chineseValue();
		String score2 = g.getValue();
		System.out.println(score1 + "..." + score2);
	}
}

enum Grade1 {
	// new 这个A("100-90")对象的同时，需实例化枚举的抽象方法
	A("100-90"){
		public String chineseValue(){
			return "优";
		}
	},

	B("89-80"){
		public String chineseValue(){
			return "良";
		}
	},

	C("79-70"){
		public String chineseValue(){
			return "一般";
		}
	},

	D("69-60"){
		public String chineseValue(){
			return "及格";
		}
	},

	E("59-0"){
		public String chineseValue(){
			return "不及格";
		}
	};
	private String value;

	private Grade1(String value) {
		this.value = value;
	}

	public String getValue() {
		return this.value;
	}

	public abstract String chineseValue(); //抽象方法
}
```
>day01-11

测试枚举的常用方法：
```java
 	@Test
	// 测试枚举的常用方法
	public void test0() {

		// 1. name() ordinal()
		System.out.println(Grade1.C.name()); // 打印C 枚举值
		System.out.println(Grade1.C.ordinal()); // 打印2 枚举值序号

		// 2. valueOf()
		// 下面表现的是： 在什么情况下，要把 “字符串” 转为 “枚举”
		// 查看用户提供的字符串，是否为枚举值
		String str = "B";
		// Grade g = Grade.valueOf(Grade.class, str); //与下行同效
		Grade g = Grade.valueOf(str); // 接收字符串str, 可查看该串是否为枚举值
		System.out.println(g);

		// 3. values() 获取所有枚举值，且返回一个数组
		Grade gd[] = Grade.values();
		for (Grade g1 : gd) { // 遍历gd[]
			System.out.println(g1);
		}
	}
```
>练习：编写一个关于星期几的枚举 WeekDay, 要求：
	* 枚举值： MON TUE WED THU FRI SAT SUN
	* 该枚举要有一个方法，调用该方法返回中文格式的星期

```java
package cn.xiang.enumeration;

import org.junit.Test;

public class Excersize01 {
	@Test
	public void weekDayTest(){
		for(WeekDay wd : WeekDay.values()){
			System.out.println(wd+"..."+wd.cn_show());
		}
	}
}

enum WeekDay{
	MON{
		public String cn_show(){
			return "星期一";
		}
	},
	TUE{
		public String cn_show(){
			return "星期二";
		}
	},
	WED{
		public String cn_show(){
			return "星期三";
		}
	},
	THU{
		public String cn_show(){
			return "星期四";
		}
	},
	FRI{
		public String cn_show(){
			return "星期五";
		}
	},
	FAT{
		public String cn_show(){
			return "星期六";
		}
	},
	SUN{
		public String cn_show(){
			return "星期天";
		}
	};

	public abstract String cn_show();
}
```
**反射**：就是<font color=blue>加载类</font>，并<font color=blue>解剖出类的各个组成部分</font>
加载类，获得类的字节码，三种方式:
```java
//已经建好了Person类
public class Demo1 {
	/**
	 * 反射： 加载类，获得类的字节码，三种方式
	 * @throws ClassNotFoundException
	 * */
	public static void main(String[] args) throws ClassNotFoundException {
		//1. //这方法怎么不行？
		Class clazz = Class.forName("/day01/src/cn/xiang/reflection/Person");
		//2.
		Class clazz1 = new Person().getClass();
		//3.
		Class clazz2 = Person.class;
	}
}
```
> day01-13

向Person类添加了内容，然后用反射抽取构造器再创建对象
```java
public class Person {

	public String name = "aaaa";

	public Person(){
		System.out.println("person");
	}

	public Person(String name){
		System.out.println("Person name");
	}

	public Person(String name, int password){
		System.out.println("Person name & password");
	}

	private Person(List list){
		System.out.println("list");
	}
}
```
```java
//解剖（反射）类的构造函数，创建类的对象
public class Demo2 {
	@Test
	// 反射构造函数： public Person()
	public void test1() {//需抛 各种 异常

		//Class clazz = Class.forName("/day01/src/cn/xiang/reflection/Person"); // 获取类, doesn't work
		//Class clazz = Class.forName("day01.src.cn.xiang.reflection.Person"); // 获取类, doesn't work
		Class clazz = new Person().getClass();
		Constructor c = clazz.getConstructor(null); // 得到Person类的空参Constructor
		Person p = (Person) c.newInstance(null); // 用该构造器创建一个对象

		System.out.println(p.name);
	}
}
```
反射构造函数： public Person(String name)
```java
@Test
	// 反射构造函数： public Person(String name)
	public void test2() throws Exception {
		Class clazz = new Person().getClass();
		// 注意，String.class 这是获得了参数为String类型的构造器
		Constructor c = clazz.getConstructor(String.class);
		Person p = (Person) c.newInstance("xiaoqiang");
		System.out.println(p.name);
	}
```

其他各种反射构造函数，e.g.

```java
// 创建对象的另外一种途径 等效于反射构造函数： public Person()
	@Test
	public void test5() throws Exception {
		Class clazz = Class.forName("cn.xiang.reflection.Person");
		// 调用空参构造函数
		Person p = (Person) clazz.newInstance();
		System.out.println(p.name);
	}

	@Test
	// private Person(List list)
	// 问：private 的东西别的类能访问吗？
	// 答：不能，但是 反射 可访问，既， 用 setAccessible()暴力反射 技术
	// 现实生活的类比： 不能杀人， 但满大街可以买菜刀。 留了后门。
	public void test4() throws Exception {
		Class clazz = Class.forName("cn.xiang.reflection.Person");
		Constructor c = clazz.getDeclaredConstructor(List.class);
		c.setAccessible(true); // 暴力反射
		Person p = (Person) c.newInstance(new ArrayList());
		System.out.println(p.name);
	}

	@Test
	// public Person(String name, int password)
	public void test3() throws Exception {
		Class clazz = Class.forName("cn.xiang.reflection.Person");
		Constructor c = clazz.getConstructor(String.class, int.class);
		Person p = (Person) c.newInstance("wangcai", 5);
		System.out.println(p.name + "..." + p.age);
	}
```



* 泛型
* 元数据
