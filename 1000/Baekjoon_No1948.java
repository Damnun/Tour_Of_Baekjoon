import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class b1948 {

    static class Node {
        int target;
        int value;

        Node (int target, int value) {
            this.target = target;
            this.value = value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        ArrayList<ArrayList<Node>> arr = new ArrayList<>();
        ArrayList<ArrayList<Node>> reverseArr = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            arr.add(new ArrayList<>());
            reverseArr.add(new ArrayList<>());
        }

        int[] indegree = new int[n + 1];
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            arr.get(s).add(new Node(e, v));
            reverseArr.get(e).add(new Node(s, v));
            indegree[e]++;
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        int[] result = new int[n + 1];

        while(!queue.isEmpty()) {
            int cur = queue.poll();

            for (Node next : arr.get(cur)) {
                indegree[next.target]--;
                result[next.target] = Math.max(result[next.target], result[cur] + next.value);
                if (indegree[next.target] == 0)
                    queue.offer(next.target);
            }
        }

        int resultCount = 0;
        boolean visited[] = new boolean[n + 1];
        queue = new LinkedList<>();
        queue.offer(end);
        visited[end] = true;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (Node next : reverseArr.get(cur)) {
                if (result[next.target] + next.value == result[cur]) {
                    resultCount++;
                    if (!visited[next.target]) {
                        visited[next.target] = true;
                        queue.offer(next.target);
                    }
                }
            }
        }
        System.out.println(result[end]);
        System.out.println(resultCount);
    }
}
