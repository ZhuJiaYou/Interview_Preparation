#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target)
	{
		vector<vector<int>> allans;
		if (nums.size() < 4)
			return allans;

		sort(nums.begin(), nums.end());
		int i, j, p, q, temp, n=nums.size();
		for (i=0; i<n-3; ++i)
		{
			if (nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target)
				break;
			if (nums[n-1]+nums[n-2]+nums[n-3]+nums[i] < target)
				continue;
			if (i>0 && nums[i]==nums[i-1])
				continue;
			for (j=i+1; j<n-2; ++j)
			{
				if (nums[i]+nums[j]+nums[j+1]+nums[j+2] > target)
					break;
				if (nums[n-1]+nums[n-2]+nums[j]+nums[i] < target)
					continue;
				if (j>i+1 && nums[j]==nums[j-1])
					continue;

				p = j + 1;
				q = n - 1;
				while (p < q)
				{
					temp = nums[i] + nums[j] + nums[p] + nums[q];
					if (temp < target)
						++p;
					else if (temp > target)
						--q;
					else
					{
						allans.push_back(vector<int>{nums[i], nums[j], nums[p], nums[q]});
						do {++p;} while (p<q && nums[p]==nums[p-1]);
						do {--q;} while (p<q && nums[q]==nums[q+1]);
					}
				}

			}
		}
        return allans;
    }
};

int main()
{
	Solution sln;
	vector<int> nums = {1, 0, -1, 0, -2, 2};
	vector<vector<int>> allans = sln.fourSum(nums, 0);
	for (auto &ans : allans)
	{
		for (auto a : ans)
			cout << a << " ";
		cout << endl;
	}

	return 0;
}
