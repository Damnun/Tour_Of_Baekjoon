import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b1219 {

    static int n, m, startCity, endCity;
    static long distance[], cityMoney[];
    static Edge edges[];

    public static class Edge {
        int start;
        int end;
        int time;

        public Edge(int start, int end, int time) {
            this.start = start;
            this.end = end;
            this.time = time;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        startCity = Integer.parseInt(st.nextToken());
        endCity = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        distance = new long[n];
        cityMoney = new long[n];
        edges = new Edge[m];
        Arrays.fill(distance, Long.MIN_VALUE);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());
            edges[i] = new Edge(start, end, time);
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            cityMoney[i] = Long.parseLong(st.nextToken());

        distance[startCity] = cityMoney[startCity];
        for (int i = 0; i <= n + 100; i++) {
            for (int j = 0; j < m; j++) {
                int start = edges[j].start;
                int end = edges[j].end;
                int time = edges[j].time;

                if (distance[start] == Long.MAX_VALUE)
                    distance[end] = Long.MAX_VALUE;
                else if (distance[end] < distance[start] + cityMoney[end] - time) {
                    distance[end] = distance[start] + cityMoney[end] - time;
                    if (i >= n - 1)
                        distance[end] = Long.MAX_VALUE;
                }
            }
        }

        if (distance[endCity] == Long.MIN_VALUE)
            System.out.println("gg");
        else if (distance[endCity] == Long.MAX_VALUE)
            System.out.println("Gee");
        else System.out.println(distance[endCity]);
    }
}
