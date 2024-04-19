import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        List<Integer> arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::valueOf)
                .boxed()
                .collect(Collectors.toList());
        Collections.sort(arr);

        // 1 2 3 4 5 7
        int s = 0;
        int e = n - 1;
        while (s < e) {
            int sum = arr.get(s) + arr.get(e);
            if (sum == m) {
                answer++;
                s++;
            } else if (sum > m) {
                e--;
            } else {
                s++;
            }
        }

        System.out.println(answer);
    }
}