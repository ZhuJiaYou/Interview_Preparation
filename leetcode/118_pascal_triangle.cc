#include <iostream>
#include <vector>


using std::endl;
using std::cout;
using std::cin;
using std::vector;
using std::ends;


class Solution 
{
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> triangle;
        
        if(numRows == 0)
            return triangle;
        else if(numRows == 1)
        {
            triangle = {{1}};
            return triangle;
        }

        else if(numRows == 2)
        {
            triangle = {{1}, {1, 1}};
            return triangle;
        }
        
        triangle = {{1}, {1, 1}};
        vector<int> row = {1};
        for(int i=2; i<numRows; ++i)
        {
            for(int j=0; j<triangle.back().size()-1; ++j)
            {
                row.push_back(triangle.back()[j]+triangle.back()[j+1]);
            }
            row.push_back(1);
            triangle.push_back(row);
            row = {1};
        }
        return triangle;
    }
};


int main()
{
	Solution slt;
	int numRows;
	cin >> numRows;
	vector<vector<int>> vv = slt.generate(numRows);
	for(auto vec : vv)
	{
		for(auto v : vec)
		{
			cout << v << " ";
		}
		cout << endl;
	}

	return 0;
}
