import java.util.Scanner;
public class b2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] arr = new int[10] ;

        String str = String.valueOf(a * b * c);

        for(int i = 0; i < str.length(); i++) {
            arr[Integer.parseInt(String.valueOf(str.charAt(i)))]++;
        }

        for (int x : arr)
            System.out.println(x);
    }
}
