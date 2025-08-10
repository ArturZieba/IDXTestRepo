// A header file for storing custom functions which were used in two or more different excercises (.cpp files)
// Note that for readability sake this should not be included for most of the .cpp files in this repo, as they usually do not exceed ~60 lines of code
// Include for bigger source files where most of listed functions would be used
#include <iostream>
#include <tuple>
#include <vector>

// Function used to print true or false to the terminal depending on the passed boolean's value
void printBool (bool bInput)
{
    if (bInput == 1) {
        std::cout << "true\n";
    }
    else 
    {
        std::cout << "false\n";
    }
}

// Function used to print contents of int vector containers enclosed in [] (for example [1, 2, 3])
void printVectorInt (std::vector<int> vInput)
{
    std::cout << '[';

    for (int i = 0; i < vInput.size(); i++)
    {
        std::cout << vInput[i];
        if (i != vInput.size() - 1)
        {
            std::cout << ',';
        }
    }

    std::cout << "]\n";
}

// Linked list functions
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* reverseList(ListNode* head)
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

/*
// Initialize linked list and print them
    std::vector<int> head0Values = {1, 2, 3, 4, 5}; // head = [1,2,3,4,5]
    ListNode* head0 = nullptr;
    ListNode* current0 = nullptr;

    std::tuple initializedLinkedList0 = initializeLinkedList(head0Values, head0, current0);
    head0 = std::get<0>(initializedLinkedList0);
    current0 = std::get<1>(initializedLinkedList0);
    reverseList(head0);
    printLinkedList(current0); // Expected Output: [5,4,3,2,1]
*/