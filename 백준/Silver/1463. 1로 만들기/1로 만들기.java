
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		int x = input();
		int[] dp = new int[x+1];
		initDp(dp, x);

		for (int i = 2; i < x+1; i++) {
			dp[i] = dp[i-1]+1;
			if (i % 2 == 0) {
				dp[i] = Math.min(dp[i], dp[i/2]+1);
			}
			if (i % 3 == 0) {
				dp[i] = Math.min(dp[i], dp[i/3]+1);
			}
		}

		System.out.print(dp[x]);

	}

	private static int input() throws IOException {
		return Integer.parseInt(br.readLine());
	}

	private static void initDp(int[] dp, int x) {
		for (int i = 0; i < x+1; i++) {
			dp[i] = 0;
		}
	}
}
