import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");

        int[] bucket = new int[Integer.parseInt(nm[0])];
        int count = Integer.parseInt(nm[1]);

        for(int i = 0; i < count; i++) {
            //from ~ To 번 바구니까지 Number번 공으로 채운다.
            String[] fromToNumber = br.readLine().split(" ");
            int from = Integer.parseInt(fromToNumber[0])-1;
            int to = Integer.parseInt(fromToNumber[1])-1;
            String number = fromToNumber[2];

            for(int j = from; j <= to; j++) {
                bucket[j] = Integer.parseInt(number);
            }
        }

        for (int s : bucket) {
            if(s == 0) {
                System.out.print("0 ");
            } else {
                System.out.print(s + " ");
            }
        }
    }
}
