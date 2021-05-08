package com.attendanceMonitoring;

import java.io.File;  
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner; 
public class EmpBT {
	private EmployeeNode root, tempNode;
	private ArrayList<EmployeeNode> array;
	
	public EmpBT() {
		root = null;
		tempNode = null;
	}
	private void createArray() {
		array = new ArrayList<EmployeeNode>();
	}
	private EmployeeNode readEmployees(EmployeeNode emp, int id) {
		if(emp == null) {
			tempNode = createNode(id);
			root = tempNode;
			return root;
		}
		if(emp.getId() == id) {
			emp.setEmployeeEnteredCount(emp.getEmployeeEnteredCount()+1);
			return root;
		}
		if(id > emp.getId()) {
			if(emp.getRightNode() == null) {
				tempNode = createNode(id);
				emp.setRightNode(tempNode);
				return root;
			}
			return readEmployees(emp.getRightNode() ,id);
		}
		else {
			if(emp.getLeftNode() == null) {
				tempNode = createNode(id);
				emp.setLeftNode(tempNode);
				return root;
			}
			return readEmployees(emp.getLeftNode(), id);
		}
	}
	private EmployeeNode createNode(int rawIdCasted) {
		EmployeeNode newNode = new EmployeeNode(rawIdCasted, 1, null, null);
		return newNode;
	}
	public void inorderTraversal(EmployeeNode node) {
		if(node != null) {
		inorderTraversal(node.getLeftNode());
		array.add(node);
		inorderTraversal(node.getRightNode());
		}
	}
	public void printData() {
		System.out.print("\nIn Order: ");
		for(int index=0; index<array.size(); index++) {
			System.out.print(array.get(index).getId()+" ");
		}
		System.out.println("\n");
	}
	public EmployeeNode parseDataAndCreateBST(String fileName) {
		try {
			File fileHandler = new File(fileName);
			Scanner scanDocument = new Scanner(fileHandler);
			while(scanDocument.hasNextLine()) {
				String rawId = scanDocument.nextLine();
				int rawIdCasted = Integer.parseInt(rawId);
				root = readEmployees(root, rawIdCasted);
			}
			scanDocument.close();
			createArray();
			inorderTraversal(root);
			printData();
			return root;
		}
		catch(FileNotFoundException exception){
			System.out.println("File Not Found.!");
			
		}	
		return root;
	}
	public int getHeadCount(EmployeeNode emp) {
		if(emp == null) {
			return 0;
		}
		if(emp.getLeftNode() == null && emp.getRightNode() == null) {
			return 1;
		}
		
		return getHeadCount( emp.getLeftNode() ) + getHeadCount( emp.getRightNode() ) + 1;
	}
	boolean searchId(EmployeeNode emp, int id) {
		if(emp.getId() == id) {
			return true;
		}
		if(id > emp.getId()) {
			if(emp.getRightNode() != null) {
				return searchId(emp.getRightNode(), id);
			}
			return false;
			
		}
		else {
			if(emp.getLeftNode() != null) {
				return searchId(emp.getLeftNode(), id);
			}
			return false;
		}
		
	}
	int howOften(EmployeeNode emp, int id) {
		if(emp.getId() == id) {
			return emp.getEmployeeEnteredCount();
		}
		if(id > emp.getId()) {
			if(emp.getRightNode() != null) {
				return howOften(emp.getRightNode(), id);
			}
			return 0;
		}
		else {
			if(emp.getLeftNode() != null) {
				return howOften(emp.getLeftNode(), id);
			}
			return 0;
		}
	}
	
	private int MaxEmpVisitor=0,node;
	void frequentVisitorCalc(EmployeeNode root)
	{
		if (root == null) return;
		if (root != null)
		{
			frequentVisitorCalc(root.getLeftNode());
			if (root.getEmployeeEnteredCount() > MaxEmpVisitor) 
		    {
		        MaxEmpVisitor = root.getEmployeeEnteredCount();
		        node = root.getId();
		    }
			frequentVisitorCalc(root.getRightNode());
		}
	}
	int frequentVisitor(EmployeeNode root)
	{
		frequentVisitorCalc(root);
	    return node;
	}
	
}