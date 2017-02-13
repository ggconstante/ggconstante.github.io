/*
   Gingrefel G. Constante  
	Partner's name: Akbar Faqeeri	
   John McGowan
   Section 3, 09/29/2011 
   Lab 6 - Problem 1, CSc 127A, Fall 2011
   
	This program will simulate and generate a roll of a 20 sided die battle engine for a game.

*/


import java.util.Scanner;
import java.util.Random;

public class BattleEngineCase{
  
	public static void main (String [] args){

	Scanner scan=new Scanner(System.in);
	 
		System.out.print("Enter a seed: ");
		
		int seed=scan.nextInt();
		
		Random keyboard=new Random(seed);
	 
	 	int a = keyboard.nextInt(5)+1;
	 	int b = keyboard.nextInt(10)+1;
	 	int c = keyboard.nextInt(15)+1;
	 	int d = keyboard.nextInt(15)+5;
	 	int e = (d*2);
	 	
		switch (seed){
	 		case 0:
			case 1:
				System.out.println("You swing and miss!");
				break; 
	   	case 2:
			case 3:
			case 4:
		   	System.out.println("You stumble and do only " +a+" damage.");
				break;
			case 5:
			case 6:
			case 7:
			case 8:
			case 9:
			case 10:
			case 11:
			case 12:
			case 13:
			case 14:
		   	System.out.println("Normal strike and do only "+b+" damage.");
				break;
			case 15:
			case 16:
			case 17:
			case 18:
			case 19: 
		   	System.out.println("Strong strike and do only "+c+" damage.");
				break;
			case 20:
		   	System.out.println("Critical strike and do only "+d+" damage.");	 
				break;	
			default:
		   	System.out.println("Critical strike and do only "+e+" damage.");
	   }
    }//end method main
}//end of BattleEngineCase	 