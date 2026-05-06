class Solution {
    public int longestConsecutive(int[] nums) {
        int longest=0;
        HashSet<Integer> numSet= new HashSet<>();
        for (int num:nums){
            if (!numSet.contains(num)){
            numSet.add(num);}
        }
        
        System.out.println(numSet);
        for (int num: numSet){
            if (!numSet.contains(num-1)){
                int currentNum=num;
                int streak=1;

                while(numSet.contains(currentNum+1)){
                    currentNum++;
                    streak++;
                }

                longest= Math.max(longest,streak);
            }
        }
        return longest;
    }
}
