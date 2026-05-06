class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> sMap = new HashMap();
        HashMap<Character,Integer> tMap = new HashMap();
        char[] sArr=s.toCharArray();
        char[] tArr=t.toCharArray();
        for (char a : sArr){
            if (sMap.get(a)==null) sMap.put(a,1);
            else sMap.put(a,sMap.get(a)+1);
        }
        for (char a : tArr){
            if (tMap.get(a)==null) tMap.put(a,1);
            else tMap.put(a,tMap.get(a)+1);
        }
        return sMap.equals(tMap);
    }
}
