import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Tomato {
    int row;
    int col;
    int height;

    public Tomato(int height, int row, int col) {
        this.row = row;
        this.col = col;
        this.height = height;
    }
}

public class b7576 {
    static int rowArr[] = {-1, 0, 1, 0, 0, 0};
    static int colArr[] = {0, 1, 0, -1, 0, 0};
    static int heightArr[] = {0, 0, 0, 0, 1, -1};
    static int M, N, H;
    static int tomato[][][];
    static int result;
    static Queue<Tomato> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        tomato = new int[H + 1][N + 1][M + 1];

        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= N; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 1; k <= M; k++) {
                    tomato[i][j][k] = Integer.parseInt(st.nextToken());
                    if (tomato[i][j][k] == 1)
                        queue.add(new Tomato(i, j, k));
                }
            }
        }

        bw.write(bfs() + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    public static int bfs() {
        while (!queue.isEmpty()) {
            Tomato point = queue.poll();

            int row = point.row;
            int col = point.col;
            int height = point.height;

            for (int i = 0; i < 6; i++) {
                int newHeight = height + heightArr[i];
                int newRow = row + rowArr[i];
                int newCol = col + colArr[i];
                if (checkPoint(newHeight, newRow, newCol)) {
                    queue.add(new Tomato(newHeight, newRow, newCol));
                    tomato[newHeight][newRow][newCol] = tomato[height][row][col] + 1;
                }
            }
        }

        int result = Integer.MIN_VALUE;

        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= N; j++) {
                for (int k = 1; k <= M; k++) {
                    if (tomato[i][j][k] == 0) {
                        return -1;
                    }
                    result = Math.max(result, tomato[i][j][k]);
                }
            }
        }
        if (result == 1) {
            return 0;
        } else {
            return result - 1;
        }
    }

    public static boolean checkPoint(int height, int row, int col) {
        if (height < 1 || height > H || row < 1 || row > N || col < 1 || col > M)
            return false;
        if (tomato[height][row][col] == 0)
            return true;
        else
            return false;
    }
}
