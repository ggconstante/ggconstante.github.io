public class ArrayToolsClient {
    public static void main(String[] args) throws Exception{
        
        int[] data = {0,6,3,2,22,8,2,-5,10};
        ArrayTools at = new ArrayTools(data);
        System.out.println("Testing first constructor");
        System.out.println("Data contains: " + at.toString());
        
        //testing the range method
        System.out.println("The range of data is " + at.range());
        
        //testing the maxIndex method
        System.out.println("The index of the largest value is " + at.maxIndex());
        
        //testing the minIndex method
        System.out.println("The index of the smallest value is " + at.minIndex());
        
        //testing oddsEvens
        int[] result = at.oddsEvens();
        System.out.println("The number of odds is " + result[0]);
        System.out.println("The number of evens is " + result[1]);
        
        //testing scale
        System.out.print("Scaling data by 5 gives ");
        at.scale(5);
        System.out.println(at.toString());
        
        //testing range again
        System.out.println("The range of data is now " + at.range());
       


        System.out.println("\nTesting 2nd Constructor");
        at = new ArrayTools("input.txt", 8);
        System.out.println("Data contains: " + at.toString());
        
        //testing the range method
        System.out.println("The range of data is " + at.range());
        
        //testing the maxIndex method
        System.out.println("The index of the largest value is " + at.maxIndex());
        
        //testing the minIndex method
        System.out.println("The index of the smallest value is " + at.minIndex());
        
        //testing oddsEvens
        result = at.oddsEvens();
        System.out.println("The number of odds is " + result[0]);
        System.out.println("The number of evens is " + result[1]);
        
        //testing scale
        System.out.print("Scaling data by 5 gives ");
        at.scale(5);
        System.out.println(at.toString());
        
        //testing range again
        System.out.println("The range of data is now " + at.range());
    }
}