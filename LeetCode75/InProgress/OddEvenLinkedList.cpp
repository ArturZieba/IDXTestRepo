// Source: https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* oddEvenList(ListNode* head)
{
    return head;
}

int main()
{
/*
head0 = [1,2,3,4,5]
// Expected Output: [1,3,5,2,4]

head1 = [2,1,3,5,6,4,7]
// Expected Output: [2,3,6,7,1,5,4]
*/
}