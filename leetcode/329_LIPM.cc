#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
	public:
		int dfs(int i, int j, vector<vector<int>> &matrix, vector<vector<bool>> &marks, vector<vector<int>> &paths, int now)
		{
			if (marks[i][j] == false)
			{
				++now;
				marks[i][j] = true;
				int tmp2 = matrix[i][j];
				int tmp = now;
				int lg = now;
				if (i-1>-1 && matrix[i-1][j]>tmp2)
				{
					tmp = dfs(i-1, j, matrix, marks, paths, now);
					if (lg < tmp)
						lg = tmp;
				}
				if (j-1>-1 && matrix[i][j-1]>tmp2)
				{
					tmp = dfs(i, j-1, matrix, marks, paths, now);
					if (lg < tmp)
						lg = tmp;
				}
				if (i+1<matrix.size() && matrix[i+1][j]>tmp2)
				{
					tmp = dfs(i+1, j, matrix, marks, paths, now);
					if (lg < tmp)
						lg = tmp;
				}
				if (j+1<matrix[0].size() && matrix[i][j+1]>tmp2)
				{
					tmp = dfs(i, j+1, matrix, marks, paths, now);
					if (lg < tmp)
						lg = tmp;
				}
				paths[i][j] = lg - now + 1;
				cout << i << "--" << j << "++" << lg << "--" << paths[i][j] << endl;
				return lg;
			}
			else
			{
				cout << i << "**" << j << "**" << now << "**" << paths[i][j] << endl;
				return now+paths[i][j];
			}
		}

		int longestIncreasingPath(vector<vector<int>>& matrix) 
		{
			if (matrix.empty())
				return 0;
			int LM = matrix.size();
			int LV = matrix[0].size();
			vector<vector<bool>> marks;
			vector<vector<int>> paths;
			vector<bool> tmp;
			vector<int> path;
			for (int i=0; i<LM; ++i)
			{
				for (int j=0; j<LV; ++j)
				{
					tmp.push_back(false);
					path.push_back(1);
				}
				marks.push_back(tmp);
				paths.push_back(path);
			}

			int longest = 0;
			int now;
			for (int i=0; i<LM; ++i)
			{
				for (int j=0; j<LV; ++j)
				{
					if ((now=dfs(i, j, matrix, marks, paths, 0)) > longest)
						longest = now;
				}
			}

			return longest;
		}
};

int main()
{
	Solution sln;
	vector<vector<int>> matrix = {{9, 9, 4},
	                              {6, 6, 8},
	                              {2, 1, 1}};
	matrix = {{3, 4, 5},
	          {3, 2, 6},
	          {2, 2, 1}};
	cout << sln.longestIncreasingPath(matrix) << endl;
	return 0;
}
