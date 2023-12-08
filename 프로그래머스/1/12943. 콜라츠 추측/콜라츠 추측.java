class Solution {
    public int solution(int num) {
        int answer = 0;
        int tryCount = 0;
        while(true) {
            if(tryCount == 500) {
                answer = -1;
                break;
            }
            if(num == 1) {
                answer = tryCount;
                break;
            }
            if(num % 2 == 0) {
                num /= 2;
            } else if(num % 2 == 1) {
                num *= 3;
                num += 1;
            }
            tryCount++;
        }
        
        return answer;
    }
}