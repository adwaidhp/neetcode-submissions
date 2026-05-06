class Solution {
    public String lowerAlphaString(String s){
        List<Character> list= new ArrayList<>();

        char[] sArr= s.toCharArray();
        String out= "";
        for (char ch: sArr){
            if (Character.isLetter(ch)){
                out = out +Character.toLowerCase(ch);
            }
            if (Character.isDigit(ch)){
                out = out +ch;
            }
        }
        return out;

    }

    public boolean isPalindrome(String s) {
        s= lowerAlphaString(s);
        char[] sArr = s.toCharArray();
        int j= s.length()-1;
        for (int i=0;i<s.length() && j>=0;i++){
            if (s.charAt(i)!=(s.charAt(j))) return false;
            j--;
        }
        return true;




    }
}
