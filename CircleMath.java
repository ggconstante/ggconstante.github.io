/*
	Gingrefel G. Constante
	John McGowan
	9/16/11
	CSc 127A, Section#3
	
	This program reads a radius from the user, then calculates the area and circumference of a circle 
*/
import java.util.Scanner;
public class CircleMath
{
 	public static void main(String[] args)
 	{
 
 	Scanner kb = new Scanner(System.in);//making the scanner read from the keyboard
 
 	System.out.print("Enter the radius of the first circle: "); 
	
	float radius = kb.nextFloat();
	
	double circumference = (2 * Math.PI * radius);
	double area = (Math.PI * radius * radius);
	
	System.out.println("Circumference of a circle of radius "+radius+" is "+circumference+"");
	System.out.println("Area of a circle of radius "+radius+" is "+area+"");
	} // end method main
} // end class CircleMath
