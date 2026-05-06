class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> chars= new HashSet<>();
        int res=0;
        int l=0;
        for (int r=0; r<s.length();r++){
            while (chars.contains(s.charAt(r))){
                chars.remove(s.charAt(l));
                l+=1;
            }
            chars.add(s.charAt(r));
            res= Math.max(res,chars.size());
        }
        return res;
    }
}
