class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<long>> ways(m+1, vector<long>(n+1, 0));
        ways[0][1] = 1;
        for (int i=1; i<=m; ++i)
            for (int j=1; j<=n; ++j)
                if (obstacleGrid[i-1][j-1] == 0)
                    ways[i][j] = ways[i][j-1] + ways[i-1][j];
        return ways[m][n];
    }
};
