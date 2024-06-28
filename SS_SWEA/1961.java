package SWEA;

import java.io.*;

public class b1961 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());
            String[][] arr = new String[N][N];

            for (int i = 0; i < N; i++) {
                arr[i] = br.readLine().split(" ");
            }

            // 배치도
//            [2,0], [1,0], [0,0] || [2,2], [2,1], [2,0] || [0,2], [1,2], [2,2]
//            [2,1], [1,1], [0,1] || [1,2], [1,1], [1,0] || [0,1], [1,1], [2,1]
//            [2,2], [1,2], [0,2] || [0,2], [0,1], [0,0] || [0,0], [1,0], [2,0]

            StringBuilder[] data = new StringBuilder[N];
            for (int i = 0; i < N; i++) {
                data[i] = new StringBuilder();
            }

            // 90도
            for (int k = 0; k < N; k++) {
                for (int i = N - 1; i >= 0; i--) {
                    data[k].append(arr[i][k]);
                }
                data[k].append(" ");
            }

            // 180도
            for (int k = N - 1; k >= 0; k--) {
                for (int i = N - 1; i >= 0; i--) {
                    data[N - k - 1].append(arr[k][i]);
                }
                data[N - k - 1].append(" ");
            }

            // 270도
            for (int k = N - 1; k >= 0; k--) {
                for (int i = 0; i < N; i++) {
                    data[N - k - 1].append(arr[i][k]);
                }
                data[N - k - 1].append(" ");
            }

            // 출력
            System.out.println("#" + t);
            for (int i = 0; i < N; i++) {
                System.out.println(data[i]);
            }
        }
    }
}
