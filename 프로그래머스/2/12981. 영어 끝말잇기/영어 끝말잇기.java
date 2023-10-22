import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] solution(int n, String[] words) {
        int who = 0;
        int turn = 0;
        String beforeWord = "";
        boolean isFinish = false;
        Set<String> beforeWords = new HashSet<>();

        for (int t = 0; t < words.length/n; t++) {
            for (int i = 0; i < n; i++) {
                // 첫 번은 before에 저장만 하고 패스
                if(t == 0 && i == 0) {
                    beforeWord = words[0];
                    beforeWords.add(beforeWord);
                    continue;
                }

                int now = (t * n) + i;
                if (isNotSameBeforeLastWordAndNowFirstWord(beforeWord, words[now]) || isWordDuplicate(beforeWords, words[now])) {
                    who = i+1;
                    turn = t+1;
                    isFinish = true;
                    break;
                }
                beforeWords.add(words[now]);
                beforeWord = words[now];
            }
            if(isFinish) {
                break;
            }
        }

        return new int[] {who, turn};
    }
    
    private boolean isWordDuplicate(Set<String> beforeWords, String words) {
        return beforeWords.contains(words);
    }

    private boolean isNotSameBeforeLastWordAndNowFirstWord(String before, String words) {
        return words.charAt(0) != before.charAt(before.length() - 1);
    }
}