import java.util.Scanner;

public class b1463 {
    static Integer[] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        dp = new Integer[n + 1];
        dp[0] = dp[1] = 0;
        System.out.println(go(n));
    }

    static int go(int n) {
        if (dp[n] == null) {
            if (n % 6 == 0) {
                dp[n] = Math.min(go(n - 1), Math.min(go(n / 3), go(n / 2))) + 1;
            }

            else if (n % 3 == 0) {
                dp[n] = Math.min(go(n / 3), go(n - 1)) + 1;
            }

            else if (n % 2 == 0) {
                dp[n] = Math.min(go(n / 2), go(n - 1)) + 1;
            }

            else {
                dp[n] = go(n - 1) + 1;
            }
        }
        return dp[n];
    }
}
