import java.util.Scanner;

public class b25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int result = sc.nextInt();
        int n = sc.nextInt();

        int tmp = 0 ;
        for (int i = 0; i < n; i++) {
            tmp += sc.nextInt() * sc.nextInt();
        }

        if (tmp == result)
            System.out.println("Yes");
        else System.out.println("No");
    }
}
