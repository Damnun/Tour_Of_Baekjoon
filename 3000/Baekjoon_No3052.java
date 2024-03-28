import java.util.Scanner;

public class b3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] result = new int[43];
        int count = 0;

        for (int i = 0; i < 10; i++) {
            result[sc.nextInt() % 42]++;
        }

        for (int r : result) {
            if (r != 0)
                count++;
        }

        System.out.println(count);
    }
}
