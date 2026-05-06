class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<ArrayList<Integer>,ArrayList<String>> res= new HashMap<>();
        for (String str: strs){
            ArrayList<Integer> count= new ArrayList<>(Collections.nCopies(26,0));
            for (char c : str.toCharArray()){
                count.set(c-'a',count.get(c-'a')+1);
            }
            res.putIfAbsent(count,new ArrayList<>());
            res.get(count).add(str);
        }
        return new ArrayList<>(res.values());
    }
}
