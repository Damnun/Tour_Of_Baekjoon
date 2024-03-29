import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class b10816 {
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
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            int key = Integer.parseInt(st.nextToken());
            sb.append(upperBound(key) - lowerBound(key)).append(' ');
        }
        System.out.println(sb);
    }

    public static int lowerBound(int key) {
        int s = 0, e = a.length;

        while (s < e) {
            int m = (s + e) / 2;

            if (key <= a[m]) {
                e = m;
            }

            else {
                s = m + 1;
            }
        }
        return s;
    }


    public static int upperBound(int key) {
        int s = 0, e = a.length;

        while (s < e) {
            int m = (s + e) / 2;

            if (key < a[m]) {
                e = m;
            }

            else {
                s = m + 1;
            }
        }
        return s;
    }

}
