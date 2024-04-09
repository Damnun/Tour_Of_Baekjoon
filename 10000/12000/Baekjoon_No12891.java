import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b12891 {

    static int checkArr[];
    static int arr[];
    static int validation;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int result = 0;

        char a[] = new char[s];
        checkArr = new int[4];
        arr = new int[4];
        validation = 0;

        a = br.readLine().toCharArray();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            checkArr[i] = Integer.parseInt(st.nextToken());
            if (checkArr[i] == 0)
                validation++;
        }

        for (int i = 0; i < p; i++) {
            add(a[i]);
        }

        if (validation == 4)
            result++;

        for (int i = p; i < s; i++) {
            int j = i - p;
            add(a[i]);
            remove(a[j]);
            if (validation == 4)
                result++;
        }
        System.out.println(result);
        br.close();
    }

    private static void add(char c) {
        switch (c) {
            case 'A':
                arr[0]++;
                if (arr[0] == checkArr[0])
                    validation++;
                break;
            case 'C':
                arr[1]++;
                if (arr[1] == checkArr[1])
                    validation++;
                break;
            case 'G':
                arr[2]++;
                if (arr[2] == checkArr[2])
                    validation++;
                break;
            case 'T':
                arr[3]++;
                if (arr[3] == checkArr[3])
                    validation++;
                break;
        }
    }

    private static void remove(char c) {
        switch (c) {
            case 'A':
                if (arr[0] == checkArr[0])
                    validation--;
                arr[0]--;
                break;
            case 'C':
                if (arr[1] == checkArr[1])
                    validation--;
                arr[1]--;
                break;
            case 'G':
                if (arr[2] == checkArr[2]) {
                    validation--;
                }
                arr[2]--;
                break;
            case 'T':
                if (arr[3] == checkArr[3]) {
                    validation--;
                }
                arr[3]--;
                break;
        }
    }
}
