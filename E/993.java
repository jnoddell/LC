/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int getDepth(TreeNode root, int num_1, int num_2, int depth) {
        
        if (root == null)
            return 0;
        
        if (root.val == num_1)
            return depth;
        
        if (root.left != null && root.right != null && root.left.val == num_1 && root.right.val == num_2)
            return 0-1000;
        
        return getDepth(root.left, num_1, num_2, depth + 1) + getDepth(root.right, num_1, num_2, depth + 1);
    }
    
    public boolean isCousins(TreeNode root, int x, int y) {
     
        int depth_x = getDepth(root, x, y, 0);
        int depth_y = getDepth(root, y, x, 0);
        
        if (depth_x == depth_y)
            return true;
        return false;
    }
}
