import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[10001];

        int[] wine = new int[n+1];
        for (int i = 1; i <= n; i++) {
            wine[i] = Integer.parseInt(br.readLine());
        }

        dp[1] = wine[1];
        if (n > 1) {
            dp[2] = dp[1] + wine[2];
            for (int i = 3; i <= n; i++) {
                dp[i] = Math.max(Math.max(dp[i - 1], dp[i - 2] + wine[i]), dp[i - 3] + wine[i - 1] + wine[i]);
            }
        }

        System.out.println(dp[n]);
    }
}