/*
	Gingrefel G. Constante
	John McGowan
	9/22/2011
	CSc 127A, Section #3
	
	This program reads in a speed caught by the police and decides "yes/no" for whether it is your b-day.
	If the speed is 60 or less(No Ticket), between 61 and 80(Small Ticket),greater than 80(Big Ticket).     
*/

import java.util.Scanner;

public class CaughtSpeeding
{
	public static void main(String args [])
	{
	Scanner keyboard = new Scanner(System.in); 
	
	System.out.print("Please enter the recorded speed: ");
	int speed = keyboard.nextInt();  
	System.out.print("Is it your birthday? (yes/no): ");
	String word = keyboard.next(); 
	 
	 int a = 60;
	 int b = 82;
	 int c = 100;
	 int d = 82;
	 int e = 80;
	 
	 if ((speed<=a)||(speed<a)){
		System.out.println("No ticket");	 
	 }else if((speed>=d)||(speed>=b)){
	  System.out.println("Small ticket");	
	 }else if (speed<=e){
	  System.out.println("Small ticket");
	 }else if((speed<c)||(speed>c)) {
	  System.out.println("Big Ticket");
	 }
	
	}
}
