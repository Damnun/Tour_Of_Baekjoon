import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class b1167 {

    static ArrayList<int[]>[] list;
    static boolean[] visited;
    static int max = 0;
    static int node;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        list = new ArrayList[n + 1];

        for (int i = 1; i < n + 1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            while (true) {
                int e = sc.nextInt();
                if (e == -1) break;
                int cost = sc.nextInt();
                list[s].add(new int[] {e, cost});
            }
        }

        visited = new boolean[n + 1];
        dfs(1, 0);

        visited = new boolean[n + 1];
        dfs(node, 0);

        System.out.println(max);
    }

    public static void dfs(int x, int len) {
        if (len > max) {
            max = len;
            node = x;
        }

        visited[x] = true;

        for (int i = 0; i < list[x].size(); i++) {
            int e = list[x].get(i)[0];
            int cost = list[x].get(i)[1];

            if (visited[e] == false) {
                dfs(e, cost + len);
                visited[e] = true;
            }
        }
    }
}
