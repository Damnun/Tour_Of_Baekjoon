import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b1854 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N, M, K;
        int[][] W = new int[1001][1001];

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer>[] dist = new PriorityQueue[N + 1];
        Comparator<Integer> cp = (o1, o2) -> o1 < o2 ? 1 : -1;

        for (int i = 0; i < N + 1; i++) {
            dist[i] = new PriorityQueue<>(K, cp);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            W[a][b] = c;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1, 0));
        dist[1].add(0);
        
        while (!pq.isEmpty()) {
            Node u = pq.poll();
            for (int i = 1; i <= N; i++) {
                if (W[u.node][i] != 0) {
                    if (dist[i].size() < K) {
                        dist[i].add(u.cost + W[u.node][i]);
                        pq.add(new Node(i, u.cost + W[u.node][i]));
                    }
                    
                    else if (dist[i].peek() > u.cost + W[u.node][i]) {
                        dist[i].poll();
                        dist[i].add(u.cost + W[u.node][i]);
                        pq.add(new Node(i, u.cost + W[u.node][i]));
                    }
                }
            }
        }
        
        for (int i = 1; i <= N; i++) {
            if (dist[i].size() == K) {
                bw.write(dist[i].peek() + "\n");
            } else {
                bw.write(-1 + "\n");
            }
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}

class Node implements Comparable<Node> {
    int node;
    int cost;

    Node(int node, int cost) {
        this.node = node;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost < o.cost ? -1 : 1;
    }
}
