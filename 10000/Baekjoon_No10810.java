import java.util.Scanner;

public class b10810 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = 0;

        for (int i = 0; i < m; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            int target = sc.nextInt();

            for (int j = s - 1; j <= e - 1; j++) {
                arr[j] = target;
            }
        }

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
