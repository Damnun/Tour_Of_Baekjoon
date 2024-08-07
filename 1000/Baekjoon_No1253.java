import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1253 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        long arr[] = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(arr);

        for (int k = 0; k < n; k++) {
            long key = arr[k];
            int i = 0, j = n - 1;

            while (i < j) {
                if (arr[i] + arr[j] == key) {
                    if (i != k && j != k) {
                        result++;
                        break;
                    }

                    else if (i == k)
                        i++;

                    else if (j == k)
                        j--;
                }

                else if (arr[i] + arr[j] < key) {
                    i++;
                }

                else j--;
            }
        }
        System.out.println(result);
        br.close();
    }
}
