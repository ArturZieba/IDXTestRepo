// Source: https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* reverseList(ListNode* head) {
    ListNode* current = head;
    ListNode* previous = nullptr; // nullptr is before the head

    while(current)
    {
        ListNode* nextCopy = current->next; // Link after the current link

        current->next = previous;
        previous = current;
        current = nextCopy;
    }

    return previous;
}

int main()
{
//ListNode* head0();
// Expected Output: [5,4,3,2,1]

//ListNode* head1();
// Expected Output: [2,1]

//ListNode* head2();
// Expected Output: []

}