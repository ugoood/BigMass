package cn.it.gui;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.TextField;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**
 * 鼠标键盘监听示例
 */
public class MouseAndKeyboardDemo {

	private Frame f;
	private TextField tf;
	private Button but;

	// alt shift s
	public MouseAndKeyboardDemo() {
		init();
	}

	private void init() {
		f = new Frame("演示鼠标和键盘监听");
		f.setBounds(400, 200, 500, 400);
		f.setLayout(new FlowLayout());

		tf = new TextField(35);
		but = new Button("一个按钮");
		f.add(tf);
		f.add(but);

		myEvent(); // 添加事件监听

		f.setVisible(true);
	}

	private void myEvent() {

		// 给文本框添加键盘监听
		// 1.确定事件源
		// 2.确定事件和监听器
		// 3.确定具体动作，并把要设定的内容写入该动作所示的方法体

		tf.addKeyListener(new KeyAdapter() {

			@Override
			public void keyPressed(KeyEvent e) {
				// 1. 记录键盘按键
				// System.out.println("keyboard..."+e.getKeyChar()+"..."+e.getKeyCode());
				// 展示shift ^^
				// System.out.println("keyboard..." +
				// KeyEvent.getKeyText(e.getKeyCode()) + "..." +
				// e.getKeyCode());
				//
				// 2. 只认数字，不认别的键，咋办？
				// int code = e.getKeyCode();
				// if(!(code>=KeyEvent.VK_0 && code<=KeyEvent.VK_9)){
				// System.out.println("必须是数字");
				// e.consume(); //不起作用
				// }

				// 3. ctrl + enter 咋办？？
				if (e.isControlDown() && e.getKeyCode() == KeyEvent.VK_ENTER) {
					System.out.println("enter run...");
				}
			}
		});

		// 给Frame对象添加 “关窗体监听”
		f.addWindowListener(new WindowAdapter() {

			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});

		// 鼠标事件：按下，释放，单击，进入 或 离开
		// 要在 按钮上添加一个鼠标监听
		but.addMouseListener(new MouseAdapter() {

			private int count = 1;

			@Override
			public void mouseEntered(MouseEvent e) {
				// System.out.println("我进");
				// tf.setText("我进..." + this.count++);
			}

			@Override
			public void mouseClicked(MouseEvent e) {
				// 双击
				if (e.getClickCount() == 2)
					tf.setText("我点..." + this.count++);
				// System.out.println("click done"+count++);
			}
		});
	}

	public static void main(String[] args) {
		new MouseAndKeyboardDemo();
	}
}
