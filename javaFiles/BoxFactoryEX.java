/*
	Gingrefel G. Constante
	Partner's name: Akbar Faqeeri
	Section leader: John McGowan
	Date: 10/20/2011, CSc 127A, Section 3
	
	This program reads in from an input file as to how print boxes. Your program should ask for 
	the name of the input file, and then begin processing it. 
*/	
import javax.swing.JButton;
import java.util.Scanner; 
import java.io.File;
import java.io.IOException;


public class BoxFactoryEX
{
  public static void main (String[]args) throws IOException
  {
    
    Scanner scan = new Scanner(System.in);
	 
	 System.out.print("Enter the name of the file: ");
	 String fileName = scan.next();
	 
	 File inputFile = new File(fileName);
	 Scanner fileScan = new Scanner(inputFile);
  		
		
		  for ( int counter = 0; counter< 3; counter ++){
  
  			int numTimes = scan.nextInt();
			printdollarsign(numTimes);
		}
	
	}	
	
	public static void printdollarsign(int times){
		for (int i = 0; i<times; i++) {
		System.out.print("$");
		
		}
		System.out.println();
		}
		public static int add(int v1, int v2){
			if (v1>v2) {
				return v1+v2;
			} else if (v1 < v2) {
			   return v2+v1;
				
			}
			return 0;	
	}
	
}


	