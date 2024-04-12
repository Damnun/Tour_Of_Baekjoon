import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> wantList = new HashMap<String, Integer>();
        HashMap<String, Integer> tmpList;
        boolean isAlright;
        int result = 0;

        for (int i = 0; i < number.length; i++) {
            wantList.put(want[i], number[i]);
        }

        for (int i = 0; i <= discount.length - 10; i++) {
            tmpList = new HashMap<String, Integer>(wantList);
            for (int j = i; j < 10 + i; j++) {
                if (tmpList.containsKey(discount[j]))
                    tmpList.put(discount[j], tmpList.get(discount[j]) - 1);
            }
            
            isAlright = true;
            for (String x : tmpList.keySet()) {
                if (tmpList.get(x) != 0) {
                    isAlright = false;
                    break;
                }
            }
            
            if (isAlright) result++;
        }

        return result;
    }
}
