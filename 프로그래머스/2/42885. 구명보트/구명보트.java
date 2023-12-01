import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        // 정렬
        Arrays.sort(people);
        int l = 0;
        int r = people.length - 1;

        while (true) {
            if(l == r) {
                answer++;
                break;
            } else if(l > r) {
                break;
            }
            if (people[l] + people[r] <= limit) {
                answer++;
                l++;
                r--;
            }
            else if (people[l] + people[r] > limit) {
                answer++;
                r--;
            }
        }

        return answer;
    }
}