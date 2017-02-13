import static org.junit.Assert.*;

import org.junit.Test;

public class RecursionFunTest {

  RecursionFun rf = new RecursionFun();

  @Test
  public void testFactorialUsingRecursion() {
    assertEquals(2, rf.factRec(2));
    assertEquals(24, rf.factRec(4));
    assertEquals(6, rf.factRec(3));
    assertEquals(24, rf.factRec(4));
    assertEquals(3628800, rf.factRec(10));
  }

  @Test
  public void testGCDUsingRecursion() {
    assertEquals(5, rf.gcd(5, 0));
    assertEquals(5, rf.gcd(0, 5));
    assertEquals(5, rf.gcd(5, 5));
    assertEquals(5, rf.gcd(25, 5));
    assertEquals(1, rf.gcd(13, 7));
    assertEquals(3, rf.gcd(24, 9));
    assertEquals(3, rf.gcd(9, 24));

  }

  @Test
  public void testIsPalindromeWhenItIs() {
    assertTrue(rf.isPalindrome(""));
    assertTrue(rf.isPalindrome("X"));
    assertTrue(rf.isPalindrome("abba"));
    assertTrue(rf.isPalindrome("racecar"));
    assertTrue(rf.isPalindrome("amanaplanacanalpanama"));
    assertTrue(rf.isPalindrome("madamimadam"));
  }

  @Test
  public void testIsPalindromeWhenItIsNot() {
    assertFalse(rf.isPalindrome("not"));
    assertFalse(rf.isPalindrome("Aba"));
    assertFalse(rf.isPalindrome("1231"));
    assertFalse(rf.isPalindrome("1233 21"));
  }
  
  public void forward(int n) {
	    if (n > 1)
	      forward(n - 1); // recursive call: n goes toward 0
	    // RP# FORWARD
	    System.out.print(n);
	  }

	  @Test
	  public void showRecursion() {
	    int arg = 3;
	    forward(arg);
	    // RP# SHOW
	    arg = 999;
	  }

	  // Non-recursive solution, using a loop
	  // precondition: n >= 0
	  public long factRep(int n) {
	    long result = 1;
	    for (int j = 2; j <= n; j++)
	      result = j * result;
	    return result;
	  }

	  // Recursive solution
	  // precondition: n >= 0
	  public long factRec(int n) {
	    if (n == 0)
	      return 1; // base case
	    else
	      return n * factRec(n - 1); // Recursive case
	  } // Don't call factRec(n + 1)!

	  @Test
	  public void testFacortialMethods() {
	    assertEquals(1, factRep(0));
	    assertEquals(1, factRec(0));
	    assertEquals(1, factRep(1));
	    assertEquals(1, factRec(1));
	    assertEquals(2, factRep(2));
	    assertEquals(2, factRec(2));
	    assertEquals(6, factRep(3));
	    assertEquals(6, factRec(3));
	    assertEquals(24, factRep(4));
	    assertEquals(24, factRec(4));
	    assertEquals(3628800, factRep(10));
	    assertEquals(3628800, factRec(10));
	  }

	  @Test
	  public void testIsPalindromeWhenTheyAre() {
	    assertTrue(isPalindrome(""));
	    assertTrue(isPalindrome("X"));
	    assertTrue(isPalindrome("bb"));
	    assertTrue(isPalindrome("abba"));
	    assertTrue(isPalindrome("amanaplanacanalpanama"));
	    assertTrue(isPalindrome("satanoscillatemymetallicsonatas"));
	  }

	  @Test
	  public void testIsPalindromeWhenTheyAreNot() {
	    assertFalse(isPalindrome("bc"));
	    assertFalse(isPalindrome(" X"));
	    assertFalse(isPalindrome("Bb"));
	    assertFalse(isPalindrome("1232"));
	    assertFalse(isPalindrome("abca"));
	  }

	  private boolean isPalindrome(String str) {
	    if (str.length() <= 1)
	      return true;
	    if (str.charAt(0) != str.charAt(str.length() - 1))
	      return false;
	    else
	      return isPalindrome(str.substring(1, str.length() - 1));
	  }

	  @Test
	  public void testGCD() {
	    assertEquals(10, GCD(10, 0));
	    assertEquals(5, GCD(25, 5));
	    assertEquals(1, GCD(25, 2));
	    assertEquals(6, GCD(12, 30));
	    assertEquals(9, GCD(81, 9));
	    assertEquals(3, GCD(42, 123));
	    assertEquals(42, GCD(42, 0));
	  }

	  @Test(expected = IllegalArgumentException.class)
	  public void testGCDWhenBothZero() {
	    assertEquals(10, GCD(0, 0));
	  }

	  private int GCD(int a, int b) {
	    if (a == 0 && b == 0)
	      throw new IllegalArgumentException();
	    if (b == 0)
	      return a;
	    else if (a == 0)
	      return b;
	    else
	      return GCD(b, a % b);
	  }

	  public int GCDwithALoop(int a, int b) {
	    while (b != 0) {
	      int temp = a;
	      a = b;
	      b = temp % b;
	    }
	    return a;
	  }

	  @Test
	  public void testCombination() {
	    assertEquals(0, combinations(5, 6));
	    assertEquals(1, combinations(5, 0));
	    assertEquals(1, combinations(5, 5));
	    assertEquals(5, combinations(5, 1));
	    assertEquals(10, combinations(5, 2));
	    assertEquals(2598960, combinations(52, 5));
	  }

	  private int combinations(int n, int k) {
	    if (n < 1 || k < 0)
	      throw new IllegalArgumentException();
	    if (k > n)
	      return 0;
	    if (k == 0 || n == 0)
	      return 1;
	    if (n == k)
	      return 1;
	    if (k == 1)
	      return n;
	    else
	      return combinations(n - 1, k - 1) + combinations(n - 1, k);
	  }

	  @Test
	  public void testcountPairs() {
	    assertEquals(0, countPairs(""));
	    assertEquals(0, countPairs("a"));
	    assertEquals(0, countPairs("ab"));
	    assertEquals(0, countPairs("abc"));
	    assertEquals(1, countPairs("aba"));
	    assertEquals(2, countPairs("abab"));
	    assertEquals(3, countPairs("ababa"));
	    assertEquals(1, countPairs("xyyxy"));
	    assertEquals(2, countPairs("yyyy"));
	  }

	  private int countPairs(String str) {
	    if (str.length() < 3)
	      return 0;
	    if (str.charAt(0) == str.charAt(2))
	      return 1 + countPairs(str.substring(1));
	    else
	      return 0 + countPairs(str.substring(1));
	  }
}
