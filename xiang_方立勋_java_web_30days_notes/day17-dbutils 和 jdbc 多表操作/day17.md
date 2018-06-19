
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day17 dbutils 和 jdbc 多表操作](#day17-dbutils-和-jdbc-多表操作)
  * [1. dbutils 框架简化 jdbc 开发](#1-dbutils-框架简化-jdbc-开发)
    * [1.1 ResultSetHandler 接口的实现类](#11-resultsethandler-接口的实现类)
  * [2. 用 dbutils 进行事务管理](#2-用-dbutils-进行事务管理)
    * [2.1 正常开发中的转账实现](#21-正常开发中的转账实现)
    * [2.2 ThreadLocal - 线程范围内共享数据](#22-threadlocal-线程范围内共享数据)
  * [3. jdbc 多表操作(1:n)](#3-jdbc-多表操作1n)
    * [3.1 jdbc 多表操作 - 级联](#31-jdbc-多表操作-级联)
  * [4. jdbc 多表操作(n:m)](#4-jdbc-多表操作nm)
  * [5. web 树](#5-web-树)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：June 12, 2018
最后更新日期：June 15, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。本笔记目的是强化自己学习所用。若有疏漏或不当之处，请在评论区指出。谢谢。**
**涉及的图片，文档写完后，一次性更新。**

# day17 dbutils 和 jdbc 多表操作
## 1. dbutils 框架简化 jdbc 开发
commons-dbutils 是 Apache 组织提供的一个开源 JDBC工具类库，它是对JDBC的简单封装，学习成本极低，并且使用dbutils能极大简化jdbc编码的工作量，同时也不会影响程序的性能。因此dbutils成为很多不喜欢hibernate的公司的首选。

API介绍：
* `org.apache.commons.dbutils.QueryRunner`提供了 update(增删改) 和 query(查询)
* `org.apache.commons.dbutils.ResultSetHandler`

工具类
* `org.apache.commons.dbutils.DbUtils`   

本节工程准备：
1. 建立 day17 java 工程；
2. 建立 lib，导入 jar 包并变奶瓶：`mysql-connector-java-5.0.8-bin.jar commons-dbcp-1.2.2.jar commons-pool.jar commons-dbutils-1.2.jar`；
3. src下建立`dbcpconfig.properties`(该配置文件内容下面有)供创建连接池的工具 dbcp 所使用。
4. 创建`cn.wk.utils.JdbcUtils`用来创建连接池。

dbcpconfig.properties如下:

```
driverClassName=com.mysql.jdbc.Driver
url=jdbc\:mysql\://localhost\:3306/day17
username=root
password=root

initialSize=10
maxActive=50
maxIdle=20
minIdle=5
maxWait=60000
connectionProperties=useUnicode=true;characterEncoding=utf8
defaultAutoCommit=true
defaultReadOnly=
defaultTransactionIsolation=READ_COMMITTED
```

`cn.wk.utils.JdbcUtils`创建连接池的工具类如下：

```java
package cn.wk.utils;
import java.io.InputStream;
import java.util.Properties;
import javax.sql.DataSource;
import org.apache.commons.dbcp.BasicDataSourceFactory;

public class JdbcUtils {
	// 创建连接池
	private static DataSource ds;
	static {
		try {
			Properties prop = new Properties();
			InputStream in = JdbcUtils.class.getClassLoader()
					.getResourceAsStream("dbcpconfig.properties");
			prop.load(in);

			BasicDataSourceFactory factory = new BasicDataSourceFactory();
			ds = factory.createDataSource(prop);
		} catch (Exception e) {
			throw new ExceptionInInitializerError(e);
		}
	}

	public static DataSource getDataSource(){return ds;}
	// dbutils 框架会自动帮我们释放链接，所以不用写 release 方法
}
```

day17工程到此已完全准备妥当，开始下面的实验啦。
为模拟将数据库取出的user数据封装到bean中，所以先建一个`cn.wk.domain.User`，如下：

```java
package cn.wk.domain;
import java.util.Date;

public class User {
	private int id;
	private String name;
	private String password;
	private String email;
	private Date birthday;
  // 后面的getter和setter方法省略
}
```

用 dbutils 完成 crud 的例子：

```java
package cn.wk.dbutils.demo;

import java.sql.SQLException;
import java.util.Date;
import java.util.List;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.junit.Test;

import cn.wk.domain.User;
import cn.wk.utils.JdbcUtils;

public class Demo1 {

	/*
	  create database day17;
	  use day17;
	  create table users(
	  	id int primary key,
	  	name varchar(40),
	  	password varchar(40),
	  	email varchar(60),
	  	birthday date
	  );
	 */

	// 使用 dbtuils 完成数据库的 crud

	@Test
	public void insert() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "insert into users(id,name,password,email,birthday) values(?,?,?,?,?)";
		Object params[] = { 2, "bbb", "123", "aa@gmail.com", new Date() };
		runner.update(sql, params);
	}

	@Test
	public void update() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "update users set email=? where id=?";
		Object params[] = { "aaaaaa@163.com", 1 };
		runner.update(sql, params);
	}

	@Test
	public void delete() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "delete from users where id=?";
		runner.update(sql, 1);
	}

	@Test
	public void find() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "select * from users where id=?";
		User user = (User) runner.query(sql, 1, new BeanHandler(User.class));
		System.out.println(user.getEmail());
	}

	@Test
	public void getAll() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "select * from users";
		List list = (List) runner.query(sql, new BeanListHandler(User.class));
		System.out.println(list);
	}

	@Test
	// 用 dbutils 作批处理
	public void batch() throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "insert into users(id,name,password,email,birthday) values(?,?,?,?,?)";
		Object params[][] = new Object[3][5];
		for (int i = 0; i < params.length; i++) { // 3条记录
			params[i] = new Object[] { i + 1, "aa" + i, "123", i + "@sina.com",
					new Date() };
		}
		runner.batch(sql, params);
	}
}
```

### 1.1 ResultSetHandler 接口的实现类
ResultSetHandler 接口的实现类：
* ArrayHandler：把结果集中的第一行数据转成对象数组；
* ArrayListHandler：把结果集中的每一行数据都转成一个数组，再存放到List中；
* BeanHandler：将结果集中的第一行数据封装到一个对应的JavaBean实例中；
* BeanListHandler：将结果集中的每一行数据都封装到一个对应的JavaBean实例中，存放到List里；
* ColumnListHandler：将结果集中某一列的数据存放到List中；
* KeyedHandler(name)：将结果集中的每一行数据都封装到一个Map里，再把这些map再存到一个map里，其key为指定的key；
* MapHandler：将结果集中的第一行数据封装到一个Map里，key是列名，value就是对应的值；
* MapListHandler：将结果集中的每一行数据都封装到一个Map里，然后再存放到List；
* ScalarHandler：将结果集的某列转成一个对象(标量)。

## 2. 用 dbutils 进行事务管理
准备：
把一下sql语句在day17数据库中执行。

```sql
create table account(
	id int primary key auto_increment,
	name varchar(40),
	money float
)character set utf8 collate utf8_general_ci;

insert into account(name,money) values('aaa',1000);
insert into account(name,money) values('bbb',1000);
insert into account(name,money) values('ccc',1000);
```

使用 dbutils 管理事务的完整案例代码：

JdbcUtils 增加了 getConnection() 方法，如下：

```java
public class JdbcUtils {
	// 创建连接池
	private static DataSource ds;
	static {
		try {
			Properties prop = new Properties();
			InputStream in = JdbcUtils.class.getClassLoader()
					.getResourceAsStream("dbcpconfig.properties");
			prop.load(in);

			BasicDataSourceFactory factory = new BasicDataSourceFactory();
			ds = factory.createDataSource(prop);
		} catch (Exception e) {throw new ExceptionInInitializerError(e);}
	}

	public static DataSource getDataSource() {
		return ds;
	}

	// dbutils 框架会自动帮我们释放链接，所以不用写 release 方法

	public static Connection getConnection() throws SQLException {
		return ds.getConnection();
	}
}
```

dbutils 管理事务例子：

```java
public class AccountDao {
	// 从 a-->b账户 转100元
	public void transfer() throws SQLException {

		Connection conn = null;
		try {
			conn = JdbcUtils.getConnection();
			conn.setAutoCommit(false); // 设置开启事务

			QueryRunner runner = new QueryRunner();

			String sql1 = "update account set money=money-100 where name='aaa'";
			runner.update(conn, sql1); // 用开启了事务的 conn 去执行 sql

			String sql2 = "update account set money=money+100 where name='bbb'";
			runner.update(conn, sql2);

			conn.commit();
		} finally {if (conn != null) conn.close();}
	}
}
```

但 dao 层不应有上述这样的 transfer 方法(包含了业务逻辑，违背了mvc)，dao 应只有增删改查。下节介绍正常开发中怎样做转账。

### 2.1 正常开发中的转账实现
先弄个 Account 的 bean：

```java
package cn.wk.domain;
public class Account {
	private int id;
	private String name;
	private double money;
// getter,setter省略
}
```

AccountDao 加上下面2方法：

```java
public class AccountDao {
	public AccountDao() {super();}

	private Connection conn;

	public AccountDao(Connection conn) { // 由外界提供统一的一个 conn
		this.conn = conn;
	}

	public void update(Account a) {
		try {
			QueryRunner runner = new QueryRunner();
			String sql = "update account set money=? where id=?";
			Object params[] = { a.getMoney(), a.getId() };
			runner.update(conn, sql, params);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public Account find(int id) {
		try {
			QueryRunner runner = new QueryRunner();
			String sql = "select * from account where id=?";
			return (Account) runner.query(conn, sql, id, new BeanHandler(
					Account.class));
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
}
```

`cn.wk.service.BusinessService`对 web 层提供转账服务：

```java
public class BusinessService {

	@Test
	public void test() throws SQLException {
		transfer(1, 2, 100);
	}

	public void transfer(int sourceid, int targetid, double money)
			throws SQLException {

		Connection conn = null;
		try {
			conn = JdbcUtils.getConnection();
			conn.setAutoCommit(false); 		// 开启事务

			AccountDao dao = new AccountDao(conn); // <-- 把 conn 传进去啦

			Account a = dao.find(sourceid); // select
			Account b = dao.find(targetid); // select

			a.setMoney(a.getMoney() - money);
			b.setMoney(b.getMoney() + money);

			dao.update(a); 					// update
//			int aa = 1/0;
			dao.update(b); 					// update 得作为整体执行

			conn.commit(); 					// 提交事务
		} finally {if (conn != null) conn.close();}
	}
}
```

**<font color=red>service 层只有这样写，才保证转账操作用的是同一个 connection 并用事务去完成！
同时注意到 dao 层已经被改造，dao 层通过有参构造函数，传入了一个 service 层提供的一个已经开启了事务的 connection！</font>**

### 2.2 ThreadLocal - 线程范围内共享数据

方立勋老师叨叨了半天，竟说上面的方法不优雅~！！！
他说优雅的解决方式是用spring或 ThreadLocal 类去解决。

**ThreadLocal 的使用可以使我们在线程范围内共享数据。**

**ThreadLocal 就是一个 key = thread 的 map 容器。**

接下来，才是这伙计讲的重点，我的天啊~！ (略...)

## 3. jdbc 多表操作(1:n)
准备2个bean，如下：

```java
package cn.wk.domain;
public class Department {
	private String id;
	private String name;
	private Set employees = new HashSet(); //看是否有显示需求，若无则删除这个
// getter setter...
}
```

```java
package cn.wk.domain;
public class Employee {
	private String id;
	private String name;
	private double salary;
	private String department_id;
  // getter setter...
}
```

数据库创建2表：

```sql
use day17;
create table department(
  id varchar(40) primary key,
  name varchar(40)
);

create table employee(
  id varchar(40) primary key,
  name varchar(40),
  salary double,
  department_id varchar(40),
  constraint department_id_FK foreign key(department_id) references department(id)
);
```

多表查询的一个dao:

```java
public class DepartmentDao {

	public void add(Department d) throws SQLException {
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());

		// 1. 把 department 对象插入 department 表
		String sql = "insert into department(id,name) values(?,?)";
		Object params[] = { d.getId(), d.getName() };
		runner.update(sql, params);

		// 2. 把department 对象中的员工们插入到 employee 表
		Set<Employee> set = d.getEmployees();
		for (Employee e : set) {
			sql = "insert into employee(id,name,salary,department_id) values(?,?,?,?)";
			params = new Object[] { e.getId(), e.getName(), e.getSalary(),
					d.getId() };
			runner.update(sql, params);
		}
	}

	public Department find(String id) throws SQLException{		
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());

		//1.找部门表，查出部门的基本信息
		String sql = "select * from department where id=?";
		Department d = (Department) runner.query(sql, id, new BeanHandler(Department.class));

		//2.找员工表，找出部门下面所有员工
		sql = "select * from employee where department_id=?";
		List list = (List) runner.query(sql, id, new BeanListHandler(Employee.class));		

		d.getEmployees().addAll(list);		
		return d;
	}
}
```

多表查询的测试：

```java
public class BService {
	@Test
	public void add() throws SQLException{		

		Department d = new Department();
		d.setId("1");
		d.setName("开发部");

		Employee e1 = new Employee();
		e1.setId("1");
		e1.setName("aa");
		e1.setSalary(10000);

		Employee e2 = new Employee();
		e2.setId("2");
		e2.setName("bb");
		e2.setSalary(10000);


		d.getEmployees().add(e1);
		d.getEmployees().add(e2);

		DepartmentDao dao = new DepartmentDao();
		dao.add(d);
	}

	@Test
	public void find() throws SQLException{
		DepartmentDao dao  = new DepartmentDao();
		Department d = dao.find("1");
		System.out.println(d);
	}
}
```

方立勋说：1对多能不用就不用。因为若1中记多，太多了内存崩。
需求让你1必须记住多，那就得设计，否则不必设计。
例如：订单必须显示订单项，但部门不显示员工。

### 3.1 jdbc 多表操作 - 级联
级联删除有好几种呢。
* 删部门表记录，对应员工部门号清空 on delete set null；
* 删部门表记录，也删除对应员工 on delete cascade；
* 还有，用时再查。

```sql
create table employee(
  id varchar(40) primary key,
  name varchar(40),
  salary double,
  department_id varchar(40),
  constraint department_id_FK foreign key(department_id) references department(id)  
);

// 修改员工表的外键约束

alter table employee drop foreign key department_id_FK;
alter table employee add constraint department_id_FK foreign key(department_id) references department(id) on delete set null;
```

dao的删除方法

```java
public void delete(String id) throws SQLException{
  QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
  String sql = "delete from department where id=?";
  runner.update(sql, id);
}
```

级联删除测试：

```java
@Test
public void delete() throws SQLException{
  DepartmentDao dao  = new DepartmentDao();
  dao.delete("1");
}
```

## 4. jdbc 多表操作(n:m)
准备老师和学生bean和表，他们是 n:m 的关系。

```java
public class Student {
	private String id;
	private String name;
	private Set teachers = new HashSet();
  // getter setter...
}
```

```java
public class Teacher {
	private String id;
	private String name;
	private double salary;
	private Set students = new HashSet();
  // getter setter...
}
```

数据库生3表：

```sql
use day17;
create table teacher(
  id varchar(40) primary key,
  name varchar(40),
  salary double
);

create table student(
  id varchar(40) primary key,
  name varchar(40)
);

create table teacher_student(
  teacher_id varchar(40),
  student_id varchar(40),
  primary key(teacher_id,student_id),
  constraint teacher_id_FK foreign key(teacher_id) references teacher(id),
  constraint student_id_FK foreign key(student_id) references student(id)
);
```

操作多表dao：

```java
public class TeacherDao {

public void add(Teacher t) throws SQLException {

		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());

		//1`.取出老师存老师表
		String sql = "insert into teacher(id,name,salary) values(?,?,?)";
		Object params[] = {t.getId(),t.getName(),t.getSalary()};
		runner.update(sql, params);


		//2.取出老师所有学生的数据，存学生表
		Set<Student> set = t.getStudents();
		for(Student s : set){
			sql = "insert into student(id,name) values(?,?)";
			params = new Object[]{s.getId(),s.getName()};
			runner.update(sql, params);

			//3.更新中间表，说明老师和学生的关系
			sql = "insert into teacher_student(teacher_id,student_id) values(?,?)";
			params = new Object[]{t.getId(),s.getId()};
			runner.update(sql, params);
		}
	}

	public Teacher find(String id) throws SQLException{

		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());

		//1.找老师表，找出老师的基本信息
		String sql = "select * from teacher where id=?";
		Teacher t = (Teacher) runner.query(sql, id, new BeanHandler(Teacher.class));

		//2.找出老师的所有学生
		sql = "select s.* from teacher_student ts,student s where ts.teacher_id=? and ts.student_id=s.id";
		List list = (List) runner.query(sql, id, new BeanListHandler(Student.class));

		t.getStudents().addAll(list);
		return t;
	}

	public void delete(String id){
		QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
		String sql = "delete from teacher where id=?";
		// 未完成
	}
}
```

测试：

```java
@Test
public void addTeacher() throws SQLException {
  Teacher t = new Teacher();
  t.setId("1");
  t.setName("二麻子");
  t.setSalary(100000);

  Student s1 = new Student();
  s1.setId("1");
  s1.setName("aa");

  Student s2 = new Student();
  s2.setId("2");
  s2.setName("bb");

  t.getStudents().add(s1);
  t.getStudents().add(s2);

  TeacherDao dao = new TeacherDao();
  dao.add(t);
}

@Test
public void findTeacher() throws SQLException{
  TeacherDao dao = new TeacherDao();
  Teacher t = dao.find("1");
  System.out.println(t);
}
```

## 5. web 树
无限级分类树，通过树状数据结构设计，建了个数据库表，从而避免了递归。
剩下内容略。
