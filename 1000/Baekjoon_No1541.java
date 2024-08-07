import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class b1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = Integer.MAX_VALUE;
        StringTokenizer subtraction = new StringTokenizer(br.readLine(), "-");

        while (subtraction.hasMoreTokens()) {
            StringTokenizer addition = new StringTokenizer(subtraction.nextToken(), "+");
            int temp = 0;
            
            while (addition.hasMoreTokens()) {
                temp += Integer.parseInt(addition.nextToken());
            }

            if (sum == Integer.MAX_VALUE) {
                sum = temp;
            }
            else {
                sum -= temp;
            }
        }
        System.out.println(sum);
    }
}
