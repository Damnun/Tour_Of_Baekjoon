import java.util.Scanner;

public class b1976 {
    public static int[] parent;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] dosi = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dosi[i][j] = sc.nextInt();
            }
        }

        int[] route = new int[m + 1];
        for (int i = 1; i <= m; i++) {
            route[i] = sc.nextInt();
        }

        parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (dosi[i][j] == 1) union(i, j);
            }
        }

        int index = find(route[1]);
        for (int i = 2; i < route.length; i++) {
            if (index != find(route[i])) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    public static void union(int i, int j) {
        i = find(i);
        j = find(j);
        if (i != j)
            parent[j] = i;
    }

    public static int find(int i) {
        if (i == parent[i]) return i;
        return parent[i] = find(parent[i]);
    }
}
