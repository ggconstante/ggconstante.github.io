import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LinkedBagTest {

  @Test
  public void testFailedIsEmptyWhenEmpty() {
    // Java generics will be needed to make this compile with <String>
    LinkedBag<String> names = new LinkedBag<String>();
    assertTrue(names.isEmpty());

    // Bag objects should be able to store any type of elements
    LinkedBag<Integer> ints = new LinkedBag<Integer>();
    assertTrue(ints.isEmpty());

    LinkedBag<Character> chars = new LinkedBag<Character>();
    assertTrue(chars.isEmpty());
  }

  @Test
  public void testFailedIsEmptyAfterElementsWereAdded() {
    // Java generics will be needed to make this compile with <String>
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    assertFalse(names.isEmpty());

    // Bag objects should be able to store any type of elements
    LinkedBag<Integer> ints = new LinkedBag<Integer>();
    ints.add(123);
    ints.add(123);
    assertFalse(ints.isEmpty());

    LinkedBag<Character> chars = new LinkedBag<Character>();
    assertTrue(chars.isEmpty());
    chars.add('G');
    chars.add('H');
    chars.add('I');
    assertFalse(chars.isEmpty());
  }

  @Test
  public void testFailedOccurencesofWhenBagIsEmpty() {
    LinkedBag<String> names = new LinkedBag<String>();
    assertEquals(0, names.occurencesOf("NOT here"));
  }

  @Test
  public void testFailedAddOrOccurencesofWhenElementIsNotInTheBag() {
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    names.add("Devon");
    names.add("Sam");
    names.add("Sam");
    assertEquals(0, names.occurencesOf("NOT Here"));
  }

  @Test
  public void testFailedAddOrOccurencesOfWhenElementShouldBeFoundExactlyOnce() {
    LinkedBag<String> names = new LinkedBag<String>();
    assertTrue(names.isEmpty());
    names.add("Sam");
    assertFalse(names.isEmpty());
    names.add("Devon");
    names.add("Sam");
    assertEquals(1, names.occurencesOf("Devon"));
    assertEquals(2, names.occurencesOf("Sam"));
  }

  @Test
  public void testToString() {
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    names.add("Devon");
    names.add("Sam");
    assertEquals("Sam Devon Sam", names.toString());
  }

  @Test
  public void testFailerAddOrOccurencesOfWhenElementShouldBeFoundTwice() {
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    names.add("Devon");
    names.add("Sam");
    assertEquals(2, names.occurencesOf("Sam"));
  }

  @Test
  public void testFailedAddOrOccurencesOfWhenElementShouldBeFoundThreTimes() {
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    names.add("Jo");
    names.add("Ali");
    names.add("Sam");
    names.add("Sam");
    assertEquals(3, names.occurencesOf("Sam"));
  }
  
  @Test public void testForwardIterator() {
    LinkedBag<String> names = new LinkedBag<String>();
    names.add("Sam");
    names.add("Chris");
    names.add("Devon");
    ForwardIterator<String> fitr = names.forwardIterator();
    assertTrue(fitr.hasNext());
    assertEquals("Devon", fitr.next());
    assertEquals("Chris", fitr.next());
    assertEquals("Sam", fitr.next());
    assertFalse(fitr.hasNext());
  }
}