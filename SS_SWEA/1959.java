package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1959 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int max = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[] a = new int[n];
            int[] b = new int[m];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                b[i] = Integer.parseInt(st.nextToken());
            }

            if (n > m) {
                int tmp = n;
                n = m;
                m = tmp;

                int[] tmpArr = a;
                a = b;
                b = tmpArr;
            }

            for (int i = 0; i <= m - n; i++) {
                int cur = 0;
                for (int j = 0; j < n; j++) {
                    cur += a[j] * b[i + j];
                }

                if (max < cur)
                    max = cur;
            }
            System.out.println("#" + t + " " + max);
        }
    }
}
