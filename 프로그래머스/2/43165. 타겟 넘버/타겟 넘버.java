class Solution {
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        find(0, 0, numbers, target);
        return answer;
    }

    public void find(int idx, int v, int[] numbers, int target) {
        if (idx == numbers.length) {
            if (v == target) {
                answer++;
            }
        } else {
            find(idx + 1, v + numbers[idx], numbers, target);
            find(idx + 1, v - numbers[idx], numbers, target);
        }
    }
}