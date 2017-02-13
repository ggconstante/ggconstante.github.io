import java.util.Scanner;

/**
 * Beginning of a type that can store and evaluate arithmetic expressions
 * 
 * @author Rick Mercer
 */
public class ExpressionTree {

  private class TreeNode {
    private String data;
    private TreeNode left;
    private TreeNode right;

    public TreeNode(String theData) {
      data = theData;
      left = null;
      right = null;
    }

    public TreeNode(String theData, TreeNode leftSubTree, TreeNode rightSubTree) {
      data = theData;
      left = leftSubTree;
      right = rightSubTree;
    }

  } // end class TreeNode

  // The external reference starting point
  private TreeNode root;
  private Scanner scanner;

  public ExpressionTree(String prefixExpression) {
    scanner = new Scanner(prefixExpression);
    if (!scanner.hasNext())
      root = null;
    else
      root = build();
  }

  private TreeNode build() {
    String token = scanner.next();
    if (isOperand(token))
      return new TreeNode(token);
    else {
      TreeNode left = build();
      TreeNode right = build();
      return new TreeNode(token, left, right);
    }
  }

  private boolean isOperand(String token) {
    return "+/-*".indexOf(token) < 0;
  }

  public String inFix() {
    return inFix(root).trim();
  }

  private String inFix(TreeNode t) {
    if (t == null)
      return "";
    else
      return inFix(t.left) + t.data + " " + inFix(t.right);
  }

}