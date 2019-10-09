#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstdlib>

using namespace std;

class RandomizedSet 
{
private:
	unordered_map<int, int> indexs;
	vector<int> data;
public:
    /** Initialize your data structure here. */
    RandomizedSet() 
	{
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) 
	{
		if (indexs.find(val) != indexs.end())
		{
			return false;
		}
		data.push_back(val);
		indexs[val] = data.size() - 1;
		return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) 
	{
		if (indexs.find(val) != indexs.end())
		{
			indexs[data.back()] = indexs[val];
			data[indexs[val]] = data.back();
			data.pop_back();
			indexs.erase(val);
			return true;
		}
		return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() 
	{
		return data[rand()%data.size()];
	}
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

int main()
{
	RandomizedSet* obj = new RandomizedSet();
	int val = 1;
	bool param_1 = obj->insert(val);
	val = 2;
	bool param_2 = obj->remove(val);
	int param_3 = obj->getRandom();
	cout << param_1 << endl;
	cout << param_2 << endl;
	cout << param_3 << endl;
	return 0;
}
