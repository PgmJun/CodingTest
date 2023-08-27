import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static ArrayList<ArrayList<Town>> graph = new ArrayList<>();

	public static void main(String[] args) throws IOException {

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()); // 마을의 갯수
		int m = Integer.parseInt(st.nextToken()); // 단방향 도로의 갯수
		int x = Integer.parseInt(st.nextToken()); // 파티하는 마을

		for (int i = 0; i <= n; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int delay = Integer.parseInt(st.nextToken());
			graph.get(a).add(new Town(b, delay));
		}

		int[] toHomeDistances = dijkstra(x, n); // 도시 별, 파티장소까지의 거리 구하기
		int answer = -1;
		for(int i = 1; i <= n; i++) {
			int[] toPartyDistances = dijkstra(i, n);
			int totalDistance = toHomeDistances[i] + toPartyDistances[x];

			if(totalDistance > answer) {
				answer = totalDistance;
			}
		}
		System.out.println(answer);

	}

	private static int[] dijkstra(int start, int townCount) {
		PriorityQueue<Town> pq = new PriorityQueue<>();
		int[] delays = new int[townCount + 1];
		Arrays.fill(delays, Integer.MAX_VALUE);

		delays[start] = 0;
		pq.offer(new Town(start, 0));

		while (!pq.isEmpty()) {
			Town now = pq.poll();
			int nowDelay = now.delay;
			int nowNumber = now.number;

			if(delays[now.number] < nowDelay) {
				continue;
			}

			for (Town next : graph.get(nowNumber)) {
				int delay = next.delay + nowDelay;
				if(delay < delays[next.number]) {
					delays[next.number] = delay;
					pq.offer(new Town(next.number, delay));
				}
			}
		}

		return delays;
	}

	private static class Town implements Comparable<Town> {
		private int number;
		private int delay;

		Town(int number, int delay) {
			this.number = number;
			this.delay = delay;
		}

		@Override
		public int compareTo(Town o) {
			return this.delay - o.delay;
		}
	}

}