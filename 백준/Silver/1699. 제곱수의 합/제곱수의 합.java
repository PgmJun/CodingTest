import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // dp[i] : i의 최소 제곱수 합 항의 개수
        int[] dp = new int[100001];
        dp[1] = 1;

        for(int i = 1; i <= n; i++) {
            // 초기값: 1제곱이 i개인 경우
            dp[i] = i;
            for(int j = 1; j * j <= i; j++) {
                // 만약 i보다 작은 제곱수를 뺀 것에 +1 한 값이 dp[i]보다 작다면 dp[i] 교체
                // ex) i == 17 일때 i보다 작은 제곱값들인 1 2 4 9 16 을 뺀 dp[16], dp[15], dp[13], dp[8], dp[1] 의 값에 + 1한 값들을 dp[i]와 비교
                if(dp[i - j * j] + 1 < dp[i]) {
                    dp[i] = dp[i - j * j] + 1;
                }
            }
        }
        System.out.println(dp[n]);
    }
}
