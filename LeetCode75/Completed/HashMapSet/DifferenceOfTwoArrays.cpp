// Source: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::reverse()
#include <iostream>
#include <unordered_set>
#include <vector>

std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2)
{
    std::unordered_set<int> nums1Distinct(nums1.begin(), nums1.end());
    std::unordered_set<int> nums2Distinct(nums2.begin(), nums2.end());
    std::vector<std::vector<int>> answer(2);

    for (int value : nums1Distinct)
    {
        if (nums2Distinct.count(value) == 0)
        {
            answer[0].push_back(value);
        }
    }

    for (int value : nums2Distinct)
    {
        if (nums1Distinct.count(value) == 0)
        {
            answer[1].push_back(value);
        }
    }

    return answer;
}

int main()
{
    std::vector<int> nums01 = { 1, 2, 3 };
    std::vector<int> nums02 = { 2, 4, 6 };
    std::vector<int> nums11 = { 1, 2, 3, 3 };
    std::vector<int> nums12 = { 1, 1, 2, 2 };

    std::cout << "[";

    // Expected output: [[1,3],[4,6]]
    for(auto vectorElement : findDifference(nums01, nums02))
    {
        bool first = true;
        std::cout << "[";
        std::reverse(vectorElement.begin(), vectorElement.end());
        for(auto intElement : vectorElement)
        {
            if(first)
            {
                std::cout << intElement;
                first = false;
            }
            else
            {
                std::cout << "," << intElement;
            }
        }
        std::cout << "],";
    }

    std::cout << "\b]\n[";

    // Expected output: [[3],[]]
    for(auto vectorElement : findDifference(nums11, nums12))
    {
        for(auto intElement : vectorElement)
        {
            std::cout << "[" << intElement << "],[]";
        }
    }

    std::cout << "]\n";
}