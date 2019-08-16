#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> permuteUnique(vector<int> &num) 
    {
        sort(num.begin(), num.end());
        int len = num.size();
        recursion(num, 0, len);
        //vector<vector<int>> res;
        //res.assign(result.begin(), result.end());
        return result;
    }
    
    void recursion(vector<int> num,int i,int len)
    {
        if(i==len-1)
        {
            result.push_back(num);
			cout << i  << endl;
        } else 
        {
            for(int k=i; k<len; ++k)
            {
                //如果从i开始的后两个相邻的元素相同，则不需要交换并进行后续的递归调用
                //避免产生重复的元组
				cout << i << " " << k << endl;
				cout << num[i] << num[k] << endl;
                if((i!=k) && (num[i]==num[k]))
                    continue;
				//cout << i << " " << k << endl;
                swap(num[i], num[k]);
                recursion(num, i+1, len);
                // swap(num[k], num[i]);
            }
        }
    }
};

int main()
{
	Solution s = Solution();
	vector<int> v = {0,1,0,0,9};
	vector<vector<int>> res = s.permuteUnique(v);
	for(auto &r1 : res)
	{
		for(auto val : r1)
			cout << val << ends;
		cout << endl;
	}

	return 0;
}
