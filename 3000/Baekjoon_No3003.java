import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b3003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = {1, 1, 2, 2, 2, 8};
        String answer = "";

        for (int i = 0; i < arr.length; i++) {
            answer += String.valueOf(arr[i] - Integer.parseInt(st.nextToken()));
            answer += " ";
        }

        System.out.println(answer);

    }
}
