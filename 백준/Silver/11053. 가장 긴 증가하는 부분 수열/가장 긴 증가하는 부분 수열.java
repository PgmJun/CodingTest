import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");

        int[] arr = new int[s.length + 1];
        int[] dp = new int[n + 1];
        dp[1] = 1;

        for (int i = 1; i <= s.length; i++) {
            arr[i] = Integer.parseInt(s[i - 1]);
        }

        int result = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
            result = Math.max(result, dp[i]);
        }

        System.out.println(result);
    }
}
