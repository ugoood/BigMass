package cn.wk.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class FrameDemo {

	public static void main(String[] args) {
		Frame f = new Frame("我的窗体");
		f.setBounds(400, 150, 400, 300);
		f.setLayout(new FlowLayout());
				
		Button but = new Button("退出");
		f.add(but);
		
		//alt shift s
	
		f.addWindowListener(new WindowAdapter() {

			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
			
		});		
				
		but.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
				
		f.setVisible(true);
		System.out.println("over");

	}

}
