import java.util.Scanner;

public class b2908 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        StringBuffer sb = new StringBuffer(a);
        int x = Integer.parseInt(sb.reverse().toString());

        sb = new StringBuffer(b);
        int y = Integer.parseInt(sb.reverse().toString());

        if (x > y)
            System.out.println(x);
        else System.out.println(y);
    }
}
