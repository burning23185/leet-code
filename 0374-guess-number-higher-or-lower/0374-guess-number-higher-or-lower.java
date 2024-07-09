/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 0;
        int right = n;
        int mid = 1;
        int res;
        while(left <= right){
            mid = left + (right - left)/2;
            res = super.guess(mid);
            if(res == 0) break;
            if(res == -1){
                right = mid - 1;
                continue;
            }
            left = mid + 1;
        }
        return mid;
    }
}