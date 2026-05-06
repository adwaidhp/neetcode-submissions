class Solution {
    public int[] productExceptSelf(int[] nums) {
        int totalProd=1;
        int flag=0;
        for (int num : nums){
            if (num ==0){
                flag++;
                continue;
            };
            totalProd*=num;
        }
        int[] result= new int[nums.length];
        if (flag==0){
            for (int i=0;i<nums.length;i++){
                result[i]=totalProd/nums[i];
            }
        }
        else{
            for (int i=0;i<nums.length;i++){
                if (nums[i]==0 && flag==1){
                    result[i]=totalProd;
                }
                else if (nums[i]==0 && flag>1){
                    result[i]=0;
                }
                else{
                    result[i]=0;
                }
            }
        }
    return result;
    }
}  
