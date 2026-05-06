class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> scount = new HashMap<>();
        int l=0;
        int res=0;
        for (int r=0;r<s.length();r++){
            scount.put(s.charAt(r),scount.getOrDefault(s.charAt(r),0)+1);
            while ((r-l+1)- Collections.max(scount.values())>k){
                scount.put(s.charAt(l),scount.get(s.charAt(l))-1);
                l+=1;
            }
            res= Math.max(res,r-l+1);
        }
        return res;
    }
}
