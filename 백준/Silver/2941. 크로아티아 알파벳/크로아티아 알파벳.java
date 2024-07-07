import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;

        List<String> singleCroatiaWords = List.of("dz=", "lj", "nj");
        List<String> croatiaWords = List.of("c=", "c-", "d-", "s=", "z=");


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        for (String singleCroatiaWord : singleCroatiaWords) {
            input = input.replace(singleCroatiaWord, "*");
        }
        for (String word : input.split("")) {
            if (word.equals("*")) {
                answer++;
            }
        }
        input = input.replace("*", "");

        Set<Integer> croatiaWordIdx = new HashSet<>();
        for (String croatiaWord : croatiaWords) {
            int wordLength = croatiaWord.length();

            for (int i = 0; i <= input.length() - wordLength; i++) {
                String slice = input.substring(i, i + wordLength);
                if (croatiaWord.equals(slice)) {
                    answer++;
                    for (int j = i; j < i + wordLength; j++) {
                        croatiaWordIdx.add(j);
                    }
                }
            }
        }
        answer += input.length() - croatiaWordIdx.size();

        System.out.println(answer);
    }
}