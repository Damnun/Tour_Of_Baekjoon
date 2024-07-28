import java.io.InputStreamReader;
import java.util.Scanner;

public class b2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int time = hour * 60 + minute + sc.nextInt();

        hour = time / 60 % 24;
        minute = time % 60;

        System.out.println(hour + " " + minute);
    }
}
