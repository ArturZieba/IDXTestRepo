// Source: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int longestSubarray(std::vector<int>& nums)
{
    return 123;
}

int main()
{  
    std::vector nums0 = { 1, 1, 0, 1 };
    std::vector nums1 = { 0, 1, 1, 1, 0, 1, 1, 0, 1 };
    std::vector nums2 = { 1, 1, 1 };

    std::cout << longestSubarray(nums0) << '\n'; // Expected output: 3
    std::cout << longestSubarray(nums1) << '\n'; // Expected output: 5
    std::cout << longestSubarray(nums2) << '\n'; // Expected output: 2
}