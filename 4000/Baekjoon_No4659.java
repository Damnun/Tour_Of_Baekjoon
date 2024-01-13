import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b4659 {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String password;
        char[] pass;
        String acc = "> is acceptable.\n";
        String not = "> is not acceptable.\n";
        StringBuilder sb = new StringBuilder();

        while (!(password = in.readLine()).equals("end")) {
            pass = password.toCharArray();
            char prev = '.';
            int count = 0;
            boolean flag = false;

            for (char p : pass) {
                if (isVowel(p)) flag = true;

                if (isVowel(p) != isVowel(prev)) count = 1;
                else count++;

                if (count > 2 || (prev == p && (p != 'e' && p != 'o'))) {
                    flag = false;
                    break;
                }

                prev = p;
            }

            sb.append('<').append(password);
            if (flag) sb.append(acc);
            else sb.append(not);
        }

        System.out.println(sb);
    }

    public static boolean isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
