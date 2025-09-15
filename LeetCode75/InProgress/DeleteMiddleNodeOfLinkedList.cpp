// Source: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <tuple>
#include <vector>
/*
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
    if (head->next == nullptr)
    {
        return nullptr;
    }

    int count = 0;
    ListNode *n1 = head, *n2 = head;

    while (n1 != nullptr)
    {
        count++;
        n1 = n1->next;
    }

    int middleIndex = count / 2;

    for (int i = 0; i < middleIndex - 1; ++i)
    {
        n2 = n2->next;
    }

    n2->next = n2->next->next;

    return head;
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

// Print linked list contents
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
*/
int main()
{ 
    std::cout << "Test";

    /*
    // Initialize linked list and print it
    std::vector<int> head0Values = {1, 3, 4, 7, 1, 2, 6}; // head0 = [1,3,4,7,1,2,6]
    ListNode* head0 = nullptr;
    ListNode* current0 = nullptr;

    //std::tuple initializedLinkedList0 = initializeLinkedList(head0Values, head0, current0);
    //head0 = std::get<0>(initializedLinkedList0);
    //current0 = std::get<1>(initializedLinkedList0);
    deleteMiddle(head0);
    printLinkedList(head0); // Expected Output: [1,3,4,1,2,6]
    */
/*
head0 = [1,3,4,7,1,2,6]
// Expected output: [1,3,4,1,2,6]


head1 = [1,2,3,4]
// Expected output: [1,2,4]

head2 = [2,1]
// Expected output: [2]
*/
}