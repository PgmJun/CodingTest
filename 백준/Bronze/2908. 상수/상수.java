import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ab = br.readLine().split(" ");
        String[] a = ab[0].split("");
        String[] b = ab[1].split("");

        int reserveA = Integer.parseInt(a[2] + a[1] + a[0]);
        int reserveB = Integer.parseInt(b[2] + b[1] + b[0]);

        if(reserveA > reserveB) {
            System.out.println(reserveA);
        } else {
            System.out.println(reserveB);
        }
    }
}