import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String first = st.nextToken();

            if (st.hasMoreTokens()) {
                int second = Integer.parseInt(st.nextToken());

                if (first.equals("push_front")) {
                    deque.addFirst(second);
                }

                else if (first.equals("push_back")) {
                    deque.addLast(second);
                }
            }

            else if (first.equals("pop_front")) {
                if (deque.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(deque.pollFirst());
                }
            }

            else if (first.equals("pop_back")) {
                if (deque.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(deque.pollLast());
                }
            }

            else if (first.equals("front")) {
                if (deque.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(deque.peekFirst());
                }
            }

            else if (first.equals("back")) {
                if (deque.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(deque.peekLast());
                }
            }
            
            else if (first.equals("size")) {
                System.out.println(deque.size());
            }

            else if (first.equals("empty")) {
                if (deque.isEmpty()) {
                    System.out.println("1");
                }
                else {
                    System.out.println("0");
                }
            }
        }
    }
}
