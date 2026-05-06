class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()> s2.length()) return false;
        HashMap<Character,Integer> s1count= new HashMap<>();
        HashMap<Character,Integer> s2count= new HashMap<>();
        for (int i=0;i<26;i++){
            s1count.put((char)(97+i),0);
            s2count.put((char)(97+i),0);
        }

        for (int i=0;i<s1.length();i++){
            s1count.put(s1.charAt(i),s1count.get(s1.charAt(i))+1);
        }

        int l=0;
        for (int r=0;r<s2.length();r++){
            if (r-l>=s1.length()){
                s2count.put(s2.charAt(l),s2count.get(s2.charAt(l))-1);
                l+=1;
            }
            s2count.put(s2.charAt(r),s2count.get(s2.charAt(r))+1);
            if (s1count.equals(s2count)){
                return true;
            }
        }
        return false;
    }
}
