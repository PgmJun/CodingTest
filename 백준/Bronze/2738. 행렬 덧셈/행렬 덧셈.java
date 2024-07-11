import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int[][] a = new int[n][m];
        for(int i = 0; i < n; i++) {
            String[] inputA = br.readLine().split(" ");
            for(int j = 0; j < inputA.length; j++) {
                a[i][j] = Integer.parseInt(inputA[j]);
            }
        }

        int[][] b = new int[n][m];
        for(int i = 0; i < n; i++) {
            String[] inputB = br.readLine().split(" ");
            for(int j = 0; j < inputB.length; j++) {
                b[i][j] = Integer.parseInt(inputB[j]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                sb.append(a[i][j] + b[i][j]);
                sb.append(' ');
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }
}