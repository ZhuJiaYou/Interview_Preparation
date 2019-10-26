class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root)
            return res;
        vector<TreeNode*> stack;
        stack.push_back(root);
        while (!stack.empty())
        {
            root = stack.back();
            res.push_back(root->val);
            stack.pop_back();
            if (root->right)
                stack.push_back(root->right);
            if (root->left)
                stack.push_back(root->left);
        }
        return res;
    }
};
