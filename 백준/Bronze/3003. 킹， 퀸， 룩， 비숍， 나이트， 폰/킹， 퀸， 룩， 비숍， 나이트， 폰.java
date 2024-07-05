import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] values = br.readLine().split(" ");
        int[] count = {1, 1, 2, 2, 2, 8};

        for (int i = 0; i < values.length; i++) {
            System.out.print(count[i] - Integer.parseInt(values[i]) + " ");
        }
    }
}