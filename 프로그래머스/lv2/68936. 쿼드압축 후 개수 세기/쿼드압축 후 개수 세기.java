class Solution {
    private static int[] answer = {0, 0};

	public static int[] solution(int[][] arr) {
		// 재귀를 통해 풀이
		// 탐색 후 전부 같은 값이 아니면 4분할
		// 전부 같은 값이면 맨위 오른쪽 값의 count를 +1 한 후 return하여 탐색 종료
		quad(0, 0, arr.length, arr);
		System.out.println();
		return answer;
	}

	private static boolean zip(int x, int y, int size, int val, int[][] arr) {
		for (int i = x; i < x + size; i++) {
			for (int j = y; j < y + size; j++) {
				if (arr[j][i] != val) {
					return false;
				}
			}
		}
		return true;
	}

	private static void quad(int x, int y, int size, int[][] arr) {
		if (zip(x, y, size, arr[y][x], arr)) {
			if (arr[y][x] == 0) {
				answer[0]++;
			} else {
				answer[1]++;
			}
			return;
		}

		quad(x, y, size / 2, arr);
		quad(x + size / 2, y, size / 2, arr);
		quad(x, y + size / 2, size / 2, arr);
		quad(x + size / 2, y + size / 2, size / 2, arr);
	}
}