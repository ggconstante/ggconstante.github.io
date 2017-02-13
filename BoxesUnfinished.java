/*
	
	Gingrefel Constante
	John McGowan
	Section 3, Thursday,noon-01:50pm
	Jesse Bright, Section 4
	Assignment 8 - Problem #1,CSc 127A, Fall 2011
	
	The program will draw a square or one of the triangles. The square of triangle will be enclosed in a box.
	The box will be made of -'s across the top and bottom, |'s on the two sides, and +'s in the four corners. 

*/
import java.util.Scanner; 

public class BoxesUnfinished{
	public static void main (String [] args){
  	
		Scanner keyboard = new Scanner( System.in);//asking the Scanner to read from the keyboard 
		
		// Asking for the fill character
		
		System.out.print("Please enter the fill character: ");
		char fillCharacter = keyboard.next().charAt(0);
	
	   // Asking for the box size between 0 to 80
		
		int boxSize;
      do {
        	System.out.print("Please enter the size of the box (0 to 80): ");
	   	boxSize = keyboard.nextInt();
      }  while (  boxSize < 0 || boxSize >80);
		
		//getting the shape information
		char shape = getShape(keyboard);
		
		//making the top border 
		for(int i = 0; i < boxSize + 2; i++)
		{
			if(i == 0)
				System.out.print("+");
			else if(i == boxSize + 1)
				System.out.println("+");
			else 
				System.out.print("-");
		}//end for loop

		drawSquare(fillCharacter, boxSize);
		drawLowerTriangle(fillCharacter, boxSize);
		drawUpperTriangle(fillCharacter, boxSize);

	}//end of main	

	public static char getShape(Scanner scan){
		//Asking the user if they want a triangle or square to be printed
		
		char getShape, upperOrLower;
		do{
			System.out.print("Square or Triangle in the box? (S or T): ");
			getShape = scan.next().charAt(0);
	   }	while ( getShape != 's' &&  getShape != 'S' &&  getShape != 't' &&  getShape != 'T' ); 
		
		if (getShape == 's' || getShape == 'S')
		   return 's'; 
		
		do{
			System.out.print("Upper or lower triangle (U or L): ");
			upperOrLower = scan.next().charAt(0);	
			}while (upperOrLower != 'U' || upperOrLower != 'u' ||upperOrLower != 'L' || upperOrLower != 'l');
					
			return upperOrLower;
	}				
	
	
	
   
	public static void drawSquare(char fillCharacter, int boxSize ){
      // gives us the rows	
		for (int j= 0; j < boxSize; j++){
		//gives columns
			for (int i=0; i <  boxSize; i++){
			// the character that makes up the square
				System.out.print(fillCharacter);
			}
				//begin new line after printing each row
				System.out.println(	);
		 }  		 
	
			
	}	
	
	public static void drawLowerTriangle(char fillCharacter, int boxSize ){
	   String answer="";
		for( int i=0; 1<boxSize; i++){ 
			answer=answer+fillCharacter;
		}	
		String spaces= "";
		int k=boxSize;
		for (int i=0; i<boxSize; i++ ){
	  			
  			for (int j=0; j < boxSize; j++ ){
			
		  		System.out.println(answer+spaces);
			 	answer=answer.substring(0,k-1);
			 	spaces=spaces+" ";
			 	k--;
			}
  	   }
 			
   }
	
	
	
	public static void drawUpperTriangle(char fillCharacter, int boxSize){
	
	}
} 

	
