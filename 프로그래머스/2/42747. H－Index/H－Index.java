import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int maxCitation = citations[citations.length - 1];
        int citationsCount = citations.length;
        for (int h = 1; h < maxCitation; h++) {
            int hIndex = h;
            long citationCountQuotedMoreH = Arrays.stream(citations)
                    .filter(c -> c >= hIndex)
                    .count();
            long citationCountQuotedLessH = citationsCount - citationCountQuotedMoreH;
            if (citationCountQuotedMoreH >= h && citationCountQuotedLessH <= h) {
                answer = Math.max(answer, hIndex);
            }
        }
        return answer;
    }
}