package com.attendanceMonitoring;

public class EmployeeNode {
	private int id;
	private int employeeEnteredCount;
	private EmployeeNode leftNode;
	private EmployeeNode rightNode;
	
	public EmployeeNode(int id, int employeeEnteredCount, EmployeeNode leftNode, EmployeeNode rightNode) {
		this.id = id;
		this.employeeEnteredCount = employeeEnteredCount;
		this.leftNode = leftNode;
		this.rightNode = rightNode;
	}

	/**
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * @return the employeeEnteredCount
	 */
	public int getEmployeeEnteredCount() {
		return employeeEnteredCount;
	}

	/**
	 * @param employeeEnteredCount the employeeEnteredCount to set
	 */
	public void setEmployeeEnteredCount(int employeeEnteredCount) {
		this.employeeEnteredCount = employeeEnteredCount;
	}

	/**
	 * @return the leftNode
	 */
	public EmployeeNode getLeftNode() {
		return leftNode;
	}

	/**
	 * @param leftNode the leftNode to set
	 */
	public void setLeftNode(EmployeeNode leftNode) {
		this.leftNode = leftNode;
	}

	/**
	 * @return the rightNode
	 */
	public EmployeeNode getRightNode() {
		return rightNode;
	}

	/**
	 * @param rightNode the rightNode to set
	 */
	public void setRightNode(EmployeeNode rightNode) {
		this.rightNode = rightNode;
	}
	

}