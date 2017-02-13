// A Collection class that implement the most general collection
// there is: a multi-set.  Duplicate elements allowed.
//
// This version does not implement Bag<E>. It does not have remove.
public class LinkedBag<E>  {

  // This inner class allows nodes with a reference to the element and a
  // reference to another Node. This allows for singly linked structures
  private class Node {
    private E data;
    private Node next;

    public Node(E element, Node ref) {
      data = element;
      next = ref;
    }
  }

  // An external reference to the singly linked structure.
  // If first is null, this bag is empty (has 0 elements).
  private Node first;

  public LinkedBag() {
    first = null;
  }

  // O(1)
  public void add(E element) {
     first = new Node(element, first);
  }
  
  @Override
  public String toString() {
    String result = "";
    Node ref = first;
    while(ref != null) {
      result += ref.data + " ";
      ref = ref.next;
    }
    return result.trim();
  }

  // Return true if there are 0 elements in this bag.
  public boolean isEmpty() {
    return first == null;
  }

  // Return how many elements in this bag equals element
  public int occurencesOf(E element) {
    int result = 0;
    for (Node ref = first; ref != null; ref = ref.next) {
      if (element.equals(ref.data))
        result++;
    }
    return result;
  }

  public ForwardIterator<E> forwardIterator() {
    // TODO Auto-generated method stub
    return new FwrdItr();
  }
  
  private class FwrdItr<E> implements ForwardIterator<E> {

    private Node current;
    
    public FwrdItr() {
      current = first;
    }
    public E next() {
      E temp = (E) current.data;
      current = current.next;
      return temp;
    }

    public boolean hasNext() {
      return current != null;
    }
    
  }
}

interface ForwardIterator<E> {

  /**
   * Pre-condition: This method will not be called if there
   * is nothing left to iterate over.
   * 
   * Given the list:
   * 
   * 1, 2, 3, 4, 5
   * 
   * next() will return 1 the first time it is called.
   * next() will return 2 the second time it's called.
   * next() will return 3 the third time is is called.
   * next() will return 4 the fourth time it's called.
   * next() will return 5 the fifth time it is called.
   * At this point, hasNext() will be false
   * 
   * @return the data of the next node.
   */
  public E next();
  
  /**
   * Given the list:
   * 
   * a, b, c, d, e
   * 
   * If next() has never been called, hasNext() returns true.
   * After next() has been called 5 times, hasNext() returns false.
   * 
   * @return True if there is still an element that hasn't been 
   * returned by next(). Otherwise false.
   */
  public boolean hasNext();
  
}