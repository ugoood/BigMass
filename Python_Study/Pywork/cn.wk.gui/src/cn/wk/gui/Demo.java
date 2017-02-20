package cn.wk.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class Demo {

	public static void main(String[] args) {
		Frame f = new Frame("My frame");
		f.setBounds(400, 200, 500, 400);
		f.setLayout(new FlowLayout());
		Button but = new Button("退出");
		f.add(but);
		
		f.addWindowListener(new WindowAdapter() {
			
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
			
		});
		
		f.setVisible(true);
		System.out.println("over");

	}

}