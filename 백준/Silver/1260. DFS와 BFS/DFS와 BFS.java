import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

class Main {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
	public static Queue<Integer> queue = new ArrayDeque<>();
	public static boolean[] visited;

	public static void bfs(int v) {
		queue.add(v);
		visited[v] = true;

		while (queue.peek() != null) {
			int now = queue.poll();
			System.out.print(now + " ");

			for (int p : graph.get(now)) {
				if (!visited[p]) {
					visited[p] = true;
					queue.add(p);
				}
			}
		}
	}

	public static void dfs(int v) {
		visited[v] = true;
		System.out.print(v + " ");

		for (int p : graph.get(v)) {
			if (!visited[p]) {
				dfs(p);
			}
		}

	}

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().split(" ");
		int n = StringToInt(input[0]),
			m = StringToInt(input[1]),
			v = StringToInt(input[2]);

		generateGraph(m, n);
		sortGraph(n);

		resetVisited(n);
		dfs(v);
		printEnter();
		resetVisited(n);
		bfs(v);

	}

	private static void sortGraph(int n) {
		for (int i = 1; i <= n; i++) {
			Collections.sort(graph.get(i));
		}
	}

	private static void printEnter() {
		System.out.println();
	}

	private static void resetVisited(int n) {
		visited = new boolean[n + 1];
	}

	private static void generateGraph(int m, int n) throws IOException {
		for (int i = 0; i < n + 1; i++) {
			graph.put(i, new ArrayList<>());
		}

		int a, b;
		for (int i = 0; i < m; i++) {
			String[] points = br.readLine().split(" ");
			a = StringToInt(points[0]);
			b = StringToInt(points[1]);

			graph.get(a).add(b);
			graph.get(b).add(a);
		}
	}

	private static int StringToInt(String value) {
		return Integer.parseInt(value);
	}

}
