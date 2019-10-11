#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution 
{
public:
	vector<int> maxSlidingWindow(vector<int> &nums, int k)
	{
		deque<int> dq;
		vector<int> results;
		for (int i=0; i<nums.size(); ++i)
		{
			while (!dq.empty() && nums[dq.back()]<=nums[i])
			{
				dq.pop_back();
			}

			if (!dq.empty() && i-dq.front()>=k)
			{
				dq.pop_front();
			}

			dq.push_back(i);
			if (i >= k-1)
				results.push_back(nums[dq.front()]);
		}
		return results;
	}
};

int main()
{
	vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
	Solution sln;
	nums = sln.maxSlidingWindow(nums, 3);
	for (auto n : nums)
	{
		cout << n << " ";
	}
	cout << endl;

	return 0;
}
