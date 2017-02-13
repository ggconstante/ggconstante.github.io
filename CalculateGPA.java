/*
	Gingrefel G. Constante
	John McGowan
	Section 3, Thursday, noon-01:50pm
	9/18/11
	Assignment 4 - Problem 1,CSc 127A, Fall 2011
	
	This program calculates person's name, weight and height, then prints height in feet, inches and meters, and
	prints weight in pounds and kilograms.   
*/

import java.util.Scanner;
	
	public class CalculateGPA{
		public static void main(String args[])
		{
			
			Scanner scanInput;
			scanInput = new Scanner(System.in);
			System.out.print("Please enter the first number of credits:"); 
			double credits1 = scanInput.nextDouble();
			System.out.print("Please enter the first grade:");
			double grade1 = scanInput.nextDouble(); 
			
			System.out.print("Please enter the second number of credits:");
			double credits2 = scanInput.nextDouble();
			System.out.print("Please enter the second grade:");
			double grade2 = scanInput.nextInt();
			
			System.out.print("Please enter the third number of credits:");
			double credits3 = scanInput.nextInt();
			System.out.print("Please enter the third grade:");
			double grade3 = scanInput.nextInt();
			
			double gradePointAverage = (credits1*grade1 + credits2*grade2 + credits3*grade3)/(credits1+credits2+credits3);
			System.out.print("The GPA is:" +gradePointAverage); 
						
		}
}