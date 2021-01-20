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
    public int solve(TreeNode self, TreeNode root) {
        
        if (self == null)
            return 0;
        
        if (self.left == null && self.right == null && root.left == self) {
                return self.val;
        } else {
            return solve(self.left, self) + solve(self.right, self);
        }
    }
    
    public int sumOfLeftLeaves(TreeNode root) {
        
        if (root == null)
            return 0;
        else if (root.left == null && root.right == null)
            return 0;
        
        return solve(root, null);
    }
}
