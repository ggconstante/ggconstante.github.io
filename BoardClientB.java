// Tests the Board's second constructor and toString method
// Includes tests of the number of rows being outside 1 to 80
// and number of columns being outside 1 to 80

import java.util.Random;

public class BoardClientB
{
   public static void main(String [] args)
   {
      Board aBoard, anotherBoard;

      System.out.println("Testing 2nd Constructor\n");
      System.out.println("15 x 60 empty board:");

      aBoard = new Board(15, 60);
      System.out.println(aBoard.toString());

      System.out.println("11 x 82 empty board, the 82 should become 80:");
      
      anotherBoard = new Board(11, 82);
      System.out.println(anotherBoard.toString());

      System.out.println("11 x -2 empty board, the -2 should become 1:");
      
      anotherBoard = new Board(11, -2);
      System.out.println(anotherBoard.toString());
      
      System.out.println("0 x 20 empty board, the 0 should become 1:");

      aBoard = new Board(0, 20);
      System.out.println(aBoard.toString());

      System.out.println("101 x 20 empty board, the 101 should become 80:");

      aBoard = new Board(101, 20);
      System.out.println(aBoard.toString());

   } // end of method main
} // end of class BoardClientB