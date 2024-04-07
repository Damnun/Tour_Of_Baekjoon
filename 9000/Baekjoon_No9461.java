import java.util.Scanner;

public class b9461 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-- > 0) {
            int N = sc.nextInt();

            if (N < 3) {
                System.out.println(1);
                continue;
            }
            
            long[] array = new long[N + 1];
            array[0] = 1;
            array[1] = 1;
            array[2] = 1;

            for (int i = 3; i <= N; i++) {
                array[i] = array[i - 2] + array[i - 3];
            }

            System.out.println(array[N - 1]);
        }
    }
}
