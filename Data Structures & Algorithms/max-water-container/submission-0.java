class Solution {
    public int maxArea(int[] heights) {
        int[] nums= heights;
        int max=0;
        for (int i=0;i<nums.length;i++){
            for(int j=i; j < nums.length;j++ ){
                int lesser = nums[i]<nums[j] ?  nums[i] :nums[j];
                int water= (j-i)*lesser;
                max= Math.max(max,water);

            }
        }
        return max;
    }
}
