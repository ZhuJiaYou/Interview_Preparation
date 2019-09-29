#include <stdio.h>
#include <stdlib.h>

int lengthOfLIS(int* nums, int numsSize){
	if (numsSize <= 0)
	    return 0;
	int size=0;
    int tails[numsSize];
    int low, high, mid;
    for (int i=0; i<numsSize; ++i)
    {
        low = 0;
	    high = size;
	    while (low < high)
	    {
	        mid = (low+high)/2;
		    if (tails[mid] < nums[i])
		        low = mid + 1;
			else
			    high = mid;
		}
		tails[low] = nums[i];
		size = (low+1) > size ? (low+1) : size;
	}
	return size;
}

int main()
{
	int arr[8] = {10, 9, 2, 5, 3, 7, 101, 18};
	printf("%d\n", lengthOfLIS(arr, 8));
	return 0;
}
