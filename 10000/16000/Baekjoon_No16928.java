import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class b16928 {

    static int N, M, result;
    static int s = 1, end = 100;
    static boolean[] visited;
    static Map<Integer, Integer> snakeAndLadder;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[101];
        snakeAndLadder = new HashMap<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            snakeAndLadder.put(x, y);
        }

        bfs();
        System.out.println(result);
    }

    static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;

        while(!queue.isEmpty()) {
            result++;
            for (int i = 0, queueSize = queue.size(); i < queueSize; i++) {
                int cur = queue.poll();

                for (int j = 1; j <= 6; j++) {
                    int move = cur + j;
                    if (move == end)
                        return;

                    if (move > end)
                        continue;

                    if (visited[move])
                        continue;

                    visited[move] = true;
                    if (snakeAndLadder.containsKey(move)) {
                        move = snakeAndLadder.get(move);
                    }
                    queue.add(move);
                }
            }
        }
    }
}
