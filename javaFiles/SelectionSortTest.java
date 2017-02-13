import static org.junit.Assert.assertEquals;

import org.junit.Test;




public class SelectionSortTest {

  @Test
  public void testSelectionSort() {
    String[] names = { "Joseph", "Lauren", "Ralf", "Curtis", "Henry", "Liz" };
    selectionSort(names);

    assertEquals("Curtis", names[0]);
    assertEquals("Henry", names[1]);
    assertEquals("Joseph", names[2]);
    assertEquals("Lauren", names[3]);
    assertEquals("Liz", names[4]);
    assertEquals("Ralf", names[5]);
  }

  public void selectionSort(String names[]) { // Arrange the array
    int n = names.length;
    // Sort from left to right
    for (int left = 0; left < n - 1; left++) {
      // First assume the largest is the first element in the subarray
      int subscriptOfSmallest = left + 1;
      for (int i = left + 1; i < n; i++) {
        if (names[i].compareTo(names[subscriptOfSmallest]) < 0)
          subscriptOfSmallest = i;
      }
      String temp = names[left];
      names[left] = names[subscriptOfSmallest];
      names[subscriptOfSmallest] = temp;
    }
  }
}
