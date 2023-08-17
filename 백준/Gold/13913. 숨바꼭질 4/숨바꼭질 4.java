import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static int[] n, k;
	private static int[] parent = new int[100001];
	private static int[] visited = new int[100001];

	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		bfs(n, k);
		System.out.println(visited[k] - 1);

		Stack<Integer> s = new Stack<>();
		int idx = k;
		while (idx != n) {
			s.push(idx);
			idx = parent[idx];
		}
		s.push(idx);

		while (!s.isEmpty()) {
			System.out.print(s.pop() + " ");
		}
		br.close();
	}

	static void bfs(int start, int end) {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(start);
		visited[start] = 1; // 최초 방문 시간 기록

		while (!queue.isEmpty()) {
			int now = queue.poll();

			if (now + 1 <= 100000 && visited[now + 1] == 0) {
				visited[now + 1] = visited[now] + 1;
				parent[now + 1] = now;
				queue.add(now + 1);
			}
			if (now - 1 >= 0 && visited[now - 1] == 0) {
				visited[now - 1] = visited[now] + 1;
				parent[now - 1] = now;
				queue.add(now - 1);
			}
			if (now * 2 <= 100000 && visited[now * 2] == 0) {
				visited[now * 2] = visited[now] + 1;
				parent[now * 2] = now;
				queue.add(now * 2);
			}

			if (visited[end] != 0)
				return;
		}
	}
}
