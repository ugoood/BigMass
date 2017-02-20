package cn.it.gui;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;

import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.io.File;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JScrollPane;

public class MyWindow extends JFrame {

	protected static final String LINE_SEPARATOR = System.getProperty("line.separator");
	private JPanel contentPane;
	private JTextField textField;
	private JButton btnNewButton;
	private JTextArea textArea;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyWindow frame = new MyWindow();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyWindow() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 597, 461);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		textField = new JTextField();
		textField.setBounds(12, 23, 392, 21);
		contentPane.add(textField);
		textField.setColumns(10);

		btnNewButton = new JButton("转到");
		btnNewButton.setBounds(439, 20, 107, 27);
		contentPane.add(btnNewButton);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(12, 80, 534, 309);
		contentPane.add(scrollPane);
		
		textArea = new JTextArea();
		scrollPane.setViewportView(textArea);

		textField.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {

				if (e.getKeyCode() == KeyEvent.VK_ENTER) {
					showDir();
				}
			}
		});

		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				showDir();
			}
		});
	}

	protected void showDir() {
		/*
		 * 通过点击按钮，获取文本框中目录， 将目录中的内容显示在文本区域中。
		 */
		String dir_str = textField.getText();
		File dir = new File(dir_str);

		if (dir.exists() && dir.isDirectory()) {
			// textArea.setText("is directory");
			textArea.setText("");
			String[] names = dir.list();
			for (String name : names) {
				textArea.append(name + LINE_SEPARATOR);
			}
		}
	}
}
