import java.io.File;
import java.util.Scanner;

public class ArrayTools {
    
    private int[] data;
    
    public ArrayTools(int[] inputArray){
        data = new int[inputArray.length];
        for (int i = 0; i < inputArray.length; i++)
            data[i] = inputArray[i];
    }    
    
    public ArrayTools(String fileName, int size) throws Exception{
        //Your code to read in from a file goes here

   }    

   //range

   //scale

   //minIndex

   //maxIndex 

   //oddEvens


    public String toString(){
        String result ="[";
        for(int i = 0; i < data.length; i++){
            result += data[i];
            if (i < data.length - 1)
                result += ",";
        }
        result += "]";
        return result;
    }
    
}