import java.util.*;

class Solution {
    
    static class File {
        String name;
        String head;
        int number;
        
        public File (String name, String head, int number) {
            this.name = name;
            this.head = head;
            this.number = number;
        }
    }
    
    public String[] solution(String[] files) {
        File[] fileList = new File[files.length];
        
        for (int i = 0; i < files.length; i++) {
            String[] split = splitFileName(files[i]);
            fileList[i] = new File(files[i], split[0], Integer.parseInt(split[1]));
        }
        
        Arrays.sort(fileList, (o1, o2) -> {
            if (o1.head.equals(o2.head))
                return o1.number - o2.number;
            else
                return o1.head.compareTo(o2.head);
        });
        
        String[] answer = new String[files.length];
        for (int i = 0; i < files.length; i++)
            answer[i] = fileList[i].name;
        
        return answer;
    }

    public static String[] splitFileName(String file) {
        String str[] = new String[3];
        str[0] = "";
        str[1] = "";
        str[2] = "";
        
        int index = 0;
        for (int i = 0; i < file.length(); i++) {
            char c = file.charAt(i);
            
            if (index == 0 && !Character.isDigit(c)) {
                str[index] += c;
                continue;
            }
            
            if (index == 0 && Character.isDigit(c))
                index++;
            
            if (index == 1 && Character.isDigit(c)) {
                str[index] += c;
                continue;
            }
            
            if (index == 1 && !Character.isDigit(c))
                index++;
            
            str[index] += c;
        }
        
        str[0] = str[0].toLowerCase();
        return str;
    }
}
