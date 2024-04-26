import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> values = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            values.add(Integer.parseInt(input));
        }

        Set<Integer> unDuplValues = new HashSet<>(values);
        int maxCount = Integer.MIN_VALUE;

        for (int excludeValue : unDuplValues) {
            int count = 1;
            int before = -1;
            for(int i = 0; i < values.size(); i++){
                int now = values.get(i);
                if (now == excludeValue) {
                    continue;
                }
                if (now != before) {
                    count = 1;
                    before = now;
                } else {
                    count++;
                }
                maxCount = Math.max(maxCount, count);
            }
        }

        System.out.println(maxCount);
    }
}
