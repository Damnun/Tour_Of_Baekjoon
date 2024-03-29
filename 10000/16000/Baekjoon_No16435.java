import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class b16435 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> fruitList = new ArrayList<>();
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            fruitList.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(fruitList);

        for (int i = 0; i < n; i++) {
            if (fruitList.get(i) <= l) {
                l++;
            }
        }
        System.out.println(l);
    }
}
