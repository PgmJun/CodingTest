import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String replaced = Integer.toBinaryString(n + 1).replace("0", "4").replace("1", "7");
        System.out.println(replaced.substring(1));

        // 4,7의 패턴이 이진수의 형태와 유사한 점을 통해 변환 시도
        // 입력 -> 입력값에+1 -> 이진수변환 -> 0은 4,1은 7로 변환 -> index 1부터 자르면 변환 완료
        // 1 -> 01 -> 10 -> 74 -> 4
        // 2 -> 10 -> 11 -> 77 -> 7
        // 3 -> 11 -> 100 -> 744 -> 44
        // 4 -> 100 -> 101 -> 747 -> 47
        // 5 -> 101 -> 110 -> 774 -> 74
    }
}