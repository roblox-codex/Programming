class Solution{   
public:
    //Function to partition the array around the range such 
    //that array is divided into three parts.
    void threeWayPartition(vector<int>& array,int a, int b)
    {
        int i=0,j=array.size()-1;
        while(i<j){
            if(array[i]>b){
                swap(array[i],array[j]);
                j--;
            }
            else i++;
        }
        while(array[j]>b){
            j--;
        }
        i=0;
        while(i<j){
            if(array[i]>=a){
                swap(array[i],array[j]);
                j--;
            }
            else i++;
        }  
    }
};
