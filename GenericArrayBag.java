public class GenericArrayBag<E> implements GenericBag<E> {

  // --Instance variables
  private Object[] data;
  private int n;

  // Construct an empty bag that can store any type
  public GenericArrayBag() {
    data = new Object[20];
    n = 0;
  }

  // Add element to this bag at the end of the array
  public void add(E element) {
    data[n] = element;
    n++;
  }

  // Return true if there are 0 elements in this bag
  public boolean isEmpty() {
    return n == 0;
  }

  // Return how many objects currently in the bag match
  // element, using the equals method of the type
  public int occurencesOf(E search) {
    int result = 0;
    for (int i = 0; i < n; i++) {
      if (search.equals(data[i]))
        result++; // Found one that equals element
    }
    return result;
  }

  // If an element that equals v exists, remove one occurrence of it from this
  // Bag and return true. If occurencesOf(v) == 0, simply return false.
  public boolean remove(E element) {
    for (int i = 0; i < n; i++) {
      if (element.equals(data[i])) {
        // Replace the element to be removed with the element at the end of the
        // array
        data[i] = data[n - 1];
        // And reduce the number of meaningful elements by 1
        n--;
        return true;
      }
    }
    // Must be the case that the element did not "equals" any element in this
    // bag
    return false;
  }

  @SuppressWarnings("unchecked")
  public E get(int index) throws IllegalArgumentException {
    if (index < 0 || index >= n)
      throw new IllegalArgumentException("index ==" + index);
    return (E) data[index];
  }

  /**
   * @return a new ReverseIterator
   */
  ForwardIterator<E> forwardIterator() {
    return new ForwardItr();
  }

  private class ForwardItr<E> implements ForwardIterator<E> {

    private int current;

    public ForwardItr() {
      current = 0;
    }

    public E next() {
      E temp = (E) data[current];
      current++;
      return temp;
    }

    public boolean hasNext() {
      return n > current;
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
