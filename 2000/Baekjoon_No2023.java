import java.util.Scanner;

public class b2023 {

    static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        dfs(2, 1);
        dfs(3, 1);
        dfs(5, 1);
        dfs(7, 1);
    }

    static void dfs(int n, int k) {
        if (k == N) {
            if (isPrime(n)) {
                System.out.println(n);
            }
        }

        for (int i = 1; i < 10; i++) {
            if (i % 2 == 0) {
                continue;
            }

            if (isPrime(n * 10 + i)) {
                dfs(n * 10 + i, k + 1);
            }
        }
    }

    static boolean isPrime(int n) {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }


}
