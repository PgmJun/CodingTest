
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String args[]) throws IOException {
		Integer[] mn = input();
		int m = mn[0];
		int n = mn[1];
		int result = 0;

		Integer[] input = input();

		binarySearch(m, result, input);
	}

	private static void binarySearch(int m, int result, Integer[] input) {
		int start = 1,
			end = 1000000000;
		int mid;
		int cookieCount = 0;
		while (start <= end) {
			mid = (start + end) / 2;

			for(int i : input) {
				cookieCount += i/mid;
			}

			if(cookieCount >= m) {
				start = mid + 1;
				result = Math.max(mid, result);
			}
			else if(cookieCount < m) {
				end = mid - 1;
			}

			cookieCount = 0;
		}

		System.out.print(result);
	}

	private static Integer[] input() throws IOException {
		return Arrays.stream(br.readLine().split(" "))
			.map(Integer::parseInt)
			.toArray(Integer[]::new);
	}
}
