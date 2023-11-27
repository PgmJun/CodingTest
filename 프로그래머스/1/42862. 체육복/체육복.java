
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        // 학생의 체육복 갯수
        int[] std = new int[n+1];
        Arrays.fill(std, 1);
        std[0] = 0;
        
        for (int i : lost) {
            std[i] -= 1;
        }
        
        for (int i : reserve) {
            std[i] += 1;
        }
        
        for (int i = 1; i <= n; i++) {
            if (std[i] == 0) {
                // 1번 학생일 때 오른쪽만 탐색
                if (i == 1) {
                    if (std[i+1] == 2) {
                        std[i+1] -= 1;
                        std[i] += 1;
                        continue;
                    } else {
                        continue;
                    }
                }
                // n번 학생일 때 왼쪽만 탐색
                else if (i == n) {
                    if (std[i-1] == 2) {
                        std[i-1] -= 1;
                        std[i] += 1;
                        continue;
                    } else {
                        continue;
                    }
                }
                // 중간에 있는 학생일 때
                if (std[i-1] == 2) {
                    std[i-1] -= 1;
                    std[i] += 1;
                    continue;
                }
                if (std[i+1] == 2) {
                    std[i+1] -= 1;
                    std[i] += 1;
                    continue;
                }
            }
        }
        
        for (int s : std) {
            if (s != 0) {
                answer += 1;
            }
        }
        
        return answer;
    }
}