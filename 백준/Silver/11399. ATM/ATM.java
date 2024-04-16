import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * n명의 사람의 인출 필요 시간이 주어졌을 때, 필요한 시간의 최솟값
 * 1+2+3+3+4 -> 1+3+6+9+13 = 32
 * <p>
 * 해결 방안
 * 오름차순 정렬 후, 작은쪽부터 큰쪽으로 더해나가기
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::valueOf)
                .boxed()
                .collect(Collectors.toList());

        Collections.sort(arr);
        int sum = 0; // 1 3
        int answer = 0;
        for (int v : arr) {
            sum += v;
            answer += sum;
        }
        System.out.println(answer);
    }
}