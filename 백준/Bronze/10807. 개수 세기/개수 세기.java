import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));;

        String n = br.readLine();
        String[] values = br.readLine().split(" ");
        String v = br.readLine();

        for (String value : values) {
            if(value.equals(v)) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}