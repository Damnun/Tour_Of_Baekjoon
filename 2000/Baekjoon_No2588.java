import java.io.InputStreamReader;
import java.util.Scanner;

public class b2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        String a = sc.nextLine();
        String b = sc.nextLine();
        int result = 0;

        if (b.length() > a.length()) {
            String tmp = b;
            b = a;
            a = tmp;
        }

        for (int i = b.length() - 1; i >= 0; i--) {
            int cur = 0;
            for (int j = a.length() - 1; j >= 0; j--)
                cur += Character.getNumericValue(a.charAt(j)) * Character.getNumericValue(b.charAt(i)) * Math.pow(10, a.length() - j - 1);
            System.out.println(cur);
            result += cur * Math.pow(10, b.length() - i - 1);
        }
        System.out.println(result);
    }
}
