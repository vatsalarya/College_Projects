package com.attendanceMonitoring;

import java.util.Scanner;

public class EmployeeAttendance {
	public static void main(String[] arg) {
		EmpBT binaryTree = null;
		EmployeeNode root = null;
		int option = 0;
		String termination;
		int employeeId;
		Scanner scan = new Scanner(System.in);
		System.out.println("Attendance Monitoring System");
		while(true) {
			System.out.println("\nMenu Options");
			System.out.println("\n1. Import Employee attendance\n"
					+ "2. How many Employees came?\n"
					+ "3. Did a perticular Employee come?\n"
					+ "4. How often did an employee enter?\n"  
					+ "5. Who came in most number of times?\r\n"  
					+ "Note: Option 1 is the first step towards all the other option. Please select the option 1 at the beginning\n");
			option = scan.nextInt();
			switch(option) {
				case 1: binaryTree = new EmpBT();
						root = binaryTree.parseDataAndCreateBST("C:\\\\\\\\Users\\\\\\\\vatsa\\\\\\\\Documents\\\\\\\\ds\\\\\\\\AttendenceMonitorDSAD\\\\\\\\src\\\\\\\\com\\\\\\\\attendanceMonitoring\\\\\\\\input.txt");
						break;
				case 2: System.out.println("Number of employees who came = "+binaryTree.getHeadCount(root)+"\n");
						binaryTree.printData();
						break;
				case 3: System.out.println("Enter the employee Id to search:");
						employeeId = scan.nextInt();
						System.out.println("Search result : "+binaryTree.searchId(root, employeeId));
						binaryTree.printData();
						break;
				case 4: System.out.println("Enter the employee id to check: ");
						employeeId = scan.nextInt();
						System.out.println("Number of times employee entered: "+binaryTree.howOften(root, employeeId));
						binaryTree.printData();
						break;
				case 5: int max = binaryTree.frequentVisitor(root);
						System.out.println("Employees who came most number of times is = " + max);
						binaryTree.printData();
						break;
			}
			System.out.println("Do you want to continue (Type y or n)");
			termination = scan.next();
			if(termination.equals("n"))
				break;
		}
	}
}