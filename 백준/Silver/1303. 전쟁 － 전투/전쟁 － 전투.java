
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static String[][] graph;
    static int n;
    static int m;
    static final int[] dirX = {0,0,-1,1};
    static final int[] dirY = {-1,1,0,0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        int whiteScore = 0;
        int blueScore = 0;

        graph = new String[m][n];
        for (int i = 0; i < m; i++) {
            String[] warriors = br.readLine().split("");
            for (int j = 0; j < warriors.length; j++) {
                graph[i][j] = warriors[j];
            }
        }


        boolean[][] visited = new boolean[m][n];
        int x = 0;
        int y = 0;


        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if(graph[i][j].equals("B")) {
                        blueScore += bfs(i, j, visited, "B");
                    } else {
                        whiteScore += bfs(i,j, visited, "W");
                    }
                }
            }
        }

        System.out.println(String.format("%d %d", whiteScore, blueScore));
    }

    static int bfs(int y, int x, boolean[][] visited, String warriorColor) {
        int warriorCount = 1;
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(x,y));
        visited[y][x] = true;

        while(!queue.isEmpty()) {
            Node now = queue.poll();

            for(int i = 0; i < 4; i++) {
                int nx = dirX[i] + now.x;
                int ny = dirY[i] + now.y;

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                if(visited[ny][nx]) {
                    continue;
                }
                if(!graph[ny][nx].equals(warriorColor)) {
                    continue;
                }
                queue.add(new Node(nx, ny));
                visited[ny][nx] = true;
                warriorCount++;
            }
        }
        return warriorCount * warriorCount;
    }

    static class Node {
        int x;
        int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}