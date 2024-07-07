import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException {
        int c = System.in.read();
        int[] arr = new int[26];
        while(c > 64) {
            if(c < 91) {
                arr[c-65]++;
            } else {
                arr[c-97]++;
            }
            c = System.in.read();
        }

        int max = -1;
        int answer = -2;
        for(int i = 0; i < 26; i++) {
            if(arr[i] > max) {
                answer = i;
                max = arr[i];
            } else if(arr[i] == max) {
                answer = -2;
            }
        }

        System.out.println((char)(answer + 65));
    }
}
