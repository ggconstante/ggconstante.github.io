/**
 * This unit test shows a further specification of the Bag ADT. It can also be
 * used later to develop ArrayBag and test that the new class works correctly.
 */
import static org.junit.Assert.*;

import org.junit.Test;

public class GenericBagTest {

  @Test
  public void testGenericity() {
    GenericBag<String> names = new GenericArrayBag<String>();
    names.add("Taylor");
    names.add("Kim");
    GenericBag<Integer> testScores = new GenericArrayBag<Integer>();
    testScores.add(new Integer(99));
    testScores.add(77);
    testScores.add(88);

  }

  @Test
  public void testIsEmptyWithOneAdd() {
    GenericBag<String> names = new GenericArrayBag<String>();
    assertTrue(names.isEmpty());
    names.add("Kim");
    assertFalse(names.isEmpty());
  }

  @Test
  public void testOccurencesOfWithOneElement() {
    GenericBag<String> names = new GenericArrayBag<String>();
    assertEquals(0, names.occurencesOf("Kim"));
    names.add("Kim");
    assertEquals(1, names.occurencesOf("Kim"));
  }

  @Test
  public void testOccurencesOfWhenMoreThanOneExists() {
    GenericBag<String> names = new GenericArrayBag<String>();
    names.add("Sam");
    names.add("Devon");
    names.add("Sam");
    names.add("Sam");
    assertEquals(0, names.occurencesOf("Not here"));
    assertEquals(1, names.occurencesOf("Devon"));
    assertEquals(3, names.occurencesOf("Sam"));
  }

  @Test
  public void testRemove() {
    ArrayBag names = new ArrayBag();
    names.add("Sam");
    names.add("Chris");
    names.add("Devon");

    // Return false if the element does not occur
    assertFalse(names.remove("Not here"));

    // Remove “Sam” successfully, then try again.
    assertTrue(names.remove("Sam"));
    assertEquals(0, names.occurencesOf("Sam"));
    assertFalse(names.remove("Sam"));
    assertEquals(0, names.occurencesOf("Sam"));

    // Remove all other elements
    assertEquals(1, names.occurencesOf("Chris"));
    assertTrue(names.remove("Chris"));
    assertEquals(0, names.occurencesOf("Chris"));

    // Only one element left
    assertFalse(names.isEmpty());
    assertEquals(1, names.occurencesOf("Devon"));
    assertTrue(names.remove("Devon"));
    assertEquals(0, names.occurencesOf("Devon"));

    // Assert the bag is empty
    assertTrue(names.isEmpty());
  }

  @Test
  public void testGet() {
    GenericArrayBag<String> names = new GenericArrayBag<String>();
    names.add("Sam");
    names.add("Chris");
    names.add("Devon");
    assertEquals("Sam", names.get(0));
    assertEquals("Chris", names.get(1));
    assertEquals("Devon", names.get(2));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testExceptionIsActuallyThrown() {
    GenericArrayBag<String> names = new GenericArrayBag<String>();
    names.add("Sam");
    assertEquals("Sam", names.get(0));
  }
  
  
  @Test public void testForwardIterator() {
    GenericArrayBag<String> names = new GenericArrayBag<String>();
    names.add("Sam");
    names.add("Chris");
    names.add("Devon");
    ForwardIterator<String> fitr = names.forwardIterator();
    assertTrue(fitr.hasNext());
    assertEquals("Sam", fitr.next());
    assertEquals("Chris", fitr.next());
    assertEquals("Devon", fitr.next());
    assertFalse(fitr.hasNext());
  }

}