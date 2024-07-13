import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] graph = new int[9][9];

        for (int i = 0; i < 9; i++) {
            graph[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        int answer = -1;
        int row = 0;
        int column = 0;
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (graph[r][c] > answer) {
                    answer = graph[r][c];
                    row = r;
                    column = c;
                }
            }
        }

        System.out.println(answer);
        System.out.println((row + 1) + " " + (column + 1));
    }
}