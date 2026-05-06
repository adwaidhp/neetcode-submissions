class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map= new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int elt= target-nums[i];
            if (map.get(elt)==null){
                map.put(nums[i],i);
            }
            else{
                return map.get(elt)>i? new int[]{i,map.get(elt)}: new int[]{map.get(elt),i};
            }
        };
    
    return null;
    };
}
