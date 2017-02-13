/*
   Name: Gingrefel G. Constante
	Partner's name: Akbar Faqeeri
   Section leader: John McGowan
   Date: 10/06/2011, Section 3 
   Class: Lab 7, CSc 127A, Fall 2011
   
	This program will prompt the user to enter a character and ask for a number within 1 to 80 inclusively, 
	then prints a line of characters. 
*/


import java.util.Scanner;

public class CharacterLine{
  public static void main (String [] args){
  
  
  Scanner keyboard = new Scanner(System.in);
  
  System.out.print("Please enter a character: ");
  String character = keyboard.next();
  System.out.print("Please enter a number: ");
  int number = keyboard.nextInt(); 
  
	
  int times = 0;
  int max = 80;
  if (number < 81 && number > 0) 
		System.out.println("Your line:");
  else if (number >= 81) {
      System.out.println("The number is too large");
		}
  else if  (number <= 0)
	   System.out.println("The number is too small");	 	  
      
  while (times<number && max>number ) {
	   System.out.print(character);
		times++;
	   }	
		 
  }//end of method main
}//end of CharacterLine  