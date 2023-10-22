class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] dp = new int[n+1];
        if(n > 0) {
            dp[1] = 1;
        }
        if(n > 1) {
            dp[2] = 2;
        }

        if(n > 2) {
            for(int i = 3; i <= n; i++) {
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;
            }
        }
        
        return dp[n];
        
    }
    // 0 0
    // 1 1
    // 2 2
    // 3 3
    // 4 5
    // 5 8
}