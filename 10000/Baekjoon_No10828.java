import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class b10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String first = st.nextToken();

            if (st.hasMoreTokens()) {
                int second = Integer.parseInt(st.nextToken());
                stack.push(second);
            }

            else if (first.equals("pop")) {
                if (stack.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(stack.pop());
                }
            }

            else if (first.equals("top")) {
                if (stack.isEmpty()) {
                    System.out.println("-1");
                }
                else {
                    System.out.println(stack.peek());
                }
            }

            else if (first.equals("size")) {
                System.out.println(stack.size());
            }

            else if (first.equals("empty")) {
                if (stack.isEmpty()) {
                    System.out.println("1");
                }
                else {
                    System.out.println("0");
                }
            }
        }
    }
}
