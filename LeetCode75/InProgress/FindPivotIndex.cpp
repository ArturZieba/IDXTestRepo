// Source: https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int pivotIndex(std::vector<int>& nums)
{
    if (false)
    {
        return 0;
        // Placeholder
    }
    else
    {
        return -1;
    }
}

int main()
{
    std::vector<int> nums0 = { 1, 7, 3, 6, 5, 6 }; // Expected output: 3
    std::vector<int> nums1 = { 1, 2, 3 }; // Expected output: -1
    std::vector<int> nums2 = { 2, 1, -1 }; // Expected output: 0

    std::cout << pivotIndex(nums0) << '\n';
    std::cout << pivotIndex(nums1) << '\n';
    std::cout << pivotIndex(nums2) << '\n';
}