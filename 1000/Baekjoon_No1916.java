import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b1916 {

    static int n, m;
    static ArrayList<Node>[] list;
    static int[] dist;
    static boolean[] visit;

    public static class Node implements Comparable<Node> {
        int target;
        int value;

        Node (int target, int value) {
            this.target = target;
            this.value = value;
        }

        @Override
        public int compareTo (Node o) {
            return this.value - o.value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        list = new ArrayList[n + 1];
        dist = new int[n + 1];
        visit = new boolean[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        for (int i = 0; i <= n; i++)
            list[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            list[s].add(new Node(e, weight));
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        bw.write(dijkstra(s, e) + "\n");
        bw.flush();
        bw.close();
        br.close();

    }

    public static int dijkstra(int s, int e) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(s, 0));
        dist[s] = 0;
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (!visit[cur.target]) {
                visit[cur.target] = true;
                for (Node n : list[cur.target]) {
                    if (!visit[n.target] && dist[n.target] > dist[cur.target] + n.value) {
                        dist[n.target] = dist[cur.target] + n.value;
                        pq.add(new Node(n.target, dist[n.target]));
                    }
                }
            }
        }
        return dist[e];
    }
}
