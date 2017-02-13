/*
   Gingrefel G. Constante  
	Partner's name: Akbar Faqeeri	
   John McGowan
   Section 3, 09/29/2011 
   Lab 6 - Problem 2, CSc 127A, Fall 2011
   
	This program will simulate and generate a roll of a 20 sided die battle engine for a game.

*/


import java.util.Scanner;
import java.util.Random;

public class BattleEngineIf{
  
	public static void main (String [] args){

	Scanner scan = new Scanner(System.in);
	 
		System.out.print("Enter a seed: ");
		
		int seed = scan.nextInt();
		
		Random keyboard = new Random(seed);
	 
	 	int a = keyboard.nextInt(5)+1;
	 	int b = keyboard.nextInt(10)+1;
	 	int c = keyboard.nextInt(15)+1;
	 	int d = keyboard.nextInt(15)+5;
	 	int e = (d*2);
	 	
		if (seed<=1){
	 		System.out.println("You swing and miss!");
		}
		else if ((seed<=2)||(seed<=4)){
		   System.out.println("You stumble and do only " +a+" damage.");
		}
		else if((seed<=5)||(seed<=14)){
		   System.out.println("Normal strike and do only "+b+" damage.");
		}		
		else if((seed<=15)||(seed<=19)){ 
		   System.out.println("Strong strike and do only "+c+" damage.");
		}
	 	else if (seed<=20){
		   System.out.println("Critical strike and do only "+d+" damage.");	 
		}	
		else {
		   System.out.println("Critical strike and do only "+e+" damage.");
	   }
    }//end method main
}//end BattleEngineIf	 