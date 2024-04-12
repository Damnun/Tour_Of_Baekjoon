import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        StringTokenizer st;
        HashMap<String, Integer> hashMap = new HashMap<>();
        HashMap<String, Integer> resultTime = new HashMap<>();
        
        // fees : 기본 시간 (분) / 기본 요금 (원) / 단위 시간 (분) / 단위 요금 (원)
        for (int i = 0; i < records.length; i++) {
            st = new StringTokenizer(records[i]);
            
            String[] time = st.nextToken().split(":");
            int calcTime = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            String carNumber = st.nextToken();
            String inOrOut = st.nextToken();
            
            if (inOrOut.equals("IN")) { 
                hashMap.put(carNumber, calcTime);
            }
            
            else if (inOrOut.equals("OUT")) {
                int resultTimeValue = calcTime - hashMap.get(carNumber);
                resultTime.put(carNumber, resultTime.getOrDefault(carNumber, 0) + resultTimeValue);
                hashMap.remove(carNumber);
            }
            
        }
        
        for (String s : hashMap.keySet()) {
            int resultTimeValue = 24 * 60 - hashMap.get(s) - 1;
            resultTime.put(s, resultTime.getOrDefault(s, 0) + resultTimeValue);
        }
        
        HashMap<Integer, Integer> resultMap = new HashMap<Integer, Integer>();
        for (String s : resultTime.keySet()) {
            int cost;
            if (resultTime.get(s) - fees[0] < 0)
                cost = fees[1];
            else {
                cost = fees[1] + ((resultTime.get(s) - fees[0]) / fees[2]) * fees[3];
                if ((resultTime.get(s) - fees[0]) % fees[2] != 0)
                cost += fees[3];
            }
            
            resultMap.put(Integer.parseInt(s), cost);
        }
    
        int[] answer = new int[resultMap.size()];
        int idx = 0;
        
        Object[] sortKey = resultMap.keySet().toArray();
        Arrays.sort(sortKey);
        
        for (int i = 0; i < sortKey.length; i++) {
            answer[i] = resultMap.get(sortKey[i]);
        }
    
        return answer;
    }
}
