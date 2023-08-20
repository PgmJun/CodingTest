import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static long[] dp;

	public static void main(String[] args) throws IOException {
        // 피보나치 수를 특정 수로 나눌 때, 같은 값이 반복되는 주기를 피사노 주기(pisano period)라고 함.
        // 1000000의 피사노 주기는 1500000
        // 때문에 1500000까지의 값만 구하면 되며
        // dp[(n % 1500000)]의 값을 출력하면 됨
        
		int pisano = 1500000;
		long size = Long.parseLong(br.readLine()) % pisano;
		dp = new long[pisano + 1];
		dp[1] = 1;

		for (int i = 2; i <= pisano; i++) {
			dp[i] = (dp[i-1] + dp[i-2]) % 1000000;
		}
		System.out.println(dp[(int)size]);
	}
}