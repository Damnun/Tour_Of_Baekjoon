import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) thorws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        
        while (T --> 0) {
            HashMap<String, Integer> hashMap = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            
            while (N --> 0) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                st.nextToken();
                
                String kind = st.nextToken();
                if (hashMap.containsKey(kind)) {
                    hashMap.put(kind, hashMap.get(kind) + 1);
                }
                
                else {
                    hashMap.put(kind, 1);
                }
            }
            
            int result = 1;
            for (int x : hashMap.values()) {
                result *= (x + 1);
            }
            sb.append(result - 1).append("\n");
        }
        System.out.println(sb);
    }
}
