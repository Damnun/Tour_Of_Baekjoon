import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class b11279 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> pq = new PriorityQueue();
        int N = Integer.parseInt(br.readLine());

        while (N-- > 0) {
            int k = Integer.parseInt(br.readLine());
            if (k == 0) {
                if (pq.isEmpty()) System.out.println(0);
                else System.out.println(-pq.poll());
            } else {
                pq.add(-k);
            }
        }
    }
}
