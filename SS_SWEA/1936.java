package SWEA;

import java.util.Scanner;

public class b1936 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        char result = 'A';

        switch (A) {
            case 1:
                if (B == 2)
                    result = 'B';
                break;
            case 2:
                if (B == 3)
                    result = 'B';
                break;
            case 3:
                if (B == 1)
                    result = 'B';
                break;
        }

        System.out.println(result);
    }
}
