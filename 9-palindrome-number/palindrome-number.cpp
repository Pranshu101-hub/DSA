#include <cmath>
class Solution {
public:
    int digits(int x){
        int d = 0;
        while (x){
            x = x / 10;
            d = d + 1;
        }
        return d;
    }
    bool isPalindrome(int x) {
        if (x < 0) return false;

        int d = digits(x);

        while (d > 1) {
            int unit = x % 10;                         // last digit
            int ending = x / (int)pow(10, d - 1);     // first digit

            if (unit != ending) {
                return false;
            }

            // remove first digit
            x = x % (int)pow(10, d - 1);
            // remove last digit
            x = x / 10;

            d -= 2;
        }
        return true;
    }
};