import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[1001];

        int[] cards = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::valueOf)
                .toArray();

        dp[1] = cards[0];

        for(int i = 2; i <= n; i++) {
            dp[i] = cards[i-1];
            for(int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[i-j] + dp[j], dp[i]);
            }
        }

        System.out.println(dp[n]);
    }
}
