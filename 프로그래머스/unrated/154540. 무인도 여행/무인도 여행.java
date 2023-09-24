import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Queue;

class Solution {
    private static final int[] dy = {0, 0, 1, -1};
	private static final int[] dx = {1, -1, 0, 0};
	private static int mapX;
	private static int mapY;

	public static int[] solution(String[] maps) {
		int[] answer = {};
		mapX = maps[0].length();
		mapY = maps.length;
		boolean[][] visited = new boolean[maps.length][maps[0].length()];

		List<Integer> result = new ArrayList<>(); 

		for (int i = 0; i < maps.length; i++) {
			for (int j = 0; j < maps[0].length(); j++) {
				if (maps[i].charAt(j) != 'X' && !visited[i][j]) {
					int stayDays = bfs(maps, i, j, visited);
					result.add(stayDays);
				}
			}
		}
		
		if(result.isEmpty()) {
			answer = new int[] {-1};
		} else {
			Collections.sort(result);
			answer = new int[result.size()];
			for (int i = 0; i < result.size(); i++) {
				answer[i] = result.get(i);
			}
		}

		return answer;
	}

	private static int bfs(String[] maps, int y, int x, boolean[][] visited) {
		int stayDays = 0;

		Queue<Node> q = new ArrayDeque();
		q.add(new Node(y, x));
		visited[y][x] = true;

		while (!q.isEmpty()) {
			Node now = q.poll();
			int nowX = now.x;
			int nowY = now.y;
			stayDays += Integer.parseInt(String.valueOf(maps[nowY].charAt(nowX)));

			for (int i = 0; i < 4; i++) {
				int nextX = nowX + dx[i];
				int nextY = nowY + dy[i];

				if (nextY < 0 || nextY >= mapY || nextX < 0 || nextX >= mapX || maps[nextY].charAt(nextX) == 'X') {
					continue;
				}
				if (!visited[nextY][nextX]) {
					visited[nextY][nextX] = true;
					q.add(new Node(nextY, nextX));
				}
			}
		}

		return stayDays;
	}

	private static class Node {
		private int y;
		private int x;

		Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
}