import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        char[][] map = new char[101][101];
        int x = 0, y = 0;

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = s.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            int checkX = 0, checkY = 0;
            for (int j = 0; j < n; j++) {
                // check X
                if (map[i][j] == '.') checkX++;
                if (map[i][j] == 'X' || (j == n - 1)) {
                    if (checkX >= 2) x++;
                    checkX = 0;
                }

                // check Y
                if (map[j][i] == '.') checkY++;
                if (map[j][i] == 'X' || (j == n - 1)) {
                    if (checkY >= 2) y++;
                    checkY = 0;
                }
            }
        }
        System.out.println(x + " " + y);
    }
}
