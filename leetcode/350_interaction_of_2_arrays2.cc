#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
	vector<int> intersect(vector<int>& nums1, vector<int>& nums2)
	{
		sort(nums1.begin(), nums1.end());
		sort(nums2.begin(), nums2.end());
		nums1.erase(set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), nums1.begin()), nums1.end());
		return nums1;
	}
};

int main()
{
	Solution sln;
	vector<int> nums1 = {1, 2, 2, 1};
	vector<int> nums2 = {2, 2};

	nums1 = sln.intersect(nums1, nums2);
	for (auto num : nums1)
	{
		cout << num << " ";
	}
	cout << endl;

	return 0;
}
