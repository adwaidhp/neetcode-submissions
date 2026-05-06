class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";
        HashMap<Character,Integer> countT= new HashMap<>();
        HashMap<Character,Integer> window= new HashMap<>();
        int[] res={-1,-1};
        int resLen= Integer.MAX_VALUE;
        int l=0;
        for (char ch: t.toCharArray()){
            countT.put(ch,countT.getOrDefault(ch,0)+1);
        }
        int have=0, need= countT.size();
        for (int r=0;r<s.length();r++){
            char ch= s.charAt(r);
            window.put(ch,window.getOrDefault(ch,0)+1);
            if (countT.containsKey(ch)&& window.get(ch).equals(countT.get(ch))){
                have++;
            }
            while (have==need){
                if((r-l+1)<resLen){
                    resLen= r-l+1;
                    res[0]=l;
                    res[1]=r;
                }
                char leftChar=s.charAt(l);
                window.put(leftChar,window.get(leftChar)-1);
                if (countT.containsKey(leftChar)&& window.get(leftChar)<countT.get(leftChar)){
                    have--;
                }
                l++;
            }
        }
        return resLen == Integer.MAX_VALUE ? "" : s.substring(res[0], res[1] + 1);
     }
}
