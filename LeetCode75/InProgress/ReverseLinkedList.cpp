// Source: https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <tuple>
#include <vector>

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
    std::vector<int> head0Values = {1, 2, 3, 4, 5}; // head = [1,2,3,4,5]
    ListNode* head0 = nullptr;
    ListNode* current0 = nullptr;

    initializeLinkedList(head0Values, head0, current0);
    reverseList(head0);

    std::cout << "[";

    while (current0 != nullptr)
    {
        std::cout << current0 -> val;

        if (current0 -> next != nullptr)
        {
            std::cout << ",";
        }
        current0 = current0 -> next;
    }
    
    std::cout << "]";
// Expected Output: [5,4,3,2,1]

//ListNode* head1(); // head = [1,2]
// Expected Output: [2,1]

//ListNode* head2(); // head = []
// Expected Output: []

}