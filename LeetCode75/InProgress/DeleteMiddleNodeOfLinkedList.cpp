// Source: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <tuple>
#include <vector>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteMiddle(ListNode* head)
{
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

std::tuple <ListNode*, ListNode*> initializeLinkedList(std::vector<int> values, ListNode* head, ListNode* current)
{
    for (int value : values)
    {
        if (!head)
        {
            head = new ListNode(value);
            current = head;
        } 
        else
        {
            current -> next = new ListNode(value);
            current = current -> next;
        } 
    }

    return {head, current};
}

int main()
{   
    std::vector<int> head0Values = {1, 3, 4, 7, 1, 2, 6}; // head0 = [1,3,4,7,1,2,6]
    ListNode* head0 = nullptr;
    ListNode* current0 = nullptr;

/*
head0 = [1,3,4,7,1,2,6]
// Expected output: [1,3,4,1,2,6]


head1 = [1,2,3,4]
// Expected output: [1,2,4]

head2 = [2,1]
// Expected output: [2]
*/
}