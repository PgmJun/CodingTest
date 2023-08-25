
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class Main {

	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static LinkedList<LinkedList<Edge>> graph = new LinkedList<>();
	private static final int[] dx = {0,0,-1,1};
	private static final int[] dy = {-1,1,0,0};

	public static void main(String[] args) throws IOException {
		int k = 1;
		while (true) {
			// n입력받기
			int n = Integer.parseInt(br.readLine());
			if (n == 0) {
				break;
			}
			graph = new LinkedList<>();
			//그래프 초기화
			for(int i = 0; i < n;i++){
				graph.add(new LinkedList<>());
			}


			for (int i = 0; i < n; i++) {
				String[] costs = br.readLine().split(" ");
				for(int j = 0; j < n; j++) {
					int cost = Integer.parseInt(costs[j]);
					graph.get(i).add(new Edge(i, j, cost));
				}
			}

			System.out.println("Problem "+(k++)+": "+dijkstra(n));

		}
	}

	private static int dijkstra(int n) {
		PriorityQueue<Edge> pq = new PriorityQueue();
		int[][] costs = new int[n][n];
		for(int i = 0; i < n; i++) {
			Arrays.fill(costs[i], Integer.MAX_VALUE);
		}
		costs[0][0] = graph.get(0).get(0).cost;

		pq.offer(new Edge(0, 0, graph.get(0).get(0).cost));

		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			int nowX = now.x;
			int nowY = now.y;
			int nCost = now.cost;

			if (nCost > costs[nowY][nowX]) {
				continue;
			}

			for (int i = 0; i < 4; i++) {
				int ny = nowY + dy[i];
				int nx = nowX + dx[i];

				if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
					continue;
				}
				int cost = graph.get(ny).get(nx).cost + nCost;
				if (cost < costs[ny][nx]) {
					costs[ny][nx] = cost;
					pq.offer(new Edge(nx, ny, cost));
				}
			}
		}

		return costs[n-1][n-1];
	}

	private static class Edge implements Comparable<Edge> {
		int x;
		int y;
		int cost;

		Edge(int x, int y, int cost) {
			this.x= x;
			this.y =y;
			this.cost=cost;
		}

		@Override
		public int compareTo(Edge o) {
			return this.cost-o.cost;
		}
	}
}