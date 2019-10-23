#include <iostream>
#include <vector>

#define MAX(a, b) (a)>=(b)?(a):(b)
#define MIN(a, b) (a)<=(b)?(a):(b)

using namespace std;

int max_value_with_multi_knapsack(int m, vector<int> &weights, vector<int> &values, vector<int> &nums, int n)
{
	vector<int> max_values(n+1, 0);
	int count;
	for (int i=0; i<m; ++i)
		for (int j=n; j>=weights[i]; --j)
		{
			count = MIN(j/weights[i], nums[i]);
			for (int k=1; k<=count; ++k)
				max_values[j] = MAX(max_values[j-k*weights[i]]+k*values[i], max_values[j]);
		}

	return max_values[n];
}

int main()
{
	vector<int> weights = {1, 2, 3, 4};
	vector<int> values = {2, 4, 4, 5};
	vector<int> nums = {3, 1, 3, 2};

	cout << max_value_with_multi_knapsack(4, weights, values, nums, 6) << endl;

	return 0;
}
