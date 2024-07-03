import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int bucketCount = Integer.parseInt(nm[0]);
        int count = Integer.parseInt(nm[1]);

        int[] bucket = new int[bucketCount];
        for (int i = 0; i < bucketCount; i++) {
            bucket[i] = i + 1;
        }

        for (int i = 0; i < count; i++) {
            String[] fromTo = br.readLine().split(" ");
            int from = Integer.parseInt(fromTo[0]) - 1;
            int to = Integer.parseInt(fromTo[1]) - 1;

            if (from == to) {
                continue;
            }

            int end = to;
            for (int j = from; j <= (from + to) / 2; j++) {
                int temp = bucket[end];
                bucket[end] = bucket[j];
                bucket[j] = temp;
                end--;
            }
        }

        for (int value : bucket) {
            System.out.print(value + " ");
        }
    }
}