import java.util.Scanner;

public class b2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");

        int hour = Integer.parseInt(s[0]);
        int minute = Integer.parseInt(s[1]);

        int calcTime = hour * 60 + minute - 45;
        if (calcTime < 0)
            calcTime = 24 * 60 + calcTime;

        System.out.println(calcTime / 60 + " " + calcTime % 60);
    }
}
