// Tests the getColumns method.

public class BoardClientD
{
   public static void main(String [] args)
   {
      Board aBoard, anotherBoard;
      
      aBoard = new Board();
      
      System.out.println("Testing the getColumns() method:");

      System.out.println("Columns in aBoard: " + aBoard.getColumns());

      anotherBoard = new Board(25, 30);
      
      System.out.println("Columns in anotherBoard: " + anotherBoard.getColumns());

      anotherBoard = new Board(-5, 83);
      System.out.println("# of columns (should be 80): " + anotherBoard.getColumns());

      
   } // end of method main
} // end of class BoardClientD