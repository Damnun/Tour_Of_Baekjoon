import java.util.Scanner;

public class b2920 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String data = sc.nextLine();
        String ascending = "1 2 3 4 5 6 7 8";
        String descending = "8 7 6 5 4 3 2 1";

        if (data.equals(ascending))
            System.out.println("ascending");
        else if (data.equals(descending))
            System.out.println("descending");
        else System.out.println("mixed");
    }
}
