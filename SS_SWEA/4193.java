package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class b4193 {

	public static int N, startX, startY, desX, desY;
	public static int[][] board;
	public static boolean[][] visited;
	public static int[] dx = { 0, 0, -1, 1 };
	public static int[] dy = { -1, 1, 0, 0 };
	
	static class Node {
		int x, y, time;
		
		public Node(int x, int y, int time) {
			this.x = x;
			this.y = y;
			this.time = time;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());
			board = new int[N][N];
			visited = new boolean[N][N];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			st = new StringTokenizer(br.readLine());
			startX = Integer.parseInt(st.nextToken());
			startY = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			desX = Integer.parseInt(st.nextToken());
			desY = Integer.parseInt(st.nextToken());

			int result = bfs(new Node(startX, startY, 0));
			System.out.println("#" + t + " " + result);
		}

	}

	private static int bfs(Node startNode) {
		Queue<Node> queue = new LinkedList<>();
		queue.add(startNode);
		visited[startNode.x][startNode.y] = true;

		while (!queue.isEmpty()) {
			Node current = queue.poll();
			
			if (current.x == desX && current.y == desY)
				return current.time;

			for (int i = 0; i < 4; i++) {
				int nx = current.x + dx[i];
				int ny = current.y + dy[i];
				if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
					if (board[nx][ny] != 1 && !visited[nx][ny]) {
						if (board[nx][ny] == 2) {
							if (current.time % 3 == 2) {
							visited[nx][ny] = true;
							queue.add(new Node(nx, ny, current.time + 1));
							}
							else {
							visited[current.x][current.y] = true;
							queue.add(new Node(current.x, current.y, current.time + 1));
							}
						}
						else {
							visited[nx][ny] = true;
							queue.add(new Node(nx, ny, current.time + 1));
						}
					}
				}
			}
		}
		return -1;
	}
}
