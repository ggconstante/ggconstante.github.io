public class RecursionFun {

  // Recursive solution
  // precondition: n >= 0
  public long factRec(int n) {
    if (n <= 1)
      return 1; // base case
    else
      return n * factRec(n - 1); // Recursive case
  } // Don't call factRec(n + 1)!

  public int gcd(int a, int b) {
    if (b == 0)
      return a;
    else
      return gcd(b, a % b);

  }

  public boolean isPalindrome(String str) {
    if (str.length() <= 1)
      return true;
    else if (str.charAt(0) != str.charAt(str.length() - 1))
      return false;
    else
      return isPalindrome(str.substring(1, str.length() - 1));
  }