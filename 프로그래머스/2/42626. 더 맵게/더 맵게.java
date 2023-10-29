import java.util.*;

class Solution {
    public static int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Node> queue = new PriorityQueue<>();
        for (int s : scoville) {
            queue.add(new Node(s));
        }
        while(true) {
            if(queue.peek().value >= K || queue.size() == 1) {
                break;
            }
            answer++;
            Node first = queue.poll();
            Node second = queue.poll();

            queue.add(new Node(first.value + second.value * 2));
        }
        
        if(queue.size() == 1) {
            if(queue.peek().value < K) {
                answer = -1;
            }
        }

        return answer;
    }

    static class Node implements Comparable<Node> {

        int value;

        public Node(int value) {
            this.value = value;
        }

        @Override
        public int compareTo(Node o) {
            return this.value - o.value;
        }
    }
}