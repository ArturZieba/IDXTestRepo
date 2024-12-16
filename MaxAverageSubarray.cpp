// Source: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm>
#include <iostream>
#include <vector>

double findMaxAverage(std::vector<int>& nums, int k)
{
    int iStart = 0; // Iterator for separate sums
    int jStart = 0; // Iterator for elements inside individual sums
    int sum = 0;
    std::vector<int> sumVector;

    for (int i = iStart; i + k <= nums.size(); i++) // Make sure that element sum does not go outside of the vector
    {
        for (int j = jStart; j < i + k; j++)
        {
            sum += nums[j]; // Add to a total sum
            std::cout << sum << " element: " << j << ' ';
            sumVector.push_back(sum); // Add the sum to a vector
            jStart++;
        }

        sum = 0; // Reset sum before next adding up

        iStart++;
    }

    int highestSum = *std::max_element(sumVector.begin(), sumVector.end()); // Check vector for the highest element

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