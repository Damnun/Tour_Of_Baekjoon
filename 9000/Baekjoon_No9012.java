import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class b9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            Queue<String> open = new LinkedList<>();
//            Queue<String> close = new LinkedList<>();
            String result = "YES";
            String data = br.readLine();

            for (int j = 0; j < data.length(); j++) {
                if (data.charAt(j) == '(') {
                    open.offer("(");
                }
                else if (data.charAt(j) == ')') {
                    if (!open.isEmpty() && open.peek().equals("(")) {
                        open.poll();
                    }
                    else {
                        result = "NO";
                        break;
                    }
                }
            }
            if (!open.isEmpty())
                result = "NO";
            System.out.println(result);
        }
    }
}
