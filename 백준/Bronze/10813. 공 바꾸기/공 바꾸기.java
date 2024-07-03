import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int ballCount = Integer.parseInt(nm[0]);
        int count = Integer.parseInt(nm[1]);

        int[] bucket = new int[ballCount];
        for (int i = 1; i <= ballCount; i++) {
            bucket[i - 1] = i;
        }

        for (int i = 0; i < count; i++) {
            String[] fromTo = br.readLine().split(" ");
            int from = Integer.parseInt(fromTo[0]) - 1;
            int to = Integer.parseInt(fromTo[1]) - 1;

            int fromTemp = bucket[from];
            bucket[from] = bucket[to];
            bucket[to] = fromTemp;
        }

        for (int value : bucket) {
            System.out.print(value + " ");
        }
    }
}