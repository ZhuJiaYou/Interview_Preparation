#include <iostream>
#include <vector>
#include <string>

#define MAX(a, b) (a)>=(b)?(a):(b)

using namespace std;

class Solution 
{
public:
    int findMaxForm(vector<string>& strs, int m, int n) 
	{
		vector<vector<int>> counts;
		vector<int> count_now(2, 0);
		for (auto &s : strs)
		{
			count_now[0] = 0;
			count_now[1] = 0;
			for (auto c : s)
			{
				if (c == '0')
					++count_now[0];
				else
					++count_now[1];
			}
			counts.push_back(count_now);
		}

        vector<vector<int>> max_strs(m+1, vector<int>(n+1, 0));
		for (int i=0; i<counts.size(); ++i)
		{
			for (int j=m; j>=counts[i][0]; --j)
				for (int k=n; k>=counts[i][1]; --k)
				{
					max_strs[j][k] = MAX(max_strs[j-counts[i][0]][k-counts[i][1]]+1, max_strs[j][k]);
				}
		}
		//cout << max_strs[m][n] << endl;

		/*
		for (auto &a : counts)
			for (auto b : a)
				cout << b << ends;
			cout << endl;
		*/

		return max_strs[m][n];
    }
};

int main()
{
	Solution sln;
	vector<string> strs = {"10", "0001", "111001", "1", "0"};
	cout << sln.findMaxForm(strs, 5, 3) << endl;

	return 0;
}
