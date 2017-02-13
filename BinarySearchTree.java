public class BinarySearchTree<E extends Comparable<E>> {

  private class TreeNode {
    private E data;
    private TreeNode left, right;

    public TreeNode(E el) {
      data = el;
      left = null;
      right = null;
    }
  }

  private TreeNode root;

  public BinarySearchTree() {
    root = null;
  }

  // Add el into this BST keeping the natural ordering 
  // through an inOrder traversal
  public boolean insert(E el) {
    if (root == null) {
      root = new TreeNode(el);
      return true;
    }
    TreeNode curr = root;
    TreeNode tracker = curr;
    while (curr != null) {
      tracker = curr;
      if (el.compareTo(curr.data) == 0)
        return false;
      else if (el.compareTo(curr.data) < 0)
        curr = curr.left;
      else
        curr = curr.right;
    }

    if (tracker.data.compareTo(el) > 0)
      tracker.left = new TreeNode(el);
    else
      tracker.right = new TreeNode(el);

    return true;

  }

  public String toString() {
    return toString(root).trim();
  }

  private String toString(TreeNode t) {
    if (t == null)
      return "";
    else
      return toString(t.left) + t.data + " " + toString(t.right);
  }
}