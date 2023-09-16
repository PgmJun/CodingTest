class Solution {
    public int[] solution(int n) {
		int[] answer = {};
		int[][] graph = new int[n][n];

		if (n == 1) {
			return new int[] {1};
		}

		int y = 0;
		int x = 0;
		int val = 1;
		int count = 0;
		boolean fin = false;
		while (true) {

			count++;
			while (y < n && graph[y][x] == 0) {
				graph[y++][x] = val++;
			}
			y--;
			if(count == n) {
				break;
			}

			x++;
			count++;
			while (x < n && graph[y][x] == 0) {
				graph[y][x++] = val++;
			}
			if(count == n) {
				break;
			}
			x--;


			x--;
			y--;
			count++;
			while(x > 0 && y > 0 && graph[y][x] == 0) {
				graph[y--][x--] = val++;
			}
			if(count == n) {
				break;
			}
			x++;
			y++;

			y++;
		}

		int len = 0;

		for(int i = 0; i < n; i++) {
			for(int j = 0; j <= i; j++) {
				len++;
			}
		}
		answer = new int[len];
		int idx = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j <= i; j++) {
				answer[idx++] = graph[i][j];
			}
		}

		return answer;
	}
}