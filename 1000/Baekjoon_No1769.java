import java.util.Scanner;

public class b1769 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String x = sc.next();
        Integer count = 0;

        while (true) {
            long sum = 0;
            if (x.length() == 1) {
                break;
            }

            for (int i = 0; i < x.length(); i++) {
                sum += Integer.parseInt(String.valueOf(x.charAt(i)));
            }

            count++;
            x = String.valueOf(sum);
        }

        if (Integer.parseInt(x) % 3 == 0) {
            System.out.println(count);
            System.out.println("YES");
        }
        else {
            System.out.println(count);
            System.out.println("NO");
        }
    }
}
