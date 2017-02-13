                                                                                          
/*
   Name: Gingrefel G. Constante
	Partner's name: Akbar Faqeeri  	
   Section leader:John McGowan
   Section 3, Oct 20, 2011
   Lab 9 - Problem 1, CSc 127A, Fall 2011
   
*/
import java.util.Scanner; 
import java.io.File;
import java.io.IOException;


public class BoxFactory{
  public static void main (String[]args) throws IOException {
      // getting the input file from the user
  		Scanner scan = new Scanner(System.in);
  		System.out.print("Enter the file name: ");
  		String fileName = scan.next();
		
	   // reading from the file
	   File inputFile = new File(fileName);
	 	Scanner fileScan = new Scanner(inputFile);
		
		//while there is text in the file
	   while(fileScan.hasNext()){
		// getting the next token in the file
	  		String symbol = fileScan.next();
			int number = fileScan.nextInt();
			
			square(number, symbol);
		}	
	 }//end method
	 
	 public static void square (int number, String symbol){
	 // gives us rows
		for (int j = 0; j < number; j++)
		{
		//gives columns
			for (int i = 0; i <  number; i++)
			{
			//the symbol that is printed
				System.out.print(symbol);
			}
			//prints space between boxes
				System.out.println(	);
		 }  		 
	 }//end of method main 
}//end of BoxFactory	 
	 
	 