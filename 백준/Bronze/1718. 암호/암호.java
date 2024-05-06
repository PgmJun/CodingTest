import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<Integer, Character> asciiToCharMap = new HashMap<>();
        HashMap<Character, Integer> charToAsciiMap = new HashMap<>();
        int index = 1;
        for (char c = 'a'; c <= 'z'; c++) {
            asciiToCharMap.put(index, c);
            charToAsciiMap.put(c, index++);
        }

        String inputValue = br.readLine();
        char[] values = new char[inputValue.length()];
        for (int i = 0; i < inputValue.length(); i++) {
            values[i] = inputValue.charAt(i);
        }

        String secretValue = br.readLine();
        char[] secretKeys = new char[secretValue.length()];
        for (int i = 0; i < secretValue.length(); i++) {
            secretKeys[i] = secretValue.charAt(i);
        }

        int secretKeyLength = secretKeys.length;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            if (values[i] == ' ') {
                sb.append(" ");
                continue;
            }

            int valueAscii = charToAsciiMap.get(values[i]);
            int secretKeyAscii = charToAsciiMap.get(secretKeys[i % secretKeyLength]);
            // c: 3 v: 22 3-22 = -19
            int keyIndex = (valueAscii - secretKeyAscii);
            if(keyIndex == 0) {
                keyIndex = 26;
            }
            if (keyIndex < 0) {
                keyIndex = 26 + keyIndex;
            }

            sb.append(asciiToCharMap.get(keyIndex));
        }

        System.out.println(sb);
    }
}