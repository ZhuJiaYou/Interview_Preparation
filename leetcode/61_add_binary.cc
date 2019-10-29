class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int ap=a.size()-1, bp=b.size()-1;
        int ad, bd, c=0;
        while (ap>=0 || bp>=0 || c==1)
        {
            ad = bd = 0;
            if (ap >= 0)
                ad = a[ap--] == '1';
            if (bp >= 0)
                bd = b[bp--] == '1';
            res = static_cast<char>(ad^bd^c+'0') + res;
            c = ad+bd+c >= 2;
        }
        return res;
    }
};
