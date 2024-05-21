class Solution {
        int findCrossOver(vector<int>&arr,int low,int high,int x) {
            if(arr[high]<=x) // x is greater than all 
            return high;
            if(arr[low]>x) // x is smaller than all
            return low;
            int mid;  
            while(low<=high) {
                mid=(low+high)/2;
                if(arr[mid]<=x && arr[mid+1]>x)
                    return mid;
                if(arr[mid]<x) 
                    low=mid+1;
                else 
                    high=mid-1;    
            }
            return mid;
        }
        public:
            vector<int> printKClosest(vector<int>arr, int n, int k, int x) {
                int l=findCrossOver(arr,0,n-1,x);
                int r=l+1;
                int count=0;
                vector<int>ans;
                if(arr[l]==x)
                    l--;
                while(l>=0 && r<n && count<k) {
                    if(x-arr[l]<arr[r]-x)
                        ans.push_back(arr[l--]);
                    else
                        ans.push_back(arr[r++]);
                    count++;    
                }    
                while(count<k && l>=0) {
                    ans.push_back(arr[l--]);
                    count++;
                }    
                while(count<k && r<n) {
                    ans.push_back(arr[r++]);
                    count++;
                }   
                return ans;
            }

    };
