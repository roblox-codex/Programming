#include<bits/stdc++.h>
using namespace std;

vector<int> minOperations(vector<int>& a) {
    int n = a.size();
    vector<int> ans(n);
    int prefixSum = 0;
    for(int i=0;i<n;i++){
        ans[i] = i*a[i] - prefixSum;
        prefixSum += a[i];
    }
    int suffixSum = 0;
    for(int i=n-1;i>=0;i--){
        ans[i] += suffixSum - (n-i-1)*a[i];
        suffixSum += a[i];
    }
    return ans;
}

int main(){
    vector<int> a = {1,2,3,5,7};
    vector<int> ans = minOperations(a);
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
    return 0;
}
