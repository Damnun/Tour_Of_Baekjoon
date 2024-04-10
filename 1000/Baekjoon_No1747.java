import java.util.Scanner;

public class b1747 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[1_000_000_1];

        for (int i = 2; i < arr.length; i++) {
            arr[i] =i;
        }

        for (int i = 2; i < Math.sqrt(arr.length); i++) {
            if (arr[i] == 0)
                continue;
            for (int j = i + i; j < arr.length; j = j + i) {
                arr[j] = 0;
            }
        }

        int i = n;
        while (true) {
            if (arr[i] != 0) {
                int result = arr[i];
                if (isPalindrome(result)) {
                    System.out.println(result);
                    break;
                }
            }
            i++;
        }
    }

    private static boolean isPalindrome(int t) {
        char tmp[] = String.valueOf(t).toCharArray();
        int s = 0, e = tmp.length - 1;
        while (s < e) {
            if (tmp[s] != tmp[e]) {
                return false;
            }
            s++;
            e--;
        }
        return true;
    }
}
