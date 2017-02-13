// Tests the setRowColumn and clearBoard methods.
// The first part is the same as BoardClientC in the placement of
// turtles and marks on the board. Then clearBoard is called
// to see if the marks are removed and the turtles remain.
// Tests setRowColumn, clearBoard, and toString  methods

import java.util.Random;

public class BoardClientF
{
   public static void main(String [] args)
   {
      Board aBoard;
      int i;
      char ch;
      Random position = new Random(42);
      
      aBoard = new Board(15, 60);
      
      System.out.println("Testing setRowColumn and clearBoard methods:\n\n");

      System.out.println("The empty board:");
      System.out.println(aBoard.toString());
      
      System.out.println("The board with randomly placed turtles:");
      for ( ch = '0'; ch <= '9'; ch++ )
         aBoard.setRowColumn( position.nextInt(15), position.nextInt(60), ch);
         
      System.out.println(aBoard.toString());
      
      System.out.println("The board with randomly placed characters:");
      System.out.println("Note: not testing if the random characters end up");
      System.out.println("on top of a turtle.");
      for ( i = 0; i < 20; i++ )
         aBoard.setRowColumn( position.nextInt(15), position.nextInt(60),
                              (char) (position.nextInt(58) + 'A') );
      System.out.println(aBoard.toString());
      
      aBoard.clearBoard();
      System.out.println("The board cleared with only the turtles left:");
      System.out.println(aBoard.toString());

   } // end of method main
} // end of class BoardClientF