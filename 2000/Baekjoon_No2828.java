import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

import static java.lang.Math.abs;

public class b2828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());

        int start = 1, end = m;
        int result = 0;

        for(int i = 0; i < k; i++) {
            int targetIndex = Integer.parseInt(br.readLine());

            if (start > targetIndex) {
                result += start - targetIndex;
                end -= start - targetIndex;
                start = targetIndex;
            }
            else if (end < targetIndex) {
                result += targetIndex - end;
                start += targetIndex - end;
                end = targetIndex;
            }
        }
        System.out.println(result);
    }
}
