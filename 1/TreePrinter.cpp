/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/

class TreePrinter {
public:
    vector<vector<int> > printTree(TreeNode* root) {
        queue<TreeNode*> tree;
        vector<vector<int>> result;
        vector<int> row;
        TreeNode* last = root;
        TreeNode* nlast = NULL;
        TreeNode* node = NULL;
        tree.push(root);
        
        while(!tree.empty()){
            node = tree.front();
            tree.pop();
            row.push_back(node->val);
            if(node->left){
                tree.push(node->left);
                nlast = node->left;
            }
            if(node->right){
                tree.push(node->right);
                nlast = node->right;
            }
            if(last == node){
                last = nlast;
                result.push_back(row);
                row.clear();
            }
        }
        return result;
    }
};