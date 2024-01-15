import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b15904 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        char[] charList = {'U', 'C', 'P', 'C'};
        int charIndex = 0;
        int tokenCount = st.countTokens();

        for (int i = 0; i < tokenCount; i++) {
            String cur = st.nextToken();

            for (int j = 0; j < cur.length(); j++) {
                if (cur.charAt(j) == charList[charIndex]) {
                    charIndex++;
                }

                if (charIndex == 4) {
                    System.out.println("I love UCPC");
                    System.exit(0);
                }
            }
        }

        System.out.println("I hate UCPC");
    }
}
