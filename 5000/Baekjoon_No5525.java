import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b5525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        char[] data = br.readLine().toCharArray();

        int count = 0;
        int result = 0;

        for (int i = 1; i < m - 1; i++) {
            if (data[i - 1] == 'I' && data[i] == 'O' && data[i + 1] == 'I') {
                count++;

                if (count == n) {
                    count--;
                    result++;
                }
                i++;
            } else count = 0;
        }
        System.out.println(result);
    }
}
