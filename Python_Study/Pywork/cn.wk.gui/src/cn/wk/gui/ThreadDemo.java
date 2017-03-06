package cn.wk.gui;

public class ThreadDemo {

	public static void main(String[] args) {
		System.out.println("main 开始了");
		Thread1 t1 =new Thread1();
		Thread2 t2 =new Thread2();
		
		t1.start();
		t2.start();
		
		System.out.println("main 结束了");
	}

}

class Thread1 extends Thread {
	public void run() {
		for(int i = 1; i<=1000; i++){
			System.out.println("我是thread1 -->  " + i);
		}
	}
}

class Thread2 extends Thread {
	public void run() {
		for(int i = 1; i<=1000; i++){
			System.out.println("我是thread222222222222 -->  " + i);
		}
	}
}
