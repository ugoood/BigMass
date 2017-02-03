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
