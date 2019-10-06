#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
	vector<int> topKFrequent(vector<int>& nums, int k)
	{
		unordered_map<int, int> cnt;
		for (auto num : nums)
		{
			++cnt[num];
		}

		vector<int> res;
		int low, high, mid;
		bool flag = false;
		for (auto it=cnt.cbegin(); it!=cnt.cend(); ++it)
		{
			low = 0;
			high = res.size() - 1;
			while (low <= high)
			{
				mid = (low + high) / 2;
				if ((mid<1 || cnt[res[mid-1]]>=it->second) && cnt[res[mid]]<=it->second)
				{
					res.insert(res.begin()+mid, it->first);
					flag = true;
					break;
				}
				else if (cnt[res[mid]] > it->second)
					low = mid + 1;
				else
					high = mid - 1;
			}
			if (!flag)
			{
				res.insert(res.begin()+low, it->first);
			}
			flag = false;
		}
		res.erase(res.begin()+k, res.end());
		return res;
	}
};

int main()
{
	Solution sln;
	vector<int> nums = {1, 1, 1, 2, 2, 3};

	nums = sln.topKFrequent(nums, 2);
	for (auto num : nums)
	{
		cout << num << " ";
	}
	cout << endl;

	return 0;
}
