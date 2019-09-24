#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
	bool searchMatrix(vector<vector<int>>& matrix, int target) {
		if (matrix.empty())
			return false;
		int l1 = matrix.size();
		int l2 = matrix[0].size();
		int i = 0, j = l2 - 1;
		while (i<l1 && j >=0)
		{
			if (matrix[i][j] == target)
				return true;
			else if (matrix[i][j] > target)
				--j;
			else
				++i;
		}
		return false;
	}
};

int main()
{
	Solution sln;
	vector<vector<int>> matrix = {{1, 4, 7, 11, 15},
	                              {2, 5, 8, 12, 19},
	                              {10, 13, 14, 17, 24},
	                              {18, 21, 23, 26, 30}};
	cout << sln.searchMatrix(matrix, 5) << endl;
	cout << sln.searchMatrix(matrix, 20) << endl;

	return 0;
}
