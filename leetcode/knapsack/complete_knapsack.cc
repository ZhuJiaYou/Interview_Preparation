#include <iostream>
#include <vector>

#define MAX(a, b) (a)>=(b)?(a):(b)

using namespace std;

int max_value_with_complete_knapsack(int m, vector<int> &weights, vector<int> &values, int n)
{
	vector<int> max_values(n+1, 0);
	for (int i=0; i<m; ++i)
		for (int j=weights[i]; j<=n; ++j)
		{
			max_values[j] = MAX(max_values[j-weights[i]]+values[i], max_values[j]);
		}

	return max_values[n];
}

int main()
{
	vector<int> weights = {0, 5, 8};
	vector<int> values = {0, 5, 7};

	cout << max_value_with_complete_knapsack(3, weights, values, 10) << endl;

	return 0;
}
