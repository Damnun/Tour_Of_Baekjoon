import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

public class b5800 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer n = Integer.parseInt(st.nextToken());

        for (int i = 1; i < n + 1; i++) {
            System.out.println("Class " + i);
            st = new StringTokenizer(br.readLine());
            Integer m = Integer.parseInt(st.nextToken());

            ArrayList<Integer> data = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                data.add(Integer.parseInt(st.nextToken()));
            }

            Collections.sort(data);
            Integer gap = -1;
            for (int j = m - 1; j > 0; j--) {
                if (data.get(j) - data.get(j - 1) > gap)
                    gap = data.get(j) - data.get(j - 1);
            }

            System.out.println("Max " + data.get(m - 1) + ", Min " + data.get(0) + ", Largest gap " + gap);

        }
    }
}
