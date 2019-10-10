class Solution {
public:
    string countAndSay(int n) {
        string pre = "1";
        string now;
        while (n != 1)
        {
            now = "";
            int i=0;
            int count;
            while (i < pre.size())
            {
                count = 1;
                while (i<pre.size() && pre[i]==pre[i+1])
                {
                    ++i;
                    ++count;
                }
                now += to_string(count)+pre[i];
                ++i;
            }
            pre = now;
            --n;
        }
        return pre;
    }
};
