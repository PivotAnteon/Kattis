import java.util.*;

public class noDoops {
    public static int removeDuplicates(int[] nums) {
        int count = 0;
        HashSet<Integer> seen = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            if(seen.add(nums[i])){
                nums[count] = nums[i];
                count++;
            }
        }

        return count;
    }

    public static void printArray(int[] nums){
        System.out.print("[");
        for(int i = 0;i< nums.length; i++){
            System.out.print(nums[i]);
        }
        System.out.print("]\n");
    }

    public static void main(String[] args){
        int[] nums = {1,1,2};

        removeDuplicates(nums);
        printArray(nums);

    }
}
