import java.util.Scanner;

public class b1436 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;

        int cur = 666;
        while (true) {
            if (String.valueOf(cur).contains("666")) {
                count++;
            }

            if (n == count) {
                System.out.println(cur);
                break;
            }
            cur++;
        }
    }
}
