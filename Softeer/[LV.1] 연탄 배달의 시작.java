import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        
        int[] arr = new int[1000001];

        for(int i = 0; i < n - 1; i++) {
            arr[Math.abs(data[i] - data[i + 1])]++;
        }

        for (int i = 0; i < 1000001; i++) {
            if (arr[i] != 0) {
                System.out.println(arr[i]);
                break;
            }
        }
    }
}
