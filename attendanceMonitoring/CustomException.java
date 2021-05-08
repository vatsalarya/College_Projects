/**
 * 
 */
package com.attendanceMonitoring;


public class CustomException extends Throwable {
	private String message;
	
	public CustomException(String message) {
		this.message = message;
	}
	public String getMessage() {
		return this.message;
	}

}
