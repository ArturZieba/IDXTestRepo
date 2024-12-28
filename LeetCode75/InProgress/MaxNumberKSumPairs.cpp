// Source: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int maxOperations(std::vector<int>& nums, int k)
{
    return 2;
}

int main()
{
    std::vector<int> nums0 = { 1, 2, 3, 4 };
    int k0 = 5;
    std::vector<int> nums1 = { 3, 1, 3, 4, 3 };
    int k1 = 6;

    std::cout << maxOperations(nums0, k0) << '\n'; // Expected output: 2
    std::cout << maxOperations(nums1, k1) << '\n'; // Expected output: 1
}