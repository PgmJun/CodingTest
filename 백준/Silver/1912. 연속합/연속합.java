import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");

        int[] arr = new int[n + 1];
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(s[i - 1]);
        }
        dp[1] = arr[1];


        for (int i = 2; i <= n; i++) {
            if (dp[i - 1] + arr[i] > arr[i]) {
                dp[i] = dp[i - 1] + arr[i];
            } else {
                dp[i] = arr[i];
            }
        }

        int result = Integer.MIN_VALUE;
        for(int i = 1; i <= n; i++){
            result = Math.max(result, dp[i]);
        }
        System.out.println(result);
    }
}