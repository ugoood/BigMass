package cn.wk.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MouseListenerDemo {

	private Frame f;
	private TextField tf;
	private Button but;

	public MouseListenerDemo() {
		f = new Frame("演示鼠标");
		f.setBounds(400, 200, 500, 400);
		f.setLayout(new FlowLayout());

		tf = new TextField(36);
		f.add(tf);

		but = new Button("我是按钮");
		f.add(but);

		// alt shift s
		f.addWindowListener(new WindowAdapter() {

			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});

		but.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				tf.setText("按钮被动了一哈");
				System.out.println("我是acition listener");
			}
		});
		
		// alt shift s
		but.addMouseListener(new MouseAdapter() {

			@Override
			public void mouseClicked(MouseEvent e) {
				 tf.setText("鼠标单击了按钮");
				 System.out.println("我是 mouse Clicked");
			}
		});
		
		

		f.setVisible(true);
	}

	public static void main(String[] args) {
		new MouseListenerDemo();

	}

}
