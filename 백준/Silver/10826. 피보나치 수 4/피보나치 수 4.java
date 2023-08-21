import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static BigInteger[] dp = new BigInteger[10001];

	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		dp[0] = BigInteger.ZERO;
		dp[1] = BigInteger.ONE;

		for (int i = 2; i <= n; i++) {
			dp[i] = dp[i-2].add(dp[i-1]);
		}
		System.out.println(dp[n]);
		
		br.close();
	}
}
