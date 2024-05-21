import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        boolean isTouched = false;
        int distance = 0;
        int time = 0;

        while (true) {
            if (isTouched && distance == d) {
                System.out.println(time);
                break;
            }

            if (!isTouched) {
                // A초 뒤를 보고 있음
                if (a + distance >= d) {
                    time += d - distance;
                    distance = 0;
                    isTouched = true;
                    continue;
                }

                else {
                    time += a;
                    distance += a;
                }

                // B초 앞을 보고 있음
                time += b;
            }

            if (isTouched) {
                // B초 앞을 보고 있음
                if (b + distance >= d) {
                    time += d - distance;
                    distance = d;
                    continue;
                }

                else {
                    time += b;
                    distance += b;
                }

                // A초 뒤를 보고 있음
                time += a;
            }
        }

        // 터치 전 a초 뒤, b초 앞
        // 터치 후 b초 뒤, a초 앞
        // 1초당 1만큼 이동 가능
    }
}
