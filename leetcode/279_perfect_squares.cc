#include <iostream>
#include <vector>
#include <climits>
#include <cmath>

using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> squares = {0};
		for (int i=1; i<=n; ++i)
		{
			int minsq = INT_MAX;
			for (int j=static_cast<int>(sqrt(i)); j>0; --j)
			{
				minsq = min(minsq, squares[i-j*j]+1);
			}
			squares.push_back(minsq);
		}
		return squares[n];
    }
};

class Solution2 {
	bool isSquare(int n)
	{
		int q = static_cast<int>(sqrt(n));
		if (q * q == n)
			return true;
		else
			return false;
	}
public:
    int numSquares(int n) {
		if (isSquare(n))
			return 1;

		while ((n & 3) == 0)  //  n % 4 == 0
			n >>= 2;
		if ((n & 7) == 7)  //  n % 8 == 7
			return 4;

		for (int j=static_cast<int>(sqrt(n)); j>0; --j)
		{
			if (isSquare(n-j*j))
				return 2;
		}
		return 3;
	}
};

int main()
{
	int n = 12;
	Solution2 sln;
	cout << sln.numSquares(n);

	n = 13;
	cout << sln.numSquares(n);

	return 0;
}
