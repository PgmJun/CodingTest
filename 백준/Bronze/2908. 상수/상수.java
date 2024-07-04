import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ab = br.readLine().split(" ");
        String a = ab[0];
        String b = ab[1];

        int aValue = Integer.parseInt(new StringBuilder(a).reverse().toString());
        int bValue = Integer.parseInt(new StringBuilder(b).reverse().toString());

        if(aValue > bValue) {
            System.out.println(aValue);
        } else {
            System.out.println(bValue);
        }
    }
}