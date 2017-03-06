package cn.wk.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
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

		// but.addActionListener(new ActionListener() {
		//
		// @Override
		// public void actionPerformed(ActionEvent e) {
		// tf.setText("按钮被动了一哈");
		// System.out.println("我是acition listener");
		// }
		// });

		// alt shift s
		but.addMouseListener(new MouseAdapter() {
			int count = 0;

			@Override
			public void mouseEntered(MouseEvent e) {
				count++;
				tf.setText("鼠标进入按钮区域了。" + count);
			}

			@Override
			public void mouseExited(MouseEvent e) {
				tf.setText("鼠标   离开了");
			}

			@Override
			public void mouseClicked(MouseEvent e) {
				if (e.getClickCount() == 2) {
					count++;
					tf.setText("被双击..." + count);
				}
			}
		});

		tf.addKeyListener(new KeyAdapter() {

			@Override
			public void keyPressed(KeyEvent e) {
				System.out.println(e.getKeyChar() + "....." + e.getKeyCode());

				int code = e.getKeyCode();
				if (!(code >= KeyEvent.VK_0 && code <= KeyEvent.VK_9)) {
					System.out.println("必须是数字！！");
					// e.consume();
				}

			}

		});

		f.setVisible(true);
	}

	public static void main(String[] args) {
		new MouseListenerDemo();

	}

}
