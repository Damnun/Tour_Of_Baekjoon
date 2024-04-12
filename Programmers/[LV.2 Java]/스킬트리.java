import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        Queue<Character> queue = new LinkedList<>();
        
        for (int i = 0; i < skill.length(); i++)
            queue.add(skill.charAt(i));
                
        for (int i = 0; i < skill_trees.length; i++) {
            Queue<Character> tmpQueue = new LinkedList<>(queue);
            boolean isAvailable = true;
            char peek = tmpQueue.poll();
            
            for (int j = 0; j < skill_trees[i].length(); j++)
            {
                char currentSkill = skill_trees[i].charAt(j);
                
                if (currentSkill == peek) {
                    if (!tmpQueue.isEmpty()) peek = tmpQueue.poll();
                }
                if (tmpQueue.contains(currentSkill)) isAvailable = false;
            }
            
            if (isAvailable)
                answer++;
            
        }
        
        
        return answer;
    }
}
