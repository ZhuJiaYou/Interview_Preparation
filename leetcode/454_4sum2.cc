#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
	int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D)
	{
		unordered_map<int, int> AB;
		for (int i=0; i<A.size(); ++i)
			for (int j=0; j<B.size(); ++j)
				++AB[A[i]+B[j]];

		int s = 0;

		for (int i=0; i<C.size(); ++i)
			for (int j=0; j<D.size(); ++j)
				s += AB[-(C[i]+D[j])];

		return s;
	}
};

int main()
{
	vector<int> A = {1, 2};
	vector<int> B = {-2, -1};
	vector<int> C = {-1, 2};
	vector<int> D = {0, 2};

	Solution sln;
	cout << sln.fourSumCount(A, B, C, D) << endl;
	return 0;
}
