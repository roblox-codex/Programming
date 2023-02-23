class Solution{
public:
    int dfs(int i,vector<int> &arr,int n,vector<int> &vis,vector<int> &dp){
        if(i<0 or i>=n) 
        return 1;
        if(dp[i]!=-1) 
        return dp[i];
        if(vis[i]) 
        return 0;
        vis[i]=1;
        return dp[i]=dfs(i+arr[i],arr,n,vis,dp);
    }
    int goodStones(int n,vector<int> &arr){
        // Code here
        vector<int> vis(n,0),dp(n,-1);
        for(int i=0;i<n;i++){
            if(!vis[i])
            dfs(i,arr,n,vis,dp);
        }
        int ans=0;
        for(int i=0;i<n;i++) {
            if(dp[i]) ans++;
        }
        return ans;
    }   
};
