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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head==NULL || k==1)
            return head;
        ListNode *preh = new ListNode(-1);
        preh->next = head;
        ListNode *pre=preh, *cur=preh, *nxt;
        int num = 0;
        while (cur = cur->next)
            ++num;
        
        int i;
        while (num >= k)
        {
            cur = pre->next;
            nxt = cur->next;
            for (i=1; i<k; ++i)
            {
                cur->next = nxt->next;
                nxt->next = pre->next;
                pre->next = nxt;
                nxt = cur->next;
            }
            pre = cur;
            num -= k;
        }
        return preh->next;        
    }
};
