
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[1000001];

		dp[2] = 1;
		dp[3] = 1;

		for (int i = 4; i <= n; i++) {
			dp[i] = dp[i-1]+1;
			if(i % 2 == 0) {
				dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
			} if(i % 3 == 0) {
				dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
			}
		}

		System.out.println(dp[n]);
	}
}