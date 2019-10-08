class Solution {
private:
	vector<int> data;
public:
	Solution(vector<int>& nums) {
		data = nums;
	}

	/** Resets the array to its original configuration and return it. */
	vector<int> reset() {
		return data;
	}

	/** Returns a random shuffling of the array. */
	vector<int> shuffle() {
	vector<int> res(data);
	int pos;
	for (int i=0; i<res.size(); ++i)
	{
		pos = rand()%(res.size()-i);
		swap(res[i+pos], res[i]);
	}
	return res;
	}
};

/**
 ** Your Solution object will be instantiated and called as such:
 ** Solution* obj = new Solution(nums);
 ** vector<int> param_1 = obj->reset();
 ** vector<int> param_2 = obj->shuffle();
 **/
