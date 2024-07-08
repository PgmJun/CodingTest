import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        L:for (int i = 0; i < n; i++) {
            boolean[] isGroupWord = new boolean[27];
            String word = br.readLine();

            for (int j = 1; j < word.length(); j++) {
                if(isGroupWord[word.charAt(j) - 'a']) {
                    continue L;
                }
                if(word.charAt(j) != word.charAt(j-1)) {
                    isGroupWord[word.charAt(j-1) - 'a'] = true;
                }
            }

            answer++;
        }

        System.out.println(answer);
    }
}
