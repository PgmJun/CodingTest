import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<String, Double> creditGrade = Map.of(
                "A+", 4.5,
                "A0", 4.0,
                "B+", 3.5,
                "B0", 3.0,
                "C+", 2.5,
                "C0", 2.0,
                "D+", 1.5,
                "D0", 1.0,
                "F", 0.0
        );

        float totalCredit = 0;
        float totalGrade = 0; // 성적
        for(int i = 0; i < 20; i++) {
            String[] subject = br.readLine().split(" ");

            if(subject[2].equals("P")) {
                continue;
            }

            float subjectCredit = Float.valueOf(subject[1]);
            totalCredit += subjectCredit;
            totalGrade += creditGrade.get(subject[2]) * subjectCredit;
        }

        System.out.println(String.format("%.6f",totalGrade / totalCredit));
    }
}