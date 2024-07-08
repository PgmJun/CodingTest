import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            boolean isGroupWord = true;
            String[] words = br.readLine().split("");
            String before = "";
            Set<String> beforeWords = new HashSet<>();

            for (int j = 1; j < words.length; j++) {
                before = words[j - 1];
                beforeWords.add(words[j - 1]);

                String now = words[j];
                if (beforeWords.contains(now) && !before.equals(now)) {
                    isGroupWord = false;
                    break;
                }
            }

            if(isGroupWord) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}