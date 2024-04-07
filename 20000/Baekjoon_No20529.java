import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class b20529 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int min = 12;
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());

            int num = N > 32 ? 33 : N;
            String[] mbti = new String[num];

            N = mbti.length;

            for (int i = 0; i < N; i++) {
                mbti[i] = st.nextToken();
            }

            outerLoop:
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    for (int k = j + 1; k < N; k++) {
                        int count = 0;
                        for (int l = 0; l < 4; l++) {
                            count += mbti[i].charAt(l) != mbti[j].charAt(l) ? 1 : 0;
                            count += mbti[i].charAt(l) != mbti[k].charAt(l) ? 1 : 0;
                            count += mbti[j].charAt(l) != mbti[k].charAt(l) ? 1 : 0;
                        }
                        min = Math.min(count, min);
                        if (min == 0) break outerLoop;
                    }
                }
            }
            System.out.println(min);
        }
    }
}
