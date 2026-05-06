class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> setnums= new HashSet();
        for (int i=0;i<nums.length;i++){
            if (setnums.contains(nums[i])){
                return true;
            }
            else{
                setnums.add(nums[i]);
            }
        }
        return false;
    }
}