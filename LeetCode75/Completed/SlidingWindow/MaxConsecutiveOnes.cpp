// Source: https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int longestOnes(std::vector<int>& nums, int k)
{
    return 4;
}

int main()
{
    std::vector<int> nums0 = { 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 };
    int k0 = 2;
    std::vector<int> nums1 = { 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1 };
    int k1 = 3;

    std::cout << longestOnes(nums0, k0) << '\n'; // Expected output: 6
    std::cout << longestOnes(nums1, k1) << '\n'; // Expected output: 10
}