import java.io.InputStreamReader;
import java.util.Scanner;

public class b2480 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int prize = 0;

        if (a == b && b == c) {
            prize = 10000 + a * 1000;
        }

        else {
            if ( a == b || a == c )
                prize = 1000 + a * 100;
            else if (b == c)
                prize = 1000 + b * 100;
            else
                prize = Integer.max(Integer.max(a, b), c) * 100;
        }

        System.out.println(prize);
    }
}