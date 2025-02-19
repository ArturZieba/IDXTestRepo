// Source: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2)
{
    return { nums1, nums2 };
}

int main()
{
    std::vector<int> nums01 = { 1, 2, 3 };
    std::vector<int> nums02 = { 2, 4, 6 };
    std::vector<int> nums11 = { 1, 2, 3, 3 };
    std::vector<int> nums12 = { 1, 1, 2, 2 };

    // Expected output: [[1,3],[4,6]]
    for(auto element : findDifference(nums01, nums02))
    {
        for(int i; i < element.size(); i++)
        {
            std::cout << element[i];
        }
    }

    std::cout << '\n';

    // Expected output: [[3],[]]
    for(auto element : findDifference(nums11, nums12))
    {
        for(int i; i < element.size(); i++)
        {
            std::cout << element[i];
        }
    }
}