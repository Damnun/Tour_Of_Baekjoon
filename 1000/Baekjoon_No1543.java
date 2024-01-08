import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b1543 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String data = br.readLine();
        String target = br.readLine();

        Integer dataSize = data.length();
        Integer targetSize = target.length();

        data = data.replace(target, "");
        System.out.println(((dataSize - data.length())) / targetSize);
    }
}
