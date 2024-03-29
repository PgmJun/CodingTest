import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int solution(int[] topping) {
		int answer = 0;
		
		Set<Integer> sep1 = new HashSet<>();
		Map<Integer, Integer> sep2 = new HashMap<>();

		sep1.add(topping[0]);
		for(int i = 1; i < topping.length;i++) {
			sep2.put(topping[i], sep2.getOrDefault(topping[i], 0) + 1);
		}

		for (int i = 1; i < topping.length; i++) {
			sep1.add(topping[i]);
			sep2.put(topping[i], sep2.get(topping[i]) - 1);
			
			if(sep2.get(topping[i]) == 0) {
				sep2.remove(topping[i]);
			}

			if (sep1.size() == sep2.size()) {
				answer++;
			}
		}
		
		return answer;
	}
}