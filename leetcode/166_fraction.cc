#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using std::cout;
using std::endl;
using std::string;
using std::to_string;
using std::vector;
using std::find;
using std::unordered_map;

class Solution 
{
public:
    string fractionToDecimal(int numerator, int denominator) 
	{
		if (denominator == 0)
			return "";
		if (numerator == 0)
			return "0";
		unordered_map<long, int> appeared;
		string ans;
		long p_int = abs((long)numerator / (long)denominator);
		ans += string((numerator < 0) ^ (denominator < 0), '-');
		ans += to_string(p_int);
		long rem  = abs((long)numerator % (long)denominator);
		if (rem == 0)
			return ans;

		ans += '.';
		while (rem)
		{
			appeared[rem] = ans.size();
			rem *= 10;
			ans += to_string(rem / abs((long)denominator));
			rem %= abs((long)denominator);
			if (appeared.find(rem) != appeared.end())
			{
				ans.insert(appeared[rem], "(");
				ans += ")";
				break;
			}
		}
		return ans;
    }
};



int main()
{
	Solution s1;
	cout << s1.fractionToDecimal(-1, ) << endl;
	return 0;
}
