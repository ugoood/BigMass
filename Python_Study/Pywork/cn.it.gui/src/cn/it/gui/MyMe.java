package cn.it.gui;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;

public class MyMe extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyMe frame = new MyMe();
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
	public MyMe() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu mnFile = new JMenu("file");
		menuBar.add(mnFile);
		
		JMenuItem mntmFile = new JMenuItem("file1");
		mnFile.add(mntmFile);
		
		JMenuItem mntmFile_1 = new JMenuItem("file2");
		mnFile.add(mntmFile_1);
		
		JMenu mnXxx = new JMenu("xxx");
		menuBar.add(mnXxx);
		
		JMenuItem mntmXxx_2 = new JMenuItem("xxx0");
		mnXxx.add(mntmXxx_2);
		
		JMenuItem mntmXxx = new JMenuItem("xxx1");
		mnXxx.add(mntmXxx);
		
		JMenuItem mntmXxx_1 = new JMenuItem("xxx2");
		mnXxx.add(mntmXxx_1);
		
		JMenu mnUuu = new JMenu("uuu");
		menuBar.add(mnUuu);
		
		JMenuItem mntmUuu = new JMenuItem("uuu1");
		mnUuu.add(mntmUuu);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
	}

}
