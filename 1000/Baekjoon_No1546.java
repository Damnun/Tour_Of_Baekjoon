import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Double[] scoreArray = new Double[n];
        Double max = -1.0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            Double cur = Double.parseDouble(st.nextToken());
            scoreArray[i] = cur;
            max = Math.max(max, cur);
        }

        double scoreSum = 0;
        for (int i = 0; i < n; i++) {
            scoreSum += scoreArray[i] / max * 100;
        }

        System.out.println(scoreSum / n);
    }
}
