import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            int mid = 2 * i - 1;
            int left = n - i;
            for (int j = 0; j < left; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < mid; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = n - 1; i > 0; i--) {
            int mid = 2 * i - 1;
            int left = n - i;
            for (int j = 0; j < left; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < mid; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}