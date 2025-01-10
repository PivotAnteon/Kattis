int main(){
    int m = 3, n = 3;
    int nums1[] = {1,2,3,0,0,0};
    int nums2[] = {2,3,4};

    merge(nums1, sizeof(nums1), m, nums2, sizeof(nums2), n);
    return 0;
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;  // Last index of valid elements in nums1
    int j = n - 1;  // Last index of nums2
    int k = m + n - 1;  // Last index of nums1 array

    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }

    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}