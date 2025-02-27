/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b){
    if(a > b){
        return a;
    }
    return b;
}

int maxDepth(struct TreeNode* root) {
    if(!root)return 0;
    int maxLeft = maxDepth(root->right);
    int maxRight = maxDepth(root->left);
    return max(maxLeft, maxRight) + 1;
}