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

void printLinkedList(ListNode* current)
{
    std::cout << "[";

    while (current != nullptr)
    {
        std::cout << current -> val;

        if (current -> next != nullptr)
        {
            std::cout << ",";
        }
        current = current -> next;
    }
    
    std::cout << "]\n";
}

int main()
{
    std::vector<int> head0Values = {1, 2, 3, 4, 5}; // head = [1,2,3,4,5]
    ListNode* head0 = nullptr;
    ListNode* current0 = nullptr;

    std::tuple initializedLinkedList0 = initializeLinkedList(head0Values, head0, current0);
    head0 = std::get<0>(initializedLinkedList0);
    current0 = std::get<1>(initializedLinkedList0);
    reverseList(head0);
    printLinkedList(current0); // Expected Output: [5,4,3,2,1]

    std::vector<int> head1Values = {1, 2}; // head = [1,2]
    ListNode* head1 = nullptr;
    ListNode* current1 = nullptr;

    std::tuple initializedLinkedList1 = initializeLinkedList(head1Values, head1, current1);
    head1 = std::get<0>(initializedLinkedList1);
    current1 = std::get<1>(initializedLinkedList1);
    reverseList(head1);
    printLinkedList(current1); // Expected Output: [2,1]

    std::vector<int> head2Values = {}; // head = []
    ListNode* head2 = nullptr;
    ListNode* current2 = nullptr;

    std::tuple initializedLinkedList2 = initializeLinkedList(head2Values, head2, current2);
    head0 = std::get<0>(initializedLinkedList2);
    current0 = std::get<1>(initializedLinkedList2);
    reverseList(head2);
    printLinkedList(current2); // Expected Output: []
}