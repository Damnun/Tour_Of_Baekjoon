package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b12712 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[][] board = new int[n][n];

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 십자 이동경로
            int[] dxOne = {0, 0, -1, 1};
            int[] dyOne = {-1, 1, 0, 0};

            // 대각선 이동경로
            int[] dxTwo = {-1, -1, 1, 1};
            int[] dyTwo = {-1, 1, -1, 1};

            int maxValue = 0;

            // 십자 이동
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int currentValue = board[i][j];
                    // 4방향
                    for (int k = 0; k < 4; k++) {
                        int curX = i;
                        int curY = j;
                        // m - 1개 이동
                        for (int l = 0; l < m - 1; l++) {
                            curX += dxOne[k];
                            curY += dyOne[k];
                            if (0 > curX || n <= curX || 0 > curY || n <= curY)
                                break;
                            currentValue += board[curX][curY];
                        }
                    }
                    if (currentValue > maxValue)
                        maxValue = currentValue;
                }
            }

            // 대각 이동
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int currentValue = board[i][j];
                    for (int k = 0; k < 4; k++) {
                        int curX = i;
                        int curY = j;
                        for (int l = 0; l < m - 1; l++) {
                            curX += dxTwo[k];
                            curY += dyTwo[k];
                            if (0 > curX || n <= curX || 0 > curY || n <= curY)
                                break;
                            currentValue += board[curX][curY];
                        }
                    }
                    if (currentValue > maxValue)
                        maxValue = currentValue;
                }
            }

            System.out.println("#" + t + " " + maxValue);
        }
    }
}
