// BFS로 학교까지 최단 경로 찾기


class Solution {
    private static int[][] map;

	public static int solution(int m, int n, int[][] puddles) {
		int answer = 0;
		initMap(m, n, puddles);

		for (int[] puddle : puddles) {
			map[puddle[1]][puddle[0]] = -1;
		}

		for (int i = 1; i <= n; i++) {
			for (int k = 1; k <= m; k++) {
				if (map[i][k] == -1) {
					continue;
				}
				if (map[i][k - 1] >= 1 && map[i - 1][k] >= 1) {
					map[i][k] = (map[i][k - 1] + map[i - 1][k]) % 1000000007;
				} else if (map[i][k - 1] >= 1 && map[i - 1][k] < 1) {
					map[i][k] = map[i][k - 1] % 1000000007;
				} else if (map[i - 1][k] >= 1 && map[i][k - 1] < 1) {
					map[i][k] = map[i - 1][k] % 1000000007;
				}
			}
		}

		return map[n][m];
	}

	private static void initMap(int m, int n, int[][] puddles) {
		map = new int[n + 1][m + 1];
		map[1][1] = 1;
		for (int[] puddle : puddles) {
			map[puddle[1]][puddle[0]] = -1;
		}
	}
}