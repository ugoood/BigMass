IntelliJ IDEA maven库下载依赖包速度慢的问题
===
https://www.jianshu.com/p/361ea9235ca5

date: 2018.6.23

右键项目选中 maven 选项，然后选择 “open settings.xml” 或者 “create settings.xml”，然后把如下代码粘贴到`<mirrors>`所指定标签里就可以了。重启IDE，感受速度飞起来的感觉吧！！！

```xml
<mirrors>

    <mirror>
        <id>alimaven</id>
        <name>aliyun maven</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
        <mirrorOf>central</mirrorOf>
    </mirror>

    <mirror>
        <id>uk</id>
        <mirrorOf>central</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://uk.maven.org/maven2/</url>
    </mirror>

    <mirror>
        <id>CN</id>
        <name>OSChina Central</name>
        <url>http://maven.oschina.net/content/groups/public/</url>
        <mirrorOf>central</mirrorOf>
    </mirror>

    <mirror>
        <id>nexus</id>
        <name>internal nexus repository</name>
        <!-- <url>http://192.168.1.100:8081/nexus/content/groups/public/</url>-->
        <url>http://repo.maven.apache.org/maven2</url>
        <mirrorOf>central</mirrorOf>
    </mirror>

</mirrors>
```
