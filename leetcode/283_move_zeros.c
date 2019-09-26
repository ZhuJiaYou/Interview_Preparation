void moveZeroes(int* nums, int numsSize){
    int j = 0;
    for (int i=0; i<numsSize; ++i)
    {
        if (nums[i] != 0)
        {
            nums[j++] = nums[i];
        }
    }
    for (; j<numsSize; ++j)
    {
        nums[j] = 0;
    }
}
