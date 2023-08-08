import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public static int solution(int[] queue1, int[] queue2) {
		int answer = 0;
		int queueSize = queue1.length;

		Queue<Integer> intQueue1 = new ArrayDeque<>();
		Queue<Integer> intQueue2 = new ArrayDeque<>();
		long queue1Sum = 0;
		long queue2Sum = 0;

		for (int i = 0; i < queueSize; i++) {
			intQueue1.add(queue1[i]);
			intQueue2.add(queue2[i]);

			queue1Sum += queue1[i];
			queue2Sum += queue2[i];
		}

		while (true) {
			if(answer > queueSize * 3) {
				answer = -1;
				break;
			}

			if (queue1Sum < queue2Sum) {
				int polledValue = intQueue2.poll();
				intQueue1.add(polledValue);

				queue2Sum -= polledValue;
				queue1Sum += polledValue;
			    
                answer++;
			} else if (queue1Sum > queue2Sum) {
				int polledValue = intQueue1.poll();
				intQueue2.add(polledValue);

				queue1Sum -= polledValue;
				queue2Sum += polledValue;
                
			    answer++;
			}

			if (queue1Sum == queue2Sum) {
				break;
			}
            
		}
		return answer;
	}
}