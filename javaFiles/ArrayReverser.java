/*

	Name: Gingrefel Constante
	Partner's name: Akbar Faqeeri
	Section leader: John McGowan
	Date: 11/3/2011
	Class: CSc 127A, Section 003
	
	This program will take a number from a user, then read that integers from the keyboard and store them into an 
	array without introducing the second array. After doing this reversed the array. Reversing and printing must
	be two seperate steps. 
	
*/

import java.util.Scanner; 

public class ArrayReverser
{
	
	public static void main(String args[])
	{
	
		Scanner keyboard = new Scanner(System.in);//asking the scanner from the keyboard
			
			System.out.print("Enter the size of the array: ");
			int arrayNum = keyboard.nextInt();
			
			int [] arrayNumber = new int [arrayNum];//declaring and instantiating arrays
			
			//looping for the values of array
			int i;
			for (i = 0; i<arrayNumber.length; i++){ 
			System.out.print("Enter a value: ");
			arrayNumber[i] = keyboard.nextInt();
			}
			
			for (i = arrayNumber.length-1; i>=0; i--)//reversing the order of the array
			System.out.print(arrayNumber[i] + " ");//printing results
					
	 }//end of method main
}//end of ArrayReverser	