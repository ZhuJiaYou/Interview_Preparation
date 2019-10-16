#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution 
{
public:
    string intToRoman(int num) 
	{
        vector<string> M = {"", "M", "MM", "MMM"};
		vector<string> C = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
		vector<string> X = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
	    vector<string> I = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

		return M[num/1000]+C[(num%1000)/100]+X[(num%100)/10]+I[num%10];
    }
};


int main()
{
	Solution sln;
	cout << sln.intToRoman(3) << endl;
	cout << sln.intToRoman(9) << endl;
	cout << sln.intToRoman(1994) << endl;
	cout << sln.intToRoman(58) << endl;
	return 0;
}

