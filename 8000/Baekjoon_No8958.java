import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            int finalScore = 0;
            int score = 1;

            for (int j = 0; j < str.length(); j++)
            {
                if (str.charAt(j) == 'O')
                    finalScore += score++;
                else score = 1;
            }
            System.out.println(finalScore);
        }
    }
}
