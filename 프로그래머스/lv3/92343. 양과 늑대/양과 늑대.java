class Solution {
    
	static int[] gInfo;
	static int[][] gEdges;
	static int maxSheepCount;

	public static int solution(int[] info, int[][] edges) {
		gInfo = info;
		gEdges = edges;
		boolean[] visited = new boolean[info.length];

		dfs(visited, 0,0,0);

		return maxSheepCount;
	}

	static void dfs(boolean[] visited, int idx, int sheepCount, int wolfCount) {
		visited[idx] = true;

		if(gInfo[idx] == 0) {
			sheepCount++;
			maxSheepCount = Math.max(sheepCount, maxSheepCount);
		} else if(gInfo[idx] == 1) {
			wolfCount++;
		}

		if(wolfCount >= sheepCount) {
			return;
		}

		for(int[] edge : gEdges) {
			if(visited[edge[0]] && !visited[edge[1]]) {
				boolean[] nextVisited = new boolean[visited.length];
				for (int i = 0; i < visited.length; i++) {
					nextVisited[i] = visited[i];
				}
				dfs(nextVisited, edge[1], sheepCount, wolfCount);
			}
		}
	}

}