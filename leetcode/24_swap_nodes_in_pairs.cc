/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        vector<ListNode *> ns;
        ListNode *p = head;
        while (p != NULL)
        {
            ns.push_back(p);
            p = p->next;
        }
        
        if (ns.size() == 0)
            return NULL;
        else if (ns.size() == 1)
            return ns[0];

        for (int i=1; i<ns.size(); i+=2)
        {
            ns[i]->next = ns[i-1];
        }
        for (int i=0; i<ns.size(); i+=2)
        {
            if (i + 3 < ns.size())
                ns[i]->next = ns[i+3];
            else if (i + 2 < ns.size())
                ns[i]->next = ns[i+2];
        }
        
        if (ns.size()%2 == 0)
            ns[ns.size()-2]->next = NULL;
        else
            ns[ns.size()-1]->next = NULL;
        
        return ns[1];
    }
};
