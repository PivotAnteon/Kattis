class Solution {
    public static int removeElement(int[] nums, int val) {
        //check if nums has a value
        if(nums.length < 1){
            return 0;
        }

        int k = 0;
        //find all non-val and place in new array, increment k
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k;
    }
    public static void main(String[] args){
        //test 1
        int[] nums ={3,2,2,3};
        int search = 3;

        System.out.println(removeElement(nums, search));

        for(int i = 0; i < nums.length; i++){
            System.out.print(nums[i]);
        }
        System.out.println();

        //test 2
        int[] nums2 = {0,1,2,2,3,0,4,2};
        search = 2;

        System.out.println(removeElement(nums2, search));

        for(int i = 0; i < nums2.length; i++){
            System.out.print(nums2[i]);
        }
        System.out.println();

        int[] nums3 = {2};
        search = 3;

        System.out.println(removeElement(nums3, search));

        for(int i = 0; i < nums3.length; i++){
            System.out.print(nums3[i]);
        }
        System.out.println();
    }
}