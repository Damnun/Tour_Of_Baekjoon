import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

import java.util.StringTokenizer;

public class b10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<Integer> queue = new LinkedList<>();
        int last = 0;
        
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String first = st.nextToken();
            
            if (st.hasMoreTokens()) {
                int second = Integer.parseInt(st.nextToken());
                last = second;
                queue.offer(second);
            }

            else if (first.equals("pop")) {
                if (queue.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(queue.poll());
                }
            }

            else if (first.equals("front")) {
                if (queue.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(queue.peek());
                }
            }

            else if (first.equals("back")) {
                if (queue.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(last);
                }
            }



            else if (first.equals("size")) {
                System.out.println(queue.size());
            }

            else if (first.equals("empty")) {
                if (queue.isEmpty()) {
                    System.out.println("1");
                }
                else {
                    System.out.println("0");
                }
            }
        }
    }
}
