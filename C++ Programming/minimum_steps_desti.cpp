
class Solution {
  public:
    int minSteps(int D) {
        int sum=0;
        int steps=0;
        for(steps=1;sum<D;steps++)sum+=steps;
        if(sum==D)return steps-1;
        else if(!((sum-D)&1))return steps-1;
        else if(!((sum-D+steps)&1))return steps;
        else if(!((sum-D+steps+steps+1)&1))return steps+1;
        return -1;
    }
};
