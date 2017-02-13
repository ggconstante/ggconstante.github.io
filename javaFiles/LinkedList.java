/**
 * A collection class to represent a List where elements are stored in a
 * singly-linked structure
 * 
 * @author mercer
 * 
 * @param <E>
 *          A type parameter that limits the type of element to objects whose
 *          class implements Comparable<E>
 */
public class LinkedList<E extends Comparable<E>> {

  private class Node {
    private E data;
    private Node next;

    public Node(E element) {
      data = element;
      next = null;
    }

    public Node(E element, Node nextRef) {
      data = element;
      next = nextRef;
    }
  }

  private Node first;
  private int n;

  public LinkedList() {
    first = null;
    n = 0;
  }

  // Return true if this set is empty
  public boolean isEmpty() {
    // TODO: Make this method work
    return first == null;
  }

  @Override
  public String toString() {
    if (this.isEmpty())
      return "[]";
    else {
      String result = "[";
      Node ref = first;
      while (ref.next != null) {
        result += ref.data + ", ";
        ref = ref.next;
      }
      result += ref.data + "]";
      return result;
    }
  }

  // Add an element to this list in its natural location.
  // This method keeps elements sorted according to the
  // class's compareTo method
  public void addInOrder(E element) {
    // Special case
    if (this.isEmpty()) {
      first = new Node(element);
    }
    // Special case: element precedes all others
    else if (((Comparable<E>) element).compareTo(first.data) < 0) {
      first = new Node(element, first);
    } else {
      Node ref = first;
      while (ref.next != null && element.compareTo(ref.next.data) > 0) {
        ref = ref.next;
      }
      ref.next = new Node(element, ref.next);
    }
    n++;
  }

  // Completed by 3 brave C Sc 127B students in front
  // of 120 colleagues on Friday, 10-Feb
  public boolean remove(E element) {
    Node ref = first;
    if (ref == null)
      return false;
    if (ref.data.equals(element)) {
      first = first.next;
      n--;
      return true;
    }
    while (ref.next != null && !ref.next.data.equals(element))
      ref = ref.next;
    if (ref.next == null)
      return false;
    ref.next = ref.next.next;
    n--;
    return true;

  }

  // Return the number of elements in this set
  public int size() {
    return n;
  }

  public void addLast(E el) {
    if (this.isEmpty())
      first = new Node(el);
    else {
      Node ref = first;
      while (ref.next != null) {
        ref = ref.next;
      }
      ref.next = new Node(el);
    }
    n++;
  }

  public boolean isSorted() {
    if (size() <= 1)
      return true;
    Node prev = first;
    Node curr = first.next;
    while (curr != null) {
      if (prev.data.compareTo(curr.data) > 0) {
        return false;
      }
      prev = curr;
      curr = curr.next;
    }
    return true;
  }

  public int pairCount() {
    if (size() <= 1)
      return 0;

    Node prev = first;
    Node curr = first.next;
    int count = 0;

    while (curr != null) {
      if (prev.data.compareTo(curr.data) == 0)
        count++;
      prev = curr;
      curr = curr.next;
    }

    return count;
  }

  public void removeAll(E el) {
    if(this.isEmpty())
      return;
    while(first != null && first.data.compareTo(el) == 0) {
      first = first.next;
      n--;
    }
    
    if(first == null)
      return;
    
    Node ref = first;
    while(ref.next != null) {
      if(el.compareTo(ref.next.data) == 0) {
        ref.next = ref.next.next;
        n--;
      }
      else
        ref = ref.next;
    }
  }

  public void duplicateAll(E el) {
    if(size() == 0)
      return;
    
    Node ref = first;
    while(ref != null){
      if(ref.data.equals(el)){
        ref.next = new Node(el, ref.next);
        n++;
        ref = ref.next.next;
      }
      else 
        ref = ref.next;
    }

 

    
    
    
    
    
  }
}