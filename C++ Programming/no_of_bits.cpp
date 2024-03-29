class Solution {
  public:
    int setBits(int N) {
        int count = 0;
        while(N) {
            int last_bit = (N & 1);
            count += last_bit;
            // discard last bit
            N = N >> 1;
        }
        return count;
    }
};
