/**
 * A type that represent a Matrix of integers.
 * 
 * Methods include: 
 * 1) The constructor 
 * 2) int get(int, int) 
 * 3) void scalarMultiply(int inc) 
 * 4) Matrix sum(Matrix)
 * 5) transposeMe()  added in lecture 20-Jan
 */
import static org.junit.Assert.*;
import org.junit.Test;

public class MatrixTest {

  @Test
  public void testGetters() {
    int[][] a1 = { { 1, 2, 3}, { 1, 2, 3 } };  // two rows, three columns
    int[][] a2 = { { 1, 2}, { 1, 2 }, { 1, 2 } };  // three rows, two columns

    Matrix twoByThree = new Matrix(a1);
    Matrix threeByTwo = new Matrix(a2);
    
    assertEquals(2, twoByThree.numRows());
    assertEquals(3, twoByThree.numColumns());
    assertEquals(3, threeByTwo.numRows());
    assertEquals(2, threeByTwo.numColumns()); 
  }
  
  @Test
  public void testGet() {
    int[][] a1 = { { 5, 7, 9, 4 }, { 3, 2, 1, 8 } };

    Matrix a = new Matrix(a1);

    // Get retrieves an elements the given indexes
    assertEquals(5, a.get(0, 0));
    assertEquals(7, a.get(0, 1));
    assertEquals(9, a.get(0, 2));
    assertEquals(4, a.get(0, 3));
    assertEquals(3, a.get(1, 0));
    assertEquals(2, a.get(1, 1));
    assertEquals(1, a.get(1, 2));
    assertEquals(8, a.get(1, 3));
  }

  @Test
  public void testScalarMultiply() {
    int[][] a = { { 1, 2, 3 }, { 6, 5, 4 } };
    // Create a new instance of Matrix with a copy of an allocated 2D array.
    Matrix mat1 = new Matrix(a);
    mat1.scalarMultiply(3);
    assertEquals(3, mat1.get(0, 0));
    assertEquals(6, mat1.get(0, 1));
    assertEquals(9, mat1.get(0, 2));
    assertEquals(18, mat1.get(1, 0));
    assertEquals(15, mat1.get(1, 1));
    assertEquals(12, mat1.get(1, 2));
  }

  @Test
  public void testMatrixAddition() {
    int[][] a1 = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 } };
    Matrix a = new Matrix(a1);

    int[][] a2 = { { -2, 2, -2, 2 }, { 4, -4, 4, -4 } };

    Matrix b = new Matrix(a2);

    Matrix c = a.sum(b);

    // Check all elements
    assertEquals(-1, c.get(0, 0));
    assertEquals(4, c.get(0, 1));
    assertEquals(1, c.get(0, 2));
    assertEquals(6, c.get(0, 3));
    assertEquals(9, c.get(1, 0));
    assertEquals(2, c.get(1, 1));
    assertEquals(11, c.get(1, 2));
    assertEquals(4, c.get(1, 3));
  }

  @Test
  public void testTransposeMe() {

    int[][] a1 = { { 1, 3, 5 }, { 2, 4, 6 } };
    Matrix a = new Matrix(a1);
    // 1 3 5     t->   1 2
    // 2 4 6  becomes  3 4  <- temp
    //                 5 6
    
    System.out.println(a.toString());
    a.transposeMe();
    System.out.println(a);
       

    assertEquals(1, a.get(0, 0));
    assertEquals(2, a.get(0, 1));
    assertEquals(3, a.get(1, 0));
    assertEquals(4, a.get(1, 1));
    assertEquals(5, a.get(2, 0));
    assertEquals(6, a.get(2, 1));
  }
}
