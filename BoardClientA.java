// Tests the Board's default constructor and toString method

import java.util.Random;

public class BoardClientA
{
   public static void main(String [] args)
   {
      Board aBoard, anotherBoard;

      System.out.println("Testing default Constructor\n");
      System.out.println("10 x 25 empty board:");

      aBoard = new Board();
      System.out.println(aBoard.toString());

      System.out.println();

      // And, do it again
      System.out.println("Testing default Constructor again\n");
      System.out.println("10 x 25 empty board:");

      anotherBoard = new Board();
      System.out.println(anotherBoard.toString());

   } // end of method main
} // end of class BoardClientA