import java.util.Scanner;

public class b10986 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        long[] s = new long[n];
        long[] c = new long[m];
        long answer = 0;

        s[0] = sc.nextInt();
        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            int remain = (int) (s[i] % m);
            if (remain == 0) answer++;
            c[remain]++;
        }

        for (int i = 0; i < m; i++) {
            if (c[i] > 1) {
                answer = answer + (c[i] * (c[i] - 1) / 2);
            }
        }
        System.out.println(answer);
    }
}
