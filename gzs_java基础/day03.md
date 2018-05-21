# IO流

写IO流代码时，必须搞清楚的几件事：
1. 源头，目的地；
2. 确定IO设备；
3. 传输是 字节流 还是 字符流；    字符流 = 字节流 + 编码方式


## 重要的接口和类

字符流的接口
Reader
Writer

字节流的接口
InputStream
OutputStream

若设备是磁盘
FileReader   字符文件输入流
FileWriter   字符文件输出流

FileInputStream   字节文件输入流
FileOutputStream  字节文件输出流

缓冲  (装饰类)
BufferedReader
BufferedWriter

BufferedInputStream
BufferedOutputStream

相关代码：

```java
package gzs_day04;

import java.io.FileReader;
import java.io.FileWriter;

public class IODemo {
	// 传 字符流
	public static void main(String[] args) throws Exception {
		// 1. 定义源头
		FileReader fr = new FileReader("e:\\a.txt");

		// 2. 定义目的地
		FileWriter fw = new FileWriter("e:\\b.txt");

		// 3. 传输
		int b;
		while ((b = fr.read()) != -1) {
			fw.write(b);
			fw.flush();
		}
		// 4. 关流
		fr.close();
		fw.close();
	}
}
```

```java
package gzs_day04;

import java.io.FileInputStream;
import java.io.FileOutputStream;

public class IODemo2 {

	public static void main(String[] args) throws Exception {
		FileInputStream fis = new FileInputStream("e:\\a.jpg");
		FileOutputStream fos = new FileOutputStream("e:\\b.jpg");

		int b;
		while ((b = fis.read()) != -1) {
			fos.write(b);
			fos.flush();
		}
		fis.close();
		fos.close();
	}
}
```

```java
package gzs_day04;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class IODemo3 {

	public static void main(String[] args) throws Exception {
		BufferedInputStream bis = new BufferedInputStream(new FileInputStream(
				"e:\\a.jpg"));
		BufferedOutputStream bos = new BufferedOutputStream(
				new FileOutputStream("e:\\b.jpg"));

		int b;
		while ((b = bis.read()) != -1) {
			bos.write(b);
			bos.flush();
		}
		bis.close();
		bos.close();
	}
}
```

```java
package gzs_day04;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

public class BufferedDemo {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new FileReader("e:\\a.txt"));
		BufferedWriter bw = new BufferedWriter(new FileWriter("e:\\b.txt"));

		String str;
		while ((str = br.readLine()) != null) {
			bw.write(str);
			bw.write(System.getProperty("line.separator"));
			bw.flush();
		}

		br.close();
		bw.close();
	}
}
```
