import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();

        for (char c = 'a'; c <= 'z'; c++) {
            sb.append(str.indexOf(c) + " ");
        }

        System.out.println(sb);
    }
}
