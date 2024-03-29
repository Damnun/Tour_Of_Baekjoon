import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1920 {

    public static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(a);

        int m = Integer.parseInt(br.readLine());
        int[] b = new int[m];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        for (int x : b) {
            System.out.println(binarySearch(x));
        }
    }

    public static int binarySearch(int x) {
        int s = 0, e = a.length - 1;

        while (s <= e) {
            int m = (s + e) / 2;

            if (a[m] == x) {
                return 1;
            }

            else if (a[m] > x) {
                e = m - 1;
            }

            else if (a[m] < x) {
                s = m + 1;
            }
        }
        return 0;
    }
}
