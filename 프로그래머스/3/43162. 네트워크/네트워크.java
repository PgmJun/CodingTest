import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];

        List<Set<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new HashSet<>());
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }
                if (computers[i][j] == 1) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            answer++;
            queue.add(i);
            while (!queue.isEmpty()) {
                int now = queue.poll();
                visited[now] = true;
                for (int node : graph.get(now)) {
                    if (visited[node]) {
                        continue;
                    }
                    visited[node] = true;
                    queue.add(node);
                }
            }
        }

        return answer;
    }
}