import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int s = Integer.parseInt(input[1]);

        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(arr);

        // 3 3 4 5 6 7 8
        int start = 0;
        int end = n - 1;
        while (start < end) {
            int sum = arr.get(start) + arr.get(end);
            if(sum > s) {
                end--;
            } else {
                answer += end - start;
                start++;
            }
        }
        System.out.println(answer);
    }
}