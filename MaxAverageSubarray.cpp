// Source: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm>
#include <iostream>
#include <vector>

double findMaxAverage(std::vector<int>& nums, int k)
{
    int sum = 0;
    std::vector<int> sumVector;

    for (int i = 0; i + k <= nums.size(); i++)
    {
        sum += nums[i];
        sumVector.push_back(sum);
    }

    int highestSum = *std::max_element(sumVector.begin(), sumVector.end());

    return highestSum / k; // Average
}

int main()
{
    std::vector<int> nums0 = { 1, 12, -5, -6, 50, 3 };
    int k0 = 4;
    std::vector<int> nums1 = { 5 };
    int k1 = 1;

    std::cout << findMaxAverage(nums0, k0) << '\n'; // Expected output: 12.75000
    std::cout << findMaxAverage(nums1, k1) << '\n'; // Expected output: 5.00000
}