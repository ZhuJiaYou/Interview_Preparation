#include <iostream>
#include <vector>
#include <numeric>
#include <cstdlib>
#include <algorithm>

using namespace std;

class Solution 
{
public:
    int threeSumClosest(vector<int>& nums, int target) 
	{
		if (nums.size() <= 3)
			return accumulate(nums.begin(), nums.end(), 0);

		sort(nums.begin(), nums.end());

		int i, j, k, temp;
		int closet = nums[0] + nums[1] + nums[2];
		for (i=0; i<nums.size()-2; ++i)
		{
			j = i + 1;
			k = nums.size() - 1;
			while (j < k)
			{
				temp = nums[i] + nums[j] + nums[k];
				if (abs(target-temp) < abs(target-closet))
					closet = temp;
				if (temp < target)
					++j;
				else if (temp > target)
					--k;
				else
					return temp;
			}
		}
		return closet;        
    }
};

int main()
{
	Solution sln;
	vector<int> nums = {-1, 2, 1, -4};

	cout << sln.threeSumClosest(nums, 1) << endl;

	return 0;
}
