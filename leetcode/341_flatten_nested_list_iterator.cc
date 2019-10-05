/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        size = nestedList.size();
        p = &nestedList;
    }

    int next() {
        return nxt;
    }

    bool hasNext() {
        if (pi!=nullptr && pi->hasNext())
        {
            nxt = pi->next();
            return true;
        }
        
        if (now == size)
            return false;
        
        if ((*p)[now].isInteger())
        {
            nxt = (*p)[now].getInteger();
            ++now;
            return true;
        }
        else
        {
            pi = new NestedIterator((*p)[now].getList());
            ++now;
            if (pi->hasNext())
            {
                nxt = pi->next();
                return true;
            }
            else
            {
                return hasNext();
            }
        }
    }
private:
    unsigned int now = 0;
    unsigned int size = 0;
    vector<NestedInteger> *p = nullptr;
    NestedIterator *pi = nullptr;
    int nxt = 0;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
