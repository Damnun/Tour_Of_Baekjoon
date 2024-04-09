import java.util.PriorityQueue;
import java.util.Scanner;

public class b1715 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int data = sc.nextInt();
            pq.add(data);
        }

        int d1 = 0, d2 = 0, sum = 0;
        while (pq.size() != 1) {
            d1 = pq.remove();
            d2 = pq.remove();
            sum += d1 + d2;
            pq.add(d1 + d2);
        }
        System.out.println(sum);
    }
}
