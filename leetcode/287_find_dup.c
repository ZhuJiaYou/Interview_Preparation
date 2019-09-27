int findDuplicate(int* nums, int numsSize)
{
	int fast=nums[nums[0]], slow=nums[0];
	while (slow != fast)
	{
	    slow = nums[slow];
		fast = nums[nums[fast]];
	}
	fast = 0;
	while (slow != fast)
	{
	    slow = nums[slow];
	    fast = nums[fast];
	}
	return slow;
}
