class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int rows=board.size(), cols=rows?board[0].size():0;
        int count;
        for (int i=0; i<rows; ++i)
        {
            for (int j=0; j<cols; ++j)
            {
                count = 0;
                for (int m=max(0, i-1); m<min(i+2, rows); ++m)
                {
                    for (int n=max(0, j-1); n<min(j+2, cols); ++n)
                    {
                        count += board[m][n] & 1;
                    }
                }
                if (count==3 || count-board[i][j]==3)
                {
                    board[i][j] |= 2;
                }
            }
        }
        for (auto &r : board)
            for (auto &c : r)
                c >>= 1;
    }
};
