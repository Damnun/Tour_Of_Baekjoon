import java.util.*;

public class b18352 {

    static int visited[];
    static ArrayList<Integer>[] arr;
    static List<Integer> answer;
    static int n, m, k, x;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        k = scan.nextInt();
        x = scan.nextInt();

        arr = new ArrayList[n + 1];
        answer = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            arr[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++) {
            int s = scan.nextInt();
            int e = scan.nextInt();
            arr[s].add(e);
        }

        visited = new int[n + 1];
        Arrays.fill(visited, -1);

        bfs(x);
        for(int i = 0; i <= n; i++) {
            if (visited[i] == k)
                answer.add(i);
        }

        if (answer.isEmpty())
            System.out.println("-1");

        else {
            Collections.sort(answer);
            for (int tmp : answer) {
                System.out.println(tmp);
            }
        }
    }

    private static void bfs(int node) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(node);
        visited[node]++;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int i : arr[cur]) {
                if (visited[i] == -1) {
                    visited[i] = visited[cur] + 1;
                    queue.add(i);
                }
            }
        }
    }
}
