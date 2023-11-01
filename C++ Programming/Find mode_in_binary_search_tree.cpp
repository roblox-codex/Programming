class Solution {
public:
vector<int>ans;
int mx_freq=0;
unordered_map<int,int>mp;
void dfs(TreeNode* root){
    if(root==NULL) return;
    int f= mp[root->val]++;
    if(f>mx_freq) 
    {mx_freq=f;
    ans={root->val};
    }
    else if(f==mx_freq) ans.push_back(root->val);
    dfs(root->left);
    dfs(root->right);
}
    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
