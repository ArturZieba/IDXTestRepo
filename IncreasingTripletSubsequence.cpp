// Source: https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

bool increasingTriplet(std::vector<int>& nums)
{
    return 0;
}

int main()
{
    std::vector<int> nums0 = { 1, 2, 3, 4, 5 };
    std::vector<int> nums1 = { 5, 4, 3, 2, 1 };
    std::vector<int> nums2 = { 2, 1, 5, 0, 4, 6 };

    std::cout << increasingTriplet(nums0);
    std::cout << increasingTriplet(nums1);
    std::cout << increasingTriplet(nums2);
}