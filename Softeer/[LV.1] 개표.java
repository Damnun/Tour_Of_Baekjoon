import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T --> 0) {
            int n = Integer.parseInt(br.readLine());
            int x = n / 5;
            int y = n % 5;

            while (x --> 0) {
                System.out.print("++++ ");
            }

            while (y --> 0) {
                System.out.print("|");
            }
            System.out.println();
        }
    }
}
