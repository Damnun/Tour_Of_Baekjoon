import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class b1744 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> mq = new PriorityQueue<>();
        int o = 0, z = 0;

        for (int i = 0; i < n; i++) {
            int data = sc.nextInt();

            if (data > 1)
                pq.add(data);

            else if (data == 1)
                o++;

            else if (data == 0)
                z++;

            else
                mq.add(data);
        }

        int sum = 0;
        while (pq.size() > 1) {
            int f = pq.remove(), s = pq.remove();
            sum = sum + f * s;
        }

        if (!pq.isEmpty())
            sum = sum + pq.remove();

        while (mq.size() > 1) {
            int f = mq.remove(), s = mq.remove();
            sum = sum + f * s;
        }

        if (!mq.isEmpty()) {
            if (z == 0)
                sum = sum + mq.remove();
        }

        sum = sum + o;
        System.out.println(sum);
    }
}
