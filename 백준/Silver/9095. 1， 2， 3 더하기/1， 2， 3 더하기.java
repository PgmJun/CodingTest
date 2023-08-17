import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static int T;

	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());
		int[] dp = new int[12];
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 4;

		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			for (int j = 4; j <= N; j++) {
				if (dp[j] == 0) {
					dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
				}
			}

			System.out.println(dp[N]);
		}
	}
}