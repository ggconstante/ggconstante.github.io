/**
 
 * A Unit test for BinarySearchTree
 * 
 * @author Rick Mercer
 * 
 * Monday 4-June 2011.  Now this unit test is in two files 8:50 am
 * 
 * 777 lines of code
 *
 */
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.Test;

public class BinarySearchTreeTest {

  @Test
  public void InsertAndToString() {
    BinarySearchTree<String> bst = new BinarySearchTree<String>();
    bst.insert("d");
    bst.insert("b");
    bst.insert("e");
    assertEquals("b d e", bst.toString());
    bst.insert("a");
    assertEquals("a b d e", bst.toString());
    bst.insert("c");
    assertEquals("a b c d e", bst.toString());
  }
}