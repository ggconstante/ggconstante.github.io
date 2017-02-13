// Tests the getRows method.

public class BoardClientC
{
   public static void main(String [] args)
   {
      Board aBoard, anotherBoard;
      
      aBoard = new Board();
      
      System.out.println("Testing the getRows() method:");

      System.out.println("Rows in aBoard: " + aBoard.getRows());

      anotherBoard = new Board(25, 30);
      
      System.out.println("Rows in anotherBoard: " + anotherBoard.getRows());
      
      aBoard = new Board(-5, 83);
      System.out.println("# of rows (should be 1): " + aBoard.getRows());

   } // end of method main
} // end of class BoardClientC