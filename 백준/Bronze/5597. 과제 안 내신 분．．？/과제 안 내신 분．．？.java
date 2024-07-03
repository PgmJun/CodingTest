import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] visited = new boolean[30];
        for (int i = 0; i < 28; i++) {
            visited[Integer.parseInt(br.readLine()) - 1] = true;
        }

        for (int i = 0; i < 30; i++) {
            if (!visited[i]) {
                System.out.println(i + 1);
            }
        }
    }
}