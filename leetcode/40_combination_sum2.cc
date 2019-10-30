class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());
        vector<int> now;
        dfs(res, 0, target, now, candidates);
        
        return res;
    }
    
    void dfs(vector<vector<int>> &res, const int pos, const int target, vector<int> &now, const vector<int> &candidates)
    {
        if (target == 0)
        {
            res.push_back(now);
            return;
        }
        else
        {
            for (int i=pos; i<candidates.size(); ++i)
            {
                if (candidates[i] > target)
                    return;
                if (i&&candidates[i]==candidates[i-1]&&i>pos)
                    continue;
                now.push_back(candidates[i]);
                dfs(res, i+1, target-candidates[i], now, candidates);
                now.pop_back();
            }
        }
    }
};
