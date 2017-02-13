/*
	Gingrefel Constante

	Section Leader: John McGowan
	Section 3, noon-01:50pm
	Partner's name: Jesse Bright, Section 4 
	Assignment 11 - Problem 1, CSc 127A, Fall 2010
	
	writing multiple methods that will be called by the static main and will produce different outputs in two dimensional array. 
*/	
import java.io.File;
import java.util.Scanner;
import java.io.IOException;

public class ArrayStuff{//calling the class

	private int [][] twoArray;// two dimensional array

	// first constructor that will take a two dimensional array 
	public ArrayStuff(int [][] setArray){//this is your 2-D argument array
		twoArray = new int[setArray.length][setArray[0].length];//setting your 2-D array to your 2-D argument array
		for (int row = 0; row<setArray.length; row++){//going through the rows of a 2-D array
			for (int col = 0; col<setArray[row].length; col++){//going through the columns of a 2-D array
				twoArray[row][col] = setArray[row][col];//storing your 2-D argument array to your two dimensional array
			}
		}
	}//end of first constructor ArrayStuff  
	
	//this is the second contructor that will take the name of a file 
	public ArrayStuff(String fileName, int rowItem, int colItem) throws IOException{//setting parameters or arguments
	
		File inputFile = new File(fileName);
		Scanner fileScan = new Scanner(inputFile);//reading from the above file name or go through the first argument
		
		twoArray = new int [rowItem][colItem];
		for (int row = 0; row<rowItem; row++){//numbers of rows as the second argument
			for (int col = 0 ; col<colItem; col++){//numbers of columns as the third argument 
			twoArray[row][col] = fileScan.nextInt();//this will read the appropriate number of integers per line
			}
		}
	}//end of second constructor ArrayStuff
	
	// toString	
	public String toString(){
		String outPut = "";
		for(int row = 0; row<twoArray.length; row++){//going through the length of the rows
			outPut += "Row " + row + ":" + "\t";//this will give us the elements of the row and a colon at the start of each line 
			
			for(int col = 0; col<twoArray[row].length; col++){//going through the length of the columns
				
				if (col == twoArray[row].length - 1) 
					outPut = outPut + twoArray[row][col];
				else {
					outPut = outPut + twoArray[row][col] + "\t";
				}
				
			}
				outPut += "\n";//creates a new line for the array
		}	
			return outPut;//this will return the results of our output
	}//end of method toString
	
	//getNumbers
	public int [][]getNumbers(){
	
	int arrayCopy[][] = new int [twoArray.length][twoArray[0].length];
		for(int row = 0; row<twoArray.length; row++){//go through the length of the rows
			for (int col = 0; col<twoArray[row].length; col++){//go through the length of the columns
			arrayCopy[row][col] = twoArray[row][col];
			}
		}
		return arrayCopy;//returns the copy of the two dimensional array containing the copy of the array in the ArrayStuff
	}//end of method getNumbers
	
	//setNumbers will change the private instance array
	public void setNumbers (int [][] newNum){
	twoArray = new int[newNum.length][newNum[0].length];
		for (int row = 0; row<newNum.length; row++){
			for (int col = 0; col<newNum[row].length; col++){
				twoArray[row][col] = newNum[row][col];
			}
		}
	}//end of method setNumbers
	
	//getNumRows //***rows and columns in order respectively***//
	public int getNumRows(){
		return twoArray.length;//returns number of rows
	}//end of method getNumRows
	
	public int getNumColumns(){
		return twoArray[0].length;//returns number of columns
	}//end of method getNumColumns
	
	//getOneRow
	public int [] getOneRow(int singleRow){//takes one argument
	
		int [] oneRow = new int [twoArray[singleRow].length];
			for (int row = 0; row<twoArray[singleRow].length; row++){//going through length of the rows in a 2-D array
				oneRow[row] = twoArray[singleRow][row];
			}
			return oneRow;//returns one dimensional array 
		}//end of method getOneRow 
	
	//getOneColumn
	public int [] getOneColumn(int singleColumn){//takes one argument
		
		int [] oneColumn = new int [twoArray.length];
			for (int col = 0; col<twoArray.length; col++){//going through the length of the columns in a 2-D array
				oneColumn[col] = twoArray[col][singleColumn];
			}
			return oneColumn;
		}//end of method getOneColumn
	
	//equals method will check if two objects have the same contents
	public boolean equals(ArrayStuff otherArray){
	
	int [][] compareThisArray = new int[otherArray.getNumRows()][otherArray.getNumColumns()];
		//checking the elements of rows and columns using the if statement 
		if (otherArray.getNumRows() != twoArray.length || otherArray.getNumColumns()!= twoArray[0].length)
			
			return false;//if not equals it will return false
		
		else {//this will execute if the above condition is not met 
			for (int row = 0; row< twoArray.length; row++){//checks the length of the rows
				for (int col = 0; col<twoArray[row].length; col++){//checks the length of the columns
					if (twoArray[row][col]!= compareThisArray[row][col]);
						
						return false; //return false if not equal
				}
			}
			return true;//return true if two objects or array have the same contents
		}	
	}//end of method equals
}//end of class ArrayStuff




		   
			
	
		
		
