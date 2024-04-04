import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class b14940 {

    static int[][] board;
    static int[][] score;
    static boolean[][] visited;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int n, m, targetX, targetY;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        score = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int cur = Integer.parseInt(st.nextToken());
                if (cur == 2) {
                    targetX = i;
                    targetY = j;
                }
                board[i][j] = cur;
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{targetX, targetY});

        while (!queue.isEmpty()) {
            int x = queue.peek()[0];
            int y = queue.peek()[1];
            queue.poll();

            visited[x][y] = true;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && n > nx && 0 <= ny && m > ny) {
                    if (!visited[nx][ny] && board[nx][ny] == 1) {
                        queue.add(new int[]{nx, ny});
                        score[nx][ny] = score[x][y] + 1;
                        visited[nx][ny] = true;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if (board[i][j] == 1 && score[i][j] == 0)
                    score[i][j] = -1;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(score[i][j] + " ");
            }
            System.out.println();
        }
    }
}
