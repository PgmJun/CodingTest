import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> numberArr = Arrays.stream(numbers)
                .mapToObj(String::valueOf)
                .sorted((o1, o2) -> (o2 + o1).compareTo(o1 + o2))
                .collect(Collectors.toList());

        if (numberArr.get(0).equals("0")) {
            return "0";
        }

        StringBuilder answer = new StringBuilder();
        for (String number : numberArr) {
            answer.append(number);
        }

        return answer.toString();
    }
}