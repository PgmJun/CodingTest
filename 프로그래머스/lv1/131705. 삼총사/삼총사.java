import java.util.Arrays;

class Solution {
    static int answer = 0;
	public static int solution(int[] number) {

		int[] result = new int[number.length];

		boolean[] visited = new boolean[number.length];
		combination(0,0, result, number);

		return answer;
	}

	// 조합 메서드(cnt는 선택 횟수, idx는 다음 대상을 선택할때 집합에서 탐색을 시작할 인덱스).
	private static void combination(int cnt, int idx, int[] result, int[] target) {
		// 2개를 선택했으므로, 결과를 출력하고 재귀를 종료한다.
		if (cnt == 3) {
			if(Arrays.stream(result).sum() == 0) {
				answer++;
			}
			return;
		}
		// 대상 집합을 주어진 인덱스부터 순회하며 숫자를 하나 선택한다.
		for (int i = idx; i < target.length; i++) {
			// 숫자를 담는다.
			result[cnt] = target[i];
			// 자신을 재귀 호출한다(자신 이전의 수를 중복 선택하지 않도록 인덱스를 +1하여 재귀를 호출한다).
			combination(cnt + 1, i + 1, result, target);
		}
	}
}