// Source: https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int main()
{
    std::cout << "Check compiler 12345\n";
/*
Input: head0 = [1,2,3,4,5]
// Expected Output: [5,4,3,2,1]

Input: head1 = [1,2]
// Expected Output: [2,1]

Input: head2 = []
// Expected Output: []
*/
}