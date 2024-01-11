import javax.lang.model.type.ArrayType;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class b2628 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer n = Integer.parseInt(st.nextToken());
        Integer m = Integer.parseInt(st.nextToken());
        Integer sliceCount = Integer.parseInt(br.readLine());

        ArrayList<Integer> xList = new ArrayList<>();
        xList.add(0);
        xList.add(m);

        ArrayList<Integer> yList = new ArrayList<>();
        yList.add(0);
        yList.add(n);

        for (int i = 0; i < sliceCount; i++) {
            st = new StringTokenizer(br.readLine());
            Integer xy = Integer.parseInt(st.nextToken());
            Integer sliceNumber = Integer.parseInt(st.nextToken());

            if (xy == 0) {
                xList.add(sliceNumber);
            }

            else if (xy == 1) {
                yList.add(sliceNumber);
            }
        }

        Collections.sort(xList);
        Collections.sort(yList);

        Integer tmpX = 0;
        Integer tmpY = 0;

        for (int i = xList.size() - 1; i > 0; i--) {
            if (xList.get(i) - xList.get(i - 1) > tmpX)
                tmpX = xList.get(i) - xList.get(i - 1);
        }

        for (int i = yList.size() - 1; i > 0; i--) {
            if (yList.get(i) - yList.get(i - 1) > tmpY)
                tmpY = yList.get(i) - yList.get(i - 1);
        }

        if (tmpX == 0) tmpX = m;
        if (tmpY == 0) tmpY = n;

//        System.out.println(xList);
//        System.out.println(yList);
//        System.out.println(tmpX + " " + tmpY);
        System.out.println(tmpX * tmpY);
    }
}
