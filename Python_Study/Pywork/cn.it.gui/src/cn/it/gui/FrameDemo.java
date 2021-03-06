package cn.it.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class FrameDemo {
	public static void main(String[] args) {
		// 1. 创建窗体 最初不可见的Frame对象
		Frame f = new Frame("My frame");

		// f.setSize(500, 400); //横轴，纵轴
		// f.setLocation(400, 150); // 窗体出现的位置

		// 2. 设置各种边界，位置，布局
		f.setBounds(400, 200, 500, 400); // 代表上面两句

		f.setLayout(new FlowLayout()); // 设置流式布局

		// 3. 创建并添加组件
		Button but = new Button("一个按钮");
		f.add(but); // 大按钮，Frame对象默认"BorderLayout"

		// CAUSION： addWindowListenr()
		// 请个啥样的保镖？
		f.addWindowListener(new WindowAdapter() {

			@Override
			public void windowClosing(WindowEvent e) {
				// 这很像异常处理，catch(e){}自动接收try{}中引发的异常对象
				System.out.println("closing......" + e);
				System.exit(0); // 关窗体
			}
		});

		// 按钮上加一个监听。
		but.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		// 4. 设置可见
		f.setVisible(true);
		System.out.println("over");
	}
}
