import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringJoiner;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
		List<Integer> numbers = Arrays.stream(s.split(" "))
			.map(Integer::parseInt)
			.collect(Collectors.toList());

		Collections.sort(numbers);

		StringJoiner joiner = new StringJoiner(" ");
		joiner.add(numbers.get(0).toString());
		joiner.add(numbers.get(numbers.size()-1).toString());
		return joiner.toString();
	}
}