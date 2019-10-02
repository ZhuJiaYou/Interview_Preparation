#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode *oddEvenList(struct ListNode *head)
{
	if (head==NULL || head->next==NULL)
		return head;
	struct ListNode *odd = head;
	struct ListNode *even = head->next;
	struct ListNode *p1 = odd;
	struct ListNode *p2 = even;

	if (even->next != NULL)
		head = even->next;
	else
		head = NULL;

	while (head != NULL)
	{
		p1->next = head;
		p1 = p1->next;
		head = head->next;
		if (head != NULL)
		{
			p2->next = head;
			p2 = p2->next;
			head = head->next;
		}
	}
	p1->next = even;
	p2->next = NULL;
	return odd;
}

int main()
{
	struct ListNode n5 = {5, NULL};
	struct ListNode n4 = {4, &n5};
	struct ListNode n3 = {3, &n4};
	struct ListNode n2 = {2, &n3};
	struct ListNode n1 = {1, &n2};
	struct ListNode *h = oddEvenList(&n1);
	// exit(1);
	while (h != NULL)
	{
		printf("%d ", h->val);
		h = h->next;
	}
	printf("\n");
}
