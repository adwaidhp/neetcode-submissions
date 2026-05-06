class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack =new Stack<>();
        Map<Character,Character> closeMap= new HashMap<>();
        closeMap.put(')','(');
        closeMap.put(']','[');
        closeMap.put('}','{');
        for (char c: s.toCharArray()){
            if (closeMap.containsKey(c)){
                if (!stack.isEmpty() && stack.peek()==closeMap.get(c)){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }
        if (stack.isEmpty()) return true;
        return false;
    }
}
