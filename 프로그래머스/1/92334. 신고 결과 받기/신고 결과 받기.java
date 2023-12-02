import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Set<String> reports = Arrays.stream(report).collect(Collectors.toSet());
        Map<String, Integer> reportCount = new HashMap<>();
        Map<String, List<String>> reportTo = new HashMap<>();
        for (String id : id_list) {
            reportCount.put(id, 0);
            reportTo.put(id, new ArrayList<>());
        }

        for (String reportContent : reports) {
            String[] splited = reportContent.split(" ");
            reportTo.get(splited[0]).add(splited[1]);
            reportCount.put(splited[1], reportCount.get(splited[1]) + 1);
        }

        List<String> bans = new ArrayList();
        for (String key : reportCount.keySet()) {
            if (reportCount.get(key) >= k) {
                bans.add(key);
            }
        }

        for (int id = 0; id < id_list.length; id++) {
            List<String> idsReportList = reportTo.get(id_list[id]);
            for (String ban : bans) {
                if(idsReportList.contains(ban)) answer[id]++;
            }
        }
        return answer;
    }
}