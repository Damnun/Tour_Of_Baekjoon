import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b10872 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        Integer result = n;

        if (n == 0) {
            result = 1;
        }

        else {
            for (int i = (n - 1); i > 0; i--) {
                result = result * i;
            }
        }

        System.out.println(result);
    }
}
