import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static ArrayList<ArrayList<Computer>> graph;

	public static void main(String[] args) throws IOException {
		int t = Integer.parseInt(br.readLine());

		for (int i = 0; i < t; i++) {
			graph = new ArrayList<>();

			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken()); // 컴퓨터 갯수
			int d = Integer.parseInt(st.nextToken()); // 의존성 갯수
			int c = Integer.parseInt(st.nextToken()); // 해킹당한 컴퓨터 number


			for(int j = 0; j <= n; j++) {
				graph.add(new ArrayList<>());
			}

			for (int j = 0; j < d; j++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken()); // 컴퓨터 A
				int b = Integer.parseInt(st.nextToken()); // 컴퓨터 B
				int s = Integer.parseInt(st.nextToken()); // 바이러스 딜레이

				graph.get(b).add(new Computer(a, s));
			}

			int[] result = dijkstra(c, n);
			int cnt = 0;
			int delay = 0;
			for(int k = 0; k < result.length; k++) {
				if(result[k] != Integer.MAX_VALUE) {
					delay = Math.max(delay, result[k]);
					cnt++;
				}
			}

			System.out.println(cnt + " " + delay);

		}
	}

	private static int[] dijkstra(int start, int n) {
		PriorityQueue<Computer> pq = new PriorityQueue<>();
		int[] delays = new int[n+1];
		Arrays.fill(delays, Integer.MAX_VALUE);

		delays[start] = 0;
		pq.offer(new Computer(start, 0));

		while(!pq.isEmpty()) {
			Computer now = pq.poll();
			int nNumber = now.number;
			int nVirusDelay = now.virusDelay;

			if(nVirusDelay > delays[nNumber]) {
				continue;
			}

			for (Computer next : graph.get(nNumber)) {
				int delay = next.virusDelay + nVirusDelay;

				if(delay < delays[next.number]) {
					delays[next.number] = delay;
					pq.offer(new Computer(next.number, delay));
				}
			}
		}

		return delays;
	}

	private static class Computer implements Comparable<Computer>{
		private int number;
		private int virusDelay;

		Computer(int number, int virusDelay) {
			this.number = number;
			this.virusDelay = virusDelay;
		}

		@Override
		public int compareTo(Computer o) {
			return this.virusDelay - o.virusDelay;
		}
	}
}