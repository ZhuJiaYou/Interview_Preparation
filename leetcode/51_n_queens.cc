#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    vector<vector<string>> solveNQueens(int n)
	{
		vector<vector<string>> slns;
		vector<string> one(n, string(n, '.'));

		/*
        flag[0] to flag[n - 1] to indicate if the column had a queen before.
        flag[n] to flag[3 * n - 2] to indicate if the 45° diagonal had a queen before.
        flag[3 * n - 1] to flag[5 * n - 3] to indicate if the 135° diagonal had a queen before.
        */
		vector<int> flags(5*n-2, 1);
		solve(slns, one, flags, 0, n);

		return slns;
	}

private:
	void solve(vector<vector<string>> &slns, vector<string> &one, vector<int>flags, int row, int &n)
	{
		if (row == n)
		{
			slns.push_back(one);
			return;
		}

		for (int col=0; col<n; ++col)
		{
			if (flags[col] && flags[n+row+col] && flags[4*n-2+col-row])
			{
				flags[col] = flags[n+row+col] = flags[4*n-2+col-row] = 0;
				one[row][col] = 'Q';
				solve(slns, one, flags, row+1, n);
				one[row][col] = '.';
				flags[col] = flags[n+row+col] = flags[4*n-2+col-row] = 1;
			}
		}
	}
};

int main()
{

	return 0;
};
