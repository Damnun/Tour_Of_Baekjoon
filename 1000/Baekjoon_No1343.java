import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1343 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String data = br.readLine();
        data = data.replace("XXXX", "AAAA");
        data = data.replace("XX", "BB");

        if (data.contains("X"))
            System.out.println("-1");
        else
            System.out.println(data);
    }
}
