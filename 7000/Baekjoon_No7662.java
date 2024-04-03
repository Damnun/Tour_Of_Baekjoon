import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int k = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> queue = new TreeMap<>();

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                char ch = st.nextToken().charAt(0);
                int n = Integer.parseInt(st.nextToken());

                if (ch == 'I') {
                    queue.put(n, queue.getOrDefault(n, 0) + 1);
                } else {
                    if (queue.size() == 0)
                        continue;

                    int num = n == 1 ? queue.lastKey() : queue.firstKey();
                    if (queue.put(num, queue.get(num) - 1) == 1)
                        queue.remove(num);
                }
            }
            System.out.println(queue.size() == 0 ? "EMPTY" : queue.lastKey() + " " + queue.firstKey());
        }
    }
}
