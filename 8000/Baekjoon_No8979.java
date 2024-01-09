import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class b8979 {
    static class Nation implements Comparable<Nation> {
        private int name, gold, silver, bronze, rank;

        public Nation(int name, int gold, int silver, int bronze) {
            super();

            this.name = name;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
            this.rank = 1;
        }

        @Override
        public int compareTo(Nation nation) {
            if (this.gold == nation.gold) {
                if (this.silver == nation.silver) {
                    return nation.bronze - this.bronze;
                }
                else {
                    return nation.silver - this.silver;
                }
            }
            else {
                return nation.gold - this.gold;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        List<Nation> medalList = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int name = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());

            Nation nation = new Nation(name, gold, silver, bronze);
            medalList.add(nation);
        }

        Collections.sort(medalList);

        for (int i = 1; i < n; i++) {
            Nation origin = medalList.get(i - 1);
            Nation next = medalList.get(i);

            if (origin.gold == next.gold && origin.silver == next.silver && origin.bronze == next.bronze) {
                next.rank = origin.rank;
            }
            else {
                next.rank = i + 1;
            }
        }

        medalList.stream().filter(t -> t.name == k)
                .map(t -> t.rank)
                .forEach(System.out::println);
    }
}
