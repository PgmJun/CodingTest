import java.util.Arrays;

class Solution {
    public static int[] solution(String s) {
		int[] answer = new int[s.length()];
		Arrays.fill(answer, -1);

		for (int i = 0; i < s.length(); i++) {
			char now = s.charAt(i);
			for(int j = i-1; j >= 0; j--) {
				if(s.charAt(j) == now) {
					answer[i] = i-j;
					break;
				}
			}
		}
		System.out.println();
		return answer;
	}
}