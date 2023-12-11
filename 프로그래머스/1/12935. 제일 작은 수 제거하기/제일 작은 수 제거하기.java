import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1) {
            return new int[]{-1};
        }
        int minValue = Arrays.stream(arr)
                .min()
                .getAsInt();

        int[] answer = new int[arr.length - 1];

        int i = 0;
        for (int v : arr) {
            if(v == minValue) continue;
            answer[i++] = v;
        }
        
        return answer;
    }
}