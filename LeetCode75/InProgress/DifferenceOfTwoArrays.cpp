// Source: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2)
{
    std::vector<std::vector<int>> answer = {};
    std::vector<int> nums1Distinct = {};
    std::vector<int> nums2Distinct = {};

    for (int i = 0; i < nums1.size(); i++)
    {
        for (int j = 0; j < nums2.size(); j++)
        {
            if (nums1[i] != nums2[j])
            {
                nums1Distinct.push_back(nums1[i]);
                nums2Distinct.push_back(nums2[i]);
            }
        }
    }

    answer.push_back(nums1Distinct);
    answer.push_back(nums2Distinct);

    return answer;
}

int main()
{
    std::vector<int> nums01 = { 1, 2, 3 };
    std::vector<int> nums02 = { 2, 4, 6 };
    std::vector<int> nums11 = { 1, 2, 3, 3 };
    std::vector<int> nums12 = { 1, 1, 2, 2 };

    // Expected output: [[1,3],[4,6]]
    for(auto vectorElement : findDifference(nums01, nums02))
    {
        for(auto intElement : vectorElement)
        {
                std::cout << intElement;
        }
    }

    std::cout << '\n';

    // Expected output: [[3],[]]
    for(auto vectorElement : findDifference(nums11, nums12))
    {
        for(auto intElement : vectorElement)
        {
                std::cout << intElement;
        }
    }
}