import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] score = new int[n + 1];
        for (int i = 0; i < n; i++) {
            score[i + 1] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[301];
        dp[1] = score[1];
        if (n > 1) {
            dp[2] = score[1] + score[2];
        }
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i];
        }
        System.out.println(dp[n]);
    }
}
