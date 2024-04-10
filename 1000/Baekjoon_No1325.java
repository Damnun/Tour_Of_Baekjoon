import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class b1352 {

    static int n, m;
    static boolean visited[];
    static int answer[];
    static ArrayList<Integer> arr[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new ArrayList[n + 1];
        answer = new int[n + 1];

        for (int i = 1; i <= n; i++)
            arr[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            arr[s].add(e);
        }

        for (int i = 1; i <= n; i++) {
            visited = new boolean[n + 1];
            bfs(i);
        }

        int max = 0;
        for (int i = 1; i <= n; i++) {
            max = Math.max(max, answer[i]);
        }

        for (int i = 1; i <= n; i++) {
            if (answer[i] == max)
                System.out.print(i + " ");
        }
    }

    public static void bfs(int i) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(i);
        visited[i] = true;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int x : arr[cur]) {
                if (visited[x] == false) {
                    visited[x] = true;
                    answer[x]++;
                    queue.add(x);
                }
            }
        }
    }
}
