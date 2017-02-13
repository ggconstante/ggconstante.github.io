/*

	Gingrefel Constante
	John McGowan
	Section 3, Thursday,noon=01:50pm
	Jesse Bright, Section 4
	Assignment 5 - Problem #1,CSc 127A, Fall 2011
	
	 This program deals three cards from a standard 52-card deck cards. The three cards
	 are determmined randomly. The program will report if two , or three, of the cards are the same.
	 
*/
import java.util.Random;
import java.util.Scanner;
public class Cards
{
	public static void main(String [] args)
	{
	Scanner input = new Scanner(System.in);//making the scanner read from the keyboard
 
	System.out.print("Enter a random seed: ");
	int seed = input.nextInt(); 
	
	Random keyboard = new Random(seed); 
	
	int card1 = keyboard.nextInt(52);
	int card2 = keyboard.nextInt(52);
	int card3 = keyboard.nextInt(52);
	
	String cardDeck1 = "";
	
	if ((card1 == 0) || (card1 == 13) || (card1 == 26) || (card1 == 39))
	   cardDeck1 = "Ace";
	else if ((card1 == 1) || (card1 == 14) || (card1 == 27) || (card1 == 40))
		cardDeck1 = "2";
	else if ((card1 == 2) || (card1 == 15) || (card1 == 28) || (card1 == 41))
		cardDeck1 = "3";
	else if ((card1 == 3) || (card1 == 16) || (card1 == 29) || (card1 == 42))
		cardDeck1 = "4";
	else if ((card1 == 4) || (card1 == 17) || (card1 == 30) || (card1 == 43))
		cardDeck1 = "5";
	else if ((card1 == 5) || (card1 == 18)  || (card1 == 31) || (card1 == 44))
		cardDeck1 = "6";
	else if ((card1 == 6) || (card1 == 19) || (card1 == 32) || (card1 == 45))
		cardDeck1 = "7";
	else if ((card1 == 7) || (card1 == 20) || (card1 == 33) || (card1 == 46))
		cardDeck1 = "8";
	else if ((card1 == 8) || (card1 == 21) || (card1 == 34) || (card1 == 47))
		cardDeck1 = "9";
	else if ((card1 == 9) || (card1 == 22) || (card1 == 35) || (card1 == 48))
		cardDeck1 = "10";
	else if ((card1 == 10) || (card1 == 23) || (card1 == 36) || (card1 == 49))
		cardDeck1 = "Jack";
	else if ((card1 == 11) || (card1 == 24) || (card1 == 37) || (card1 == 50))
		cardDeck1 = "Queen";
	else if ((card1 == 12) || (card1 == 25) || (card1 == 38) || card1 == 51)
		cardDeck1 = "King";
	
	String type1 = "";
	if ((card1>=0)&& (card1<=12))
	 type1 = "Hearts";
	else if ((card1>=13) && (card1<=25))
	 type1 = "Clubs";
	else if ((card1>=26) && (card1<=38))
	 type1 = "Diamonds";
	else if ((card1>=39))
	 type1 = "Spades";
	
	String cardDeck2 = "";
	
	if ((card2 == 0) || (card2 == 13) || (card2 == 26) || (card2 == 39))
		cardDeck2 = "Ace";
	else if ((card2 == 1) || (card2 == 14) || (card2 == 27) || (card2 == 40))
		cardDeck2 = "2";
	else if ((card2 == 2) || (card2 == 15) || (card2 == 28) || (card2 == 41))
		cardDeck2 = "3";
	else if ((card2 == 3) || (card2 == 16) || (card2 == 29) || (card2 == 42))
		cardDeck2 = "4";
	else if ((card2 == 4) || (card2 == 17) || (card2 == 30) || (card2 == 43))
		cardDeck2 = "5";
	else if ((card2 == 5) || (card2 == 18)  || (card2 == 31) || (card2 == 44))
		cardDeck2 = "6";
	else if ((card2 == 6) || (card2 == 19) || (card2 == 32) || (card2 == 45))
		cardDeck2 = "7";
	else if ((card2 == 7) || (card2 == 20) || (card2 == 33) || (card2 == 46))
		cardDeck2 = "8";
	else if ((card2 == 8) || (card2 == 21) || (card2 == 34) || (card2 == 47))
		cardDeck2 = "9";
	else if ((card2 == 9) || (card2 == 22) || (card2 == 35) || (card2 == 48))
		cardDeck2 = "10";
	else if ((card2 == 10) || (card2 == 23) || (card2 == 36) || (card2 == 49))
		cardDeck2 = "Jack";
	else if ((card2 == 11) || (card2 == 24) || (card2 == 37) || (card2 == 50))
		cardDeck2 = "Queen";
	else if ((card2 == 12) || (card2 == 25) || (card2 == 38) || (card2 == 51))
		cardDeck2 = "King";
	
	String type2 = "";
	if ((card2>=0) && (card2<=12))
	 type2 = "Hearts";
	else if ((card2>=13) && (card2<=25))
	 type2 = "Clubs";
	else if ((card2>=26) && (card2<=38))
	 type2 = "Diamonds";
	else if (card2>=39)
	 type2 = "Spades";

	String cardDeck3 = "";
	
	if((card3 == 0) || (card3 == 13) || (card3 == 26) || (card3 == 39))
		cardDeck3 = "Ace";
	else if ((card3 == 1) || (card3 == 14) || (card3 == 27) || (card3 == 40))
	   cardDeck3 = "2";
	else if ((card3 == 2) || (card3 == 15) || (card3 == 28) || (card3 == 41))
	   cardDeck3 = "3";
	else if ((card3 == 3) || (card3 == 16) || (card3 == 29) || (card3 == 42))
		cardDeck3 = "4";
	else if ((card3 == 4) || (card3 == 17) || (card3 == 30) || (card3 == 43))
		cardDeck3 = "5";
	else if ((card3 == 5) || (card3 == 18)  || (card3 == 31) || (card3 == 44))
		cardDeck3 = "6";
	else if ((card3 == 6) || (card3 == 19) || (card3 == 32) || (card3 == 45))
		cardDeck3 = "7";
	else if ((card3 == 7) || (card3 == 20) || (card3 == 33) || (card3 == 46))
		cardDeck3 = "8";
	else if ((card3 == 8) || (card3 == 21) || (card3 == 34) || (card3 == 47))
		cardDeck3 = "9";
	else if ((card3 == 9) || (card3 == 22) || (card3 == 35) || (card3 == 48))
		cardDeck3 = "10";
	else if ((card3 == 10) || (card3 == 23) || (card3 == 36) || (card3 == 49))
		cardDeck3 = "Jack";
	else if ((card3 == 11) || (card3 == 24) || (card3 == 37) || (card3 == 50))
		cardDeck3 = "Queen";
	else if ((card3 == 12) || (card3 == 25) || (card3 == 38) || (card3 == 51))
		cardDeck3 = "King";

	String type3 = "";
	if ((card3>=0)&& (card3<=12))
	 type3 = "Hearts";
	else if ((card3>=13) && (card3<=25))
	 type3 = "Clubs";
	else if ((card3>=26) && (card3<=38))
	 type3 = "Diamonds";
	else if (card3>=39)
	 type3 = "Spades";
	 	
	System.out.println();
	System.out.println("First card: " + card1);
	System.out.println(cardDeck1 + " of " + type1);  
	System.out.println();
	
	System.out.println("Second card: "+ card2);
	System.out.println(cardDeck2 + " of " +type2);
	System.out.println();
	
	System.out.println("Third card: "+ card3);
	System.out.println(cardDeck3 + " of " +type3);
	
	if ((card1 == card2) && (card1 != card3)){
		System.out.println();
		System.out.println("Cards 1 and 2 are the same");
	}
	else if ((card1 == card3) && (card1 != card2)){
		System.out.println();
		System.out.println("Cards 1 and 3 are the same");
	}
	else if ((card2 == card3) && (card1 != card2)){
		System.out.println();
		System.out.println("Cards 2 and 3 are the same"); 
	}
	else if ((card1 == card2) && (card2 == card3) && (card1 == card3)){
		System.out.println();
		System.out.println("Cards 1, 2, and 3 are the same");
	}
	}//end of method main
}//end of Cards