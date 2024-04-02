class Solution
{
    public:
    void inorder(Node* root,int &ans,int &k)
    {
        if(root==NULL)return;
        inorder(root->left,ans,k);
        ans=min(ans,abs(k-root->data));
        k=root->data;
        inorder(root->right,ans,k);
    }
    int absolute_diff(Node *root)
    {
        //Your code here
        int ans=1e9,k=-1e9;
        inorder(root,ans,k);
        return ans;
    }
}
