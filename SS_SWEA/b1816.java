package SWEA;

import java.util.*;
import java.io.*;

public class b1816 {

	public static char[][] board;
	public static boolean[][] visited;
	public static int result, N;
	public static int[] dx = { -1, -1, -1, 0, 0, 1, 1, 1 };
	public static int[] dy = { -1, 0, 1, -1, 1, -1, 0, 1 };

	public static int checkBomb(int x, int y) {
		int count = 0;
		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N)
				if (board[nx][ny] == '*')
					count++;
		}
		return count;
	}

	public static void bfs(int x, int y) {
		Queue<char[]> queue = new LinkedList<>();
		visited[x][y] = true;
		queue.add(new char[] { (char) (x + '0'), (char) (y + '0') });

		while (!queue.isEmpty()) {
			char[] current = queue.poll();
			int curX = current[0] - '0';
			int curY = current[1] - '0';
			int count = checkBomb(curX, curY);
			board[curX][curY] = (char) (count + '0');
			
			if (count > 0)
				continue;

			for (int i = 0; i < 8; i++) {
				int nx = curX + dx[i];
				int ny = curY + dy[i];
				if (nx >= 0 && nx < N && ny >= 0 && ny < N)
					if (!visited[nx][ny] && board[nx][ny] != '*') {
						visited[nx][ny] = true;
						queue.add(new char[] { (char) (nx + '0'), (char) (ny + '0') });
					}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			result = 0;
			board = new char[N][N];
			visited = new boolean[N][N];
			
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String str = st.nextToken();
				for (int j = 0; j < N; j++)
					board[i][j] = str.charAt(j);
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (checkBomb(i, j) == 0 && board[i][j] != '*' && !visited[i][j]) {
						result++;
						bfs(i, j);
					}
				}
			}
			
			for(int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (board[i][j] == '.') {
						board[i][j] = (char) (checkBomb(i, j) + '0');
						visited[i][j] = true;
						result++;
					}
				}
			}
			
			System.out.println("#" + t + " " + result);
		}

	}

}
