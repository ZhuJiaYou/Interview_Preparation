#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
	vector<string> fizzBuzz(int n)
	{
		vector<string> res;
		int flag3=0, flag5=0;
		for (int i=1; i<=n; ++i)
		{
			++flag3;
			++flag5;
			if (flag3==3 && flag5==5)
			{
				res.push_back("FizzBuzz");
				flag3 = 0;
				flag5 = 0;
			}
			else if (flag3 == 3)
			{
				res.push_back("Fizz");
				flag3 = 0;
			}
			else if (flag5 == 5)
			{
				res.push_back("Buzz");
				flag5 = 0;
			}
			else
			{
				res.push_back(to_string(i));
			}
		}
		return res;
	}
};

int main()
{
	Solution sln;
	auto res = sln.fizzBuzz(15);
	for (auto s : res)
	{
		cout << s << " ";
	}
	cout << endl;

	return 0;
}
