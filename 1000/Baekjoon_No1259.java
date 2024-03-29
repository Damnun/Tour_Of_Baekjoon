import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String cur = br.readLine();
            if (cur.equals("0")) break;

            String left = cur.substring(0, cur.length() / 2);
            String right;

            if (cur.length() % 2 == 0)
                right = cur.substring(cur.length() / 2);
            else
                right = cur.substring(cur.length() / 2 + 1);
            
            StringBuffer sb = new StringBuffer(right);

            if (left.equals(sb.reverse().toString()))
                System.out.println("yes");
            else System.out.println("no");

        }
    }
}
