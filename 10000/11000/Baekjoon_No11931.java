import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class b11931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Integer N = Integer.parseInt(br.readLine());
        ArrayList<Integer> data = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            data.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(data);

        for (int i = data.size() - 1; i >= 0; i--) {
            bw.write(data.get(i) + "\n");
        }
        bw.flush();
    }
}
