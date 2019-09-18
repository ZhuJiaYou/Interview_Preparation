#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

using namespace std;

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }
int div2zero(int a, int b)
{
	bool flag = ((a ^ b) < 0);
	if (flag)
		return -(abs(a)/abs(b));
	else
		return abs(a)/abs(b);

}

class Solution
{
public:
	int calculate(string s)
	{
		vector<int> nums;
		vector<string> ops;
		vector<string> data;
		unordered_map<string, int> priorites = {{"+", 1}, {"-", 1}, {"*", 2}, {"/", 2}};
		unordered_map<string, int(*)(int, int)> c2op = {{"+", add}, {"-", sub}, {"*", mul}, {"/", div2zero}};
		string oops = "+-*/";
		int i = 0;
		int flag = 0;
		while (i < s.size())
		{
			if (oops.find(s[i]) != string::npos)
			{
				s.insert(i, 1, ' ');
				s.insert(i+2, 1, ' ');
				i += 3;
				flag += 1;
			}
			i += 1;
		}
		cout << s << endl;
		stringstream ss;
		ss << s;
		int d;
		string ts;
		// cout << flag << "&&&" << endl;
		while (flag > 0)
		{
			ss >> d;
			nums.push_back(d);
			ss >> ts;
			if (ops.empty() or priorites[ops.back()]<priorites[ts])
			{
				ops.push_back(ts);
			}
			else
			{
				while (!ops.empty() && priorites[ops.back()]>=priorites[ts])
				{
					int c1 = nums.back();
					nums.pop_back();
					int c2 = nums.back();
					nums.pop_back();
					nums.push_back(c2op[ops.back()](c2, c1));
					cout << ops.back() << c1 << c2 << endl;
					ops.pop_back();
				}
				ops.push_back(ts);
			}
			--flag;
		}

		ss >> d;
		nums.push_back(d);
		while (!ops.empty())
		{
			int c1 = nums.back();
			nums.pop_back();
			int c2 = nums.back();
			nums.pop_back();
			nums.push_back(c2op[ops.back()](c2, c1));
			cout << ops.back() << c1 << c2 << endl;
			ops.pop_back();
		}
		
		
		for (auto d : nums)
			cout << d << "&^*&^" << endl;
		for (auto ts : ops)
			cout << ")(*&&*" << ts;
		
		cout << nums.back() << endl;
		
		return 0;

	}
};


class Solution2
{
public:
	int calculate(string s)
	{
		stringstream ss("+"+s);
		char op;
		int n, last, ans = 0;
		while (ss >> op >> n)
		{
			if (op == '+' || op == '-')
			{
				n = op=='+'?n:-n;
				ans += n;
			}
			else
			{
				n = op=='*'?last*n:last/n;
				ans = ans - last + n;
			}
			last = n;
		}
		return ans;
	}
};

int main()
{
	string statm = "2+3+4";
	Solution2 sln;
	cout << sln.calculate(statm) << endl;

	return 0;
}
