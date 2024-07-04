import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<String, Integer> dialMap = new HashMap<>();

        dialMap.put("A", 3);
        dialMap.put("B", 3);
        dialMap.put("C", 3);

        dialMap.put("D", 4);
        dialMap.put("E", 4);
        dialMap.put("F", 4);

        dialMap.put("G", 5);
        dialMap.put("H", 5);
        dialMap.put("I", 5);

        dialMap.put("J", 6);
        dialMap.put("K", 6);
        dialMap.put("L", 6);

        dialMap.put("M", 7);
        dialMap.put("N", 7);
        dialMap.put("O", 7);

        dialMap.put("P", 8);
        dialMap.put("Q", 8);
        dialMap.put("R", 8);
        dialMap.put("S", 8);

        dialMap.put("T", 9);
        dialMap.put("U", 9);
        dialMap.put("V", 9);

        dialMap.put("W", 10);
        dialMap.put("X", 10);
        dialMap.put("Y", 10);
        dialMap.put("Z", 10);

        int answer = 0;
        String[] input = br.readLine().split("");
        for (String value : input) {
            answer += dialMap.get(value);
        }

        System.out.println(answer);
    }
}