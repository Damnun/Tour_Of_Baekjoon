import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class b1414 {

    static int[] parent;
    static int n, sum;
    static PriorityQueue<Edge> queue;

    public static class Edge implements Comparable<Edge> {
        int s, e, v;

        Edge(int s, int e, int v) {
            this.s = s;
            this.e = e;
            this.v = v;
        }

        @Override
        public int compareTo(Edge o) {
            return this.v - o.v;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        queue = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char[] tmp = st.nextToken().toCharArray();

            for (int j = 0; j < n; j++) {
                int temp = 0;
                if (tmp[j] >= 'a' && tmp[j] <= 'z')
                    temp = tmp[j] - 'a' + 1;
                else if (tmp[j] >= 'A' && tmp[j] <= 'Z')
                    temp = tmp[j] = 'A' + 27;

                sum = sum + temp;
                if (i != j && temp != 0)
                    queue.add(new Edge(i, j, temp));
            }
        }

        parent = new int[n];
        for (int i = 0; i < parent.length; i++)
            parent[i] = i;

        int useEdge = 0;
        int result = 0;

        while(!queue.isEmpty()) {
            Edge now = queue.poll();
            if (find(now.s) != find(now.e)) {
                union(now.s, now.e);
                result = result + now.v;
                useEdge++;
            }
        }
        if (useEdge == n - 1)
            System.out.println(sum - result);
        else System.out.println(-1);
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b)
            parent[b] = a;
    }

    public static int find(int x) {
        if (x == parent[x]) return x;
        else return parent[x] = find(parent[x]);
    }
}
