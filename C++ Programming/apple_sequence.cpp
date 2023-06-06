class Solution{   
public:
    int appleSequence(int n, int m, string arr){
        int cnt=0;
        int ans=INT_MIN;
        int st=0;
        int en=0;
        
        while(en < arr.size()){
            while(cnt > m){
                if(arr[st]=='O'){
                    cnt--;
                }
                st++;
            }
            if(arr[en]=='O'){
                cnt++;
            }
            if(cnt <= m){
                ans=max(ans , en-st+1);
            }
            en++;
        }
        return ans;
    }
};
