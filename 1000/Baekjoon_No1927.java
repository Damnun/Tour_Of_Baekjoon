import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class b1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> minQueue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            int data = Integer.parseInt(br.readLine());

            if (data > 0)
                minQueue.add(data);
            else {
                if (!minQueue.isEmpty())
                    System.out.println(minQueue.poll());
                else
                    System.out.println(0);
            }
        }
        br.close();
    }
}
