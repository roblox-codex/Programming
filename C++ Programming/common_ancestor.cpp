class Solution
{
    public:
    
    vector<int> arr;
    bool visited = false;
    Node* LCA(Node* root, int x, int y) {
        if(!root)return NULL;
        if(root->data==x or root->data==y)return root;
        auto a=LCA(root->left,x,y),b=LCA(root->right,x,y);
        if(a and b)return root;
        if(a)return a;
        return b;
    }
    
    void rootToNode(Node* root, Node* node) {
        if(!root)return;
        if(!visited)arr.push_back(root->data);
        if(root==node)visited=true;
        rootToNode(root->left, node);
        rootToNode(root->right, node);
        if(!visited)arr.pop_back();
    }
    int kthCommonAncestor(Node *root, int k,int x, int y)
    {
        auto node = LCA(root,x,y);
        rootToNode(root,node);
        if(arr.size()<k)return -1;
        return arr[arr.size()-k];
    }
};
