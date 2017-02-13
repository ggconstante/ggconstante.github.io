/**
 * class Matrix represents a matrix of integers
 * 
 * @author Rick Mercer
 */
public class Matrix {

  // Instance variable
  private int[][] t;

  // Make a clone of initArray so a change to initArray does
  // not affect the array used to construct this Matrix object.
  public Matrix(int[][] initArray) {
    int rows = initArray.length;
    int cols = initArray[0].length;
    t = new int[rows][cols];

    for (int r = 0; r < numRows(); r++) {
      for (int c = 0; c < numColumns(); c++) {
        t[r][c] = initArray[r][c];
      }
    }
  }

  // Return the number of rows in this Matrix object
  public int numRows() {
    return t.length;
  }

  // Return the number of columns in this Matrix object
  public int numColumns() {
    return t[0].length;
  }

  // Return the integer store at the given row and column
  public int get(int row, int column) {
    return t[row][column];
  }

  // Return a textual version of this Matrix object.
  // It is not formatted so number may not line up by column.
  public String toString() {
    String result = "";
    for (int r = 0; r < numRows(); r++) {
      for (int c = 0; c < numColumns(); c++) {
        result += t[r][c] + " ";
      }
      result += "\n";
    }
    return result;
  }

  // Multiply all elements in this Matrixc Object by factor
  public void scalarMultiply(int factor) {
    for (int r = 0; r < numRows(); r++) {
      for (int c = 0; c < numColumns(); c++) {
        t[r][c] *= factor;
      }
    }
  }

  // Precondition: this Matrix and other have the same shape
  public Matrix sum(Matrix other) {
    int[][] result = new int[t.length][t[0].length];
    for (int r = 0; r < numRows(); r++) {
      for (int c = 0; c < numColumns(); c++) {
        result[r][c] = t[r][c] + other.get(r, c);
      }
    }
    return new Matrix(result);
  }

  // Make the rows into columns and the columns into rows
  public void transposeMe() {
    int[][] temp = new int[t[0].length][t.length];
    for (int r = 0; r < numRows(); r++) {
      for (int c = 0; c < numColumns(); c++) {
        temp[c][r] = t[r][c];
      }
    }
    // Do not forget to assign the reference to
    // the new array to the instance variable
    t = temp;
  }
}
