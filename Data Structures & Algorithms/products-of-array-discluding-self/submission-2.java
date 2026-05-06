class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix= new int[nums.length];
        int[] suffix= new int[nums.length];
        int[] result= new int[nums.length];
        prefix[0]=1;
        suffix[nums.length-1]=1;
        for (int i=1;i<nums.length;i++){
            prefix[i]=prefix[i-1]*nums[i-1];
        }
        for (int i=nums.length-2;i>=0;i--){
            suffix[i]=suffix[i+1]*nums[i+1];
        }
        for (int i=0;i<nums.length;i++){
            result[i]=prefix[i]*suffix[i];
        }
        return result;

        /*int totalProd=1;
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
    return result;*/
    }
}  
