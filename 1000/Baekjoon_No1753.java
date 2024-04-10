import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b1753 {

    static int V, E, K;
    static int distance[];
    static boolean visited[];
    static ArrayList<Edge> arr[];
    static PriorityQueue<Edge> queue = new PriorityQueue<Edge>();

    public static class Edge implements Comparable<Edge> {
        int vertex, value;

        Edge (int vertex, int value) {
            this.vertex = vertex;
            this.value = value;
        }

        public int compareTo(Edge o) {
            if (this.value > o.value) return 1;
            else return -1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        distance = new int[V + 1];
        visited = new boolean[V + 1];
        arr = new ArrayList[V + 1];

        for (int i = 0; i <= V; i++)
            arr[i] = new ArrayList<Edge>();
        for (int i = 0; i <= V; i++)
            distance[i] = Integer.MAX_VALUE;

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            arr[u].add(new Edge(v, w));
        }

        queue.add(new Edge(K, 0));
        distance[K] = 0;

        while (!queue.isEmpty()) {
            Edge cur = queue.poll();
            int c_v = cur.vertex;

            if (!visited[c_v]) {
                visited[c_v] = true;

                for (int i = 0; i < arr[c_v].size(); i++) {
                    Edge tmp = arr[c_v].get(i);
                    int next = tmp.vertex;
                    int value = tmp.value;
                    if (distance[next] > distance[c_v] + value) {
                        distance[next] = distance[c_v] + value;
                        queue.add(new Edge(next, distance[next]));
                    }
                }
            }
        }

        for (int i = 1; i <= V; i++) {
            if (visited[i])
                System.out.println(distance[i]);
            else System.out.println("INF");
        }
    }
}
