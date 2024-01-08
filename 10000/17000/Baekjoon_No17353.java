import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long x = Integer.parseInt(st.nextToken());
        long y = Integer.parseInt(st.nextToken());

        System.out.println(lcm(x, y));
    }

    public static long gcd(long x, long y) {
        while (y > 0) {
            long tmp = x;
            x = y;
            y = tmp % x;
        }

        return x;
    }

    public static long lcm(long x, long y) {
        return (x * y) / gcd(x, y);
    }
}
