import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ExpressionTreeTest {

  @Test
  public void testConstructorAndInfix() {
    // Operators: + - * /
    ExpressionTree t = new ExpressionTree("* 4 8");
    assertEquals("4 * 8", t.inFix());
    
    ExpressionTree empty = new ExpressionTree("999");
    assertEquals("999", empty.inFix());

    ExpressionTree t1 = new ExpressionTree("* -1 2");
    assertEquals("-1 * 2", t1.inFix());
    ExpressionTree t2 = new ExpressionTree("+ 3 4");
    assertEquals("3 + 4", t2.inFix());
    ExpressionTree t4 = new ExpressionTree("+ 7 8");
    assertEquals("7 + 8", t4.inFix());
    ExpressionTree t6 = new ExpressionTree("- 777 8888");
    assertEquals("777 - 8888", t6.inFix());
  }

  @Test
  public void testConstructorAndInfixWithDifferentLengthExpressions() {
    ExpressionTree et0 = new ExpressionTree("");
    ExpressionTree et1 = new ExpressionTree("999");
    ExpressionTree et3 = new ExpressionTree("- 3 4");
    ExpressionTree et5 = new ExpressionTree("+ * 3 4 5");
    ExpressionTree et7 = new ExpressionTree("+ / 9 8 + 5 100");

    assertEquals("", et0.inFix());
    assertEquals("999", et1.inFix());
    assertEquals("3 - 4", et3.inFix());
    assertEquals("3 * 4 + 5", et5.inFix());
    assertEquals("9 / 8 + 5 + 100", et7.inFix());
  }

  @Test
  public void testHeight() {
    ExpressionTree et0 = new ExpressionTree("");
    ExpressionTree et1 = new ExpressionTree("999");
    ExpressionTree et3 = new ExpressionTree("* 1 2");
    ExpressionTree et5 = new ExpressionTree("+ * 3 4 5");

    //    assertEquals(-1, et0.height());
    //    assertEquals(0, et1.height());
    //    assertEquals(1, et3.height());
    //    assertEquals(2, et5.height());
  }
}