import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] str = new String[n];

        for (int i = 0; i < n; i++) {
            str[i] = br.readLine();
        }


        Arrays.sort(str, (e1, e2) -> {
            if (e1.length() == e2.length())
                return e1.compareTo(e2);
            else
                return e1.length() - e2.length();
        });

        String before = "";
        for (String s : str) {
            if (!s.equals(before)) {
                System.out.println(s);
                before = s;
            }
        }

    }
}
