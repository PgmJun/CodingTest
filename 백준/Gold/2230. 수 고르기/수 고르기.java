import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int start = 0;
        int end = 1;

        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(arr);

        int answer = Integer.MAX_VALUE;
        if(n == 1) {
            System.out.println(0);
            return;
        }

        while (start < n && end < n) {
            int diff = arr.get(end) - arr.get(start);
            if (diff >= m) {
                start++;
                answer = Math.min(answer, diff);
            } else {
                end++;
            }

        }

        System.out.println(answer);
        br.close();
    }
}
