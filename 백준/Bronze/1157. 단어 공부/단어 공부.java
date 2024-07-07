import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();
        String[] words = input.split("");

        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        LinkedList<Map.Entry<String, Integer>> entries = new LinkedList<>(wordMap.entrySet());
        entries.sort(new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return o2.getValue() - o1.getValue();
            }
        });

        String answer = "";
        int maxSize = entries.getFirst().getValue();
        if (entries.size() == 1) {
            answer = entries.getFirst().getKey();
        } else if (entries.size() > 1) {
            if (entries.get(1).getValue() == maxSize) {
                answer = "?";
            } else {
                answer = entries.getFirst().getKey();
            }
        }

        System.out.println(answer);
    }
}