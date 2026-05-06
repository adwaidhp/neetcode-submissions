class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> maps= new HashMap<>();
        for (int num: nums){
            maps.put(num,maps.getOrDefault(num,0)+1);
        }
        List<Integer>[] count = new List[nums.length+1];
        for (int num: maps.keySet()){
            if (count[maps.get(num)]==null){
                count[maps.get(num)]= new ArrayList<>();
            }
            count[maps.get(num)].add(num);
        }
        int[] result= new int[k];
        int counter=0;
        for (int c=nums.length;c>=0 && counter<k;c--){
            if (count[c]!=null){
                for (int num:count[c]){
                    result[counter++]=num;
                    if (counter ==k) break;
                }
            }
        }
        return result;

    }
}
