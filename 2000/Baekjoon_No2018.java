import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b2018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int data = Integer.parseInt(br.readLine());
        int count = 1;
        int sum = 1;
        int start = 1;
        int end = 1;

        while (end != data) {
            if (sum == data) {
                count++;
                end++;
                sum += end;
            }
            else if (sum > data) {
                sum -= start;
                start++;
            }
            else {
                end++;
                sum += end;
            }
        }
        System.out.println(count);
    }
}
