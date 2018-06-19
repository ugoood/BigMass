
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [day20 权限系统设计](#day20-权限系统设计)
  * [1. 权限系统设计和分析](#1-权限系统设计和分析)
  * [2. 权限 dao 层的编写](#2-权限-dao-层的编写)

<!-- tocstop -->

Author：相忠良
Email: ugoood@163.com
起始于：June 18, 2018
最后更新日期：June 18, 2018

**声明：本笔记依据传智播客方立勋老师 Java Web 的授课视频内容记录而成，中间加入了自己的理解。**

# day20 权限系统设计
建立 day20 web工程
## 1. 权限系统设计和分析
要做一个权限管理系统，至少涉及四个对象：**Privilege, Resource, Role, User。** 他们的关系大致如下图：
![1](/assets/1_83pbk5qp7.png)
上图涉及到谁应该记住谁，而不应该记住谁的问题。

按上图完成 4 个 bean 的设计，它们都在`cn.wk.domain`包里：

```java
public class Privilege {
	private String id;
	private String name;
	private String description;
// getter setter...
}
```

```java
public class Resource {
	private String id;
	private String uri; // /day20/servlet/Servlet1
	private String description;

	private Privilege privilege; // 资源对应的权限
// getter setter...
```

```java
public class Role {
	private String id;
	private String name;
	private String description;

	private Set<Privilege> privileges = new HashSet(); // 角色对应的权限
// getter setter...
}
```

```java
public class User {
	private String id;
	private String username;
	private String password;
	private String description;

	private Set<Role> roles = new HashSet();
// getter setter...
}
```

再按上图完成数据库表的设计，4个对象（2个多对多关系），故共6个表：

```sql
create database day20;
use day20;

create table privilege
(
	id varchar(40) primary key,
	name varchar(100) not null unique,
	description varchar(255)
);

create table resource
(
	id varchar(40) primary key,
	uri varchar(255) not null unique,
	description varchar(255),
	privilege_id varchar(40),
	constraint privilege_id_FK foreign key(privilege_id) references privilege(id)
  /* 一个权限对应多个资源，是一对多的关系，为了不丢失关系，所以一般要在多的一方定义外键列 */
);

create table role
(
	id varchar(40) primary key,
	name varchar(100) not null unique,
	description varchar(255)
);

create table user
(
	id varchar(40) primary key,
	username varchar(40) not null unique,
	password varchar(40) not null,
	description varchar(255)
);

create table role_privilege  /*多对多表的建立*/
(
	role_id varchar(40),
	privilege_id varchar(40),
	primary key(role_id,privilege_id),
	constraint role_id_FK foreign key(role_id) references role(id),
	constraint privilege_id_FK1 foreign key(privilege_id) references privilege(id)
);

create table user_role
(
	user_id varchar(40),
	role_id varchar(40),
	primary key(user_id,role_id),
	constraint user_id_FK foreign key(user_id) references user(id),
	constraint role_id_FK1 foreign key(role_id) references role(id)
);
```

搭建环境，需导入的 jar 包：
![2](/assets/2_t49nk32pz.png)

src 下弄个`c3p0-config.xml`配置文件：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<c3p0-config>
	<default-config>
		<property name="driverClass">com.mysql.jdbc.Driver</property>
		<property name="jdbcUrl">jdbc:mysql://localhost:3306/day20</property>
		<property name="user">root</property>
		<property name="password">root</property>

		<property name="acquireIncrement">5</property>
		<property name="initialPoolSize">10</property>
		<property name="minPoolSize">5</property>
		<property name="maxPoolSize">20</property>		
	</default-config>

	<named-config name="flx">
		<property name="driverClass">com.mysql.jdbc.Driver</property>
		<property name="jdbcUrl">jdbc:mysql://localhost:3306/day16</property>
		<property name="user">root</property>
		<property name="password">root</property>
		<property name="acquireIncrement">5</property>
		<property name="initialPoolSize">10</property>
		<property name="minPoolSize">5</property>
		<property name="maxPoolSize">20</property>
	</named-config>
</c3p0-config>
```

在`cn.wk.utils.JdbcUtils`中写入：

```java
package cn.wk.utils;
import javax.sql.DataSource;
import com.mchange.v2.c3p0.ComboPooledDataSource;
public class JdbcUtils {
	private static DataSource ds;
	static{ds = new ComboPooledDataSource();}
	public static DataSource getDataSource(){return ds;}
}
```

准备工作到此全部完成。

## 2. 权限 dao 层的编写
以下四种对象的 dao 全都在`cn.wk.dao`包中。

1. 资源 ResourceDao

```java
public class ResourceDao {

	public void add(Resource r) {
		try {
			QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
			String sql = "insert into resource(id,uri,description) values(?,?,?)";
			Object params[] = { r.getId(), r.getUri(), r.getDescription() };
			runner.update(sql, params);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public Resource find(String uri) {
		try {
			QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
			String sql = "select * from resource where uri=?";
			Resource r = (Resource) runner.query(sql, uri, new BeanHandler(
					Resource.class));
			if (r == null)
				return null;

			// 查出资源对应的权限们
			sql = "select p.* from resource r,privilege p where r.uri=? and p.id=r.privilege_id";
			Privilege p = (Privilege) runner.query(sql, uri, new BeanHandler(
					Privilege.class));
			r.setPrivilege(p);
			return r;
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public Resource findById(String id) {
		try {
			QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
			String sql = "select * from resource where id=?";
			Resource r = (Resource) runner.query(sql, id, new BeanHandler(
					Resource.class));
			if (r == null)
				return null;

			// 查出资源对应的权限们
			sql = "select p.* from resource r,privilege p where r.id=? and p.id=r.privilege_id";
			Privilege p = (Privilege) runner.query(sql, id, new BeanHandler(
					Privilege.class));
			r.setPrivilege(p);
			return r;
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public List getAll() {
		try {
			QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
			String sql = "select * from resource";
			List<Resource> list = (List<Resource>) runner.query(sql,
					new BeanListHandler(Resource.class));

			for (Resource r : list) {
				// 查出资源对应的权限们
				sql = "select p.* from resource r,privilege p where r.id=? and p.id=r.privilege_id";
				Privilege p = (Privilege) runner.query(sql, r.getId(),
						new BeanHandler(Privilege.class));
				r.setPrivilege(p);
			}
			return list;
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	// 更新资源 r 的权限为 p
	public void updatePrivilege(Resource r, Privilege p) {
		try {
			QueryRunner runner = new QueryRunner(JdbcUtils.getDataSource());
			String sql = "update resource set privilege_id=? where id=?";
			Object params[] = {p.getId(), r.getId()};
			runner.update(sql, params);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
}
```

2. 权限 PrivilegeDao

```java

```





**continued**
