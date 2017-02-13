/**
 * A unit test for class LinkedSet<E> 
 */
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LinkedListTest {

  @Test
  public void testSizeWhenEmpty() {
    LinkedList<String> names = new LinkedList<String>();
    assertEquals("Size failed when empty", 0, names.size());
  }

  @Test
  public void testIsEmpty() {
    LinkedList<String> names = new LinkedList<String>();
    assertTrue(names.isEmpty());
  }

  @Test
  public void testIsEmptyWhenNot() {
    LinkedList<String> names = new LinkedList<String>();
    names.addInOrder("any string");
    assertFalse("Failed isEmpty()", names.isEmpty());
  }

  // Rick completes addInOrder
  @Test
  public void testInsertMaintainsOrdering() {
    LinkedList<String> names = new LinkedList<String>();
    names.addInOrder("B");
    names.addInOrder("A");
    names.addInOrder("D");
    names.addInOrder("C");

    assertEquals("[A, B, C, D]", names.toString());
  }

  // Everyone implements remove
  @Test
  public void testRemove() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addInOrder(5);
    ints.addInOrder(1);
    ints.addInOrder(4);
    ints.addInOrder(2);
    ints.addInOrder(3);
    assertEquals("[1, 2, 3, 4, 5]", ints.toString());

    assertFalse(ints.remove(99));
    assertEquals("[1, 2, 3, 4, 5]", ints.toString());

    assertTrue(ints.remove(3));
    assertEquals("[1, 2, 4, 5]", ints.toString());

    assertTrue(ints.remove(1));
    assertEquals("[2, 4, 5]", ints.toString());

    assertTrue(ints.remove(5));
    assertEquals("[2, 4]", ints.toString());

    assertTrue(ints.remove(2));
    assertEquals("[4]", ints.toString());

    assertTrue(ints.remove(4));
    assertEquals("[]", ints.toString());

    assertFalse(ints.remove(4));
    assertTrue(ints.isEmpty());
  }

  @Test
  public void testAddLast() {
    LinkedList<String> strings = new LinkedList<String>();
    strings.addLast("D");
    strings.addLast("C");
    strings.addLast("B");
    strings.addLast("A");
    assertEquals(4, strings.size());
    assertEquals("[D, C, B, A]", strings.toString());
  }

  @Test
  public void testIsSorted() {
    LinkedList<String> strings = new LinkedList<String>();
    strings.addLast("C");
    strings.addLast("B");
    assertEquals(2, strings.size());
    assertEquals("[C, B]", strings.toString());
    assertFalse(strings.isSorted());
  }

  @Test
  public void testIsSorted2() {
    LinkedList<String> strings = new LinkedList<String>();
    strings.addLast("A");
    strings.addLast("B");
    strings.addLast("C");
    assertEquals(3, strings.size());
    assertEquals("[A, B, C]", strings.toString());
    assertTrue(strings.isSorted());
  }

  @Test
  public void testPairCount() {
    LinkedList<String> names = new LinkedList<String>();
    assertEquals(0, names.pairCount());

    names.addLast("Taylor");
    assertEquals(0, names.pairCount());
    names.addLast("Taylor");
    assertEquals(1, names.pairCount());
    names.addLast("Taylor");
    assertEquals(2, names.pairCount());
    names.addLast("Taylor");
    assertEquals(3, names.pairCount());
    names.addLast("Devon");
    assertEquals(3, names.pairCount());
    names.addLast("Devon");

    assertEquals(4, names.pairCount());
    assertEquals(6, names.size());
  }

  @Test
  public void removeAllWhenTheyAreAllTheSame() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addLast(1);
    ints.addLast(1);
    ints.addLast(1);

    assertEquals("[1, 1, 1]", ints.toString());
    assertEquals(3, ints.size());

    ints.removeAll(1);
    assertEquals("[]", ints.toString());
    assertEquals(0, ints.size());
  }

  @Test
  public void removeAll() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addLast(1);
    ints.addLast(2);
    ints.addLast(1);
    ints.addLast(4);
    ints.addLast(5);
    ints.addLast(1);

    assertEquals("[1, 2, 1, 4, 5, 1]", ints.toString());
    assertEquals(6, ints.size());

    ints.removeAll(1);
    assertEquals("[2, 4, 5]", ints.toString());
    assertEquals(3, ints.size());

  }

  @Test
  public void removeAllWhenConsecutive() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addLast(1);
    ints.addLast(2);
    ints.addLast(1);
    ints.addLast(1);
    ints.addLast(3);
    ints.addLast(1);
    ints.addLast(1);

    assertEquals("[1, 2, 1, 1, 3, 1, 1]", ints.toString());
    assertEquals(7, ints.size());

    ints.removeAll(1);
    assertEquals("[2, 3]", ints.toString());
    assertEquals(2, ints.size());
  }

  @Test
  public void testDuplicateAll() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addLast(5);
    ints.addLast(1);
    ints.addLast(5);
    ints.addLast(5);
    ints.addLast(4);
    ints.addLast(5);

    assertEquals("[5, 1, 5, 5, 4, 5]", ints.toString());
    assertEquals(6, ints.size());

    ints.duplicateAll(5);
    assertEquals("[5, 5, 1, 5, 5, 5, 5, 4, 5, 5]", ints.toString());
    assertEquals(10, ints.size());
  }

  @Test
  public void testDuplicateAllWhenSizeIs3() {
    LinkedList<Integer> ints = new LinkedList<Integer>();
    ints.addLast(1);
    ints.addLast(2);
    ints.addLast(3);
    ints.addLast(2);
    assertEquals("[1, 2, 3, 2]", ints.toString());
    assertEquals(4, ints.size());
    ints.duplicateAll(2);
    assertEquals("[1, 2, 2, 3, 2, 2]", ints.toString());
    assertEquals(6, ints.size());
  }

}
