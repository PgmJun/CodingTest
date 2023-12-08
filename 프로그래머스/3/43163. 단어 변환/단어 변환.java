import java.util.*;

class Solution {
    public static int solution(String begin, String target, String[] words) {
        int answer = 0;

        Queue<Node> q = new ArrayDeque();
        q.add(new Node(begin, 0));
        boolean[] visited = new boolean[words.length];

        while(!q.isEmpty()) {
            Node now = q.poll();
            String word = now.word;
            int count = now.count;

            if (word.equals(target)) {
                answer = count;
                break;
            }

            for(int i = 0; i < words.length; i++) {
                if(visited[i]) {
                    continue;
                }
                if(isOneWordDifferent(word, words[i])) {
                    q.add(new Node(words[i], count + 1));
                    visited[i] = true;
                }
            }
        }

        return answer;
    }

    private static boolean isOneWordDifferent(String word1, String word2) {
        int diffCount = 0;
        for(int i = 0; i < word1.length(); i++) {
            if(word1.charAt(i) != word2.charAt(i)) {
                diffCount++;
            }
            if(diffCount > 1) {
                return false;
            }
        }
        if (diffCount == 1) {
            return true;
        }
        return false;
    }

    private static class Node {
        String word;
        int count;

        public Node(String word, int count) {
            this.word = word;
            this.count = count;
        }
    }
}