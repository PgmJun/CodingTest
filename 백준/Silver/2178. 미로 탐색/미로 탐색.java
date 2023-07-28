import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {

	public static int MAX = 101;
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static Queue<Node> queue = new ArrayDeque<>();
	public static int[][] graph = new int[MAX][MAX];
	public static boolean[][] visited = new boolean[MAX][MAX];

	public static int[] dx = {-1, 1, 0, 0};
	public static int[] dy = {0, 0, -1, 1};
	

	public static void main(String[] args) throws IOException {
		String[] input = br.readLine().split(" ");
		int n = StringToInt(input[0]),
			m = StringToInt(input[1]);

		initGraph(n);
		initVisited();
		bfs(new Node(1, 1, 1), n, m);

	}

	public static void bfs(Node start, int n, int m) {
		queue.add(start);

		while (queue.peek() != null) {
			Node now = queue.poll();
			int x = now.getX();
			int y = now.getY();
			int depth = now.depth;

			if (x == n && y == m) {
				System.out.print(depth);
				break;
			}

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx <= 0 || nx > n || ny <= 0 || ny > m) {
					continue;
				}
				if (visited[nx][ny]) {
					continue;
				}
				if (graph[nx][ny] == 0) {
					continue;
				}

				visited[nx][ny] = true;
				queue.add(new Node(nx, ny, depth + 1));
			}
		}
	}

	private static void initGraph(int n) throws IOException {
		for (int i = 1; i < n + 1; i++) {
			int j = 1;
			for (String v : br.readLine().split("")) {
				graph[i][j++] = StringToInt(v);
			}
		}
	}

	private static void initVisited() {
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				visited[i][j] = false;
			}
		}
	}

	private static int StringToInt(String value) {
		return Integer.parseInt(value);
	}

}

class Node {
	int x;
	int y;
	int depth;

	public Node(int x, int y, int depth) {
		this.x = x;
		this.y = y;
		this.depth = depth;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public int getDepth() {
		return depth;
	}
}
