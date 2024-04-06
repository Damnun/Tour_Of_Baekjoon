import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class b16928 {
    static int[] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        board = new int[101];
        for (int i = 1; i < board.length; i++) {
            board[i] = i;
        }

        int k = n + m;
        while (k-- > 0) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            board[x] = y;
        }

        System.out.println(bfs(1));
    }

    private static int bfs(int startNode) {
        int[] check = new int[101];
        Queue<Integer> q = new LinkedList<>();
        q.offer(startNode);
        check[startNode] = 0;

        while (true) {
            int visitedNum = q.poll();
            for (int i = 1; i < 7; i++) {
                int newNode = visitedNum + i;

                if (newNode > 100) {
                    continue;
                }
                if (check[board[newNode]] == 0) {
                    q.offer(board[newNode]);
                    check[board[newNode]] = check[visitedNum] + 1;
                }
                if (board[newNode] == 100) {
                    return check[100];
                }
            }
        }
    }
}