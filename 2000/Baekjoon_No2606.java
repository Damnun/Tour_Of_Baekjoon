import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b2606 {

    static boolean[] visited;
    static int[][] board;
    static int count = 0;
    static int n, l;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        l = Integer.parseInt(br.readLine());

        board = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < l; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(str.nextToken());
            int b = Integer.parseInt(str.nextToken());

            board[a][b] = board[b][a] = 1;
        }

        dfs(1);
        System.out.println(count - 1);
    }

    public static void dfs(int start) {
        visited[start] = true;
        count++;

        for (int i = 0; i <= n; i++) {
            if (board[start][i] == 1 && !visited[i])
                dfs(i);
        }
    }
}
