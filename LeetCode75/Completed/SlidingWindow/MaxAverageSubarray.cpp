// Source: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm>
#include <iomanip> // For std::setprecsion
#include <ios> // For std::fixed
#include <iostream>
#include <vector>

double findMaxAverage(std::vector<int>& nums, int k)
{
    int iStart = 0; // Start of the iterator for separate sums
    int jStart = 0; // Start of the iterator for elements inside individual sums
    int sum = 0; // Sum of a subarray
    std::vector<int> sumVector; // Vector containing subarray sums

    for (int i = iStart; i + k <= nums.size(); i++) // Make sure that element sum does not go outside of the vector
    {
        for (int j = jStart; j < jStart + k; j++)
        {
            sum += nums[j]; // Add to a total sum
            sumVector.push_back(sum); // Add the sum to a vector
        }

        sum = 0; // Reset sum before next adding up

        iStart++;
        jStart++;
    }

    int highestSum = *std::max_element(sumVector.begin(), sumVector.end()); // Check vector for the highest element

    return (double)highestSum / (double)k; // Average, both variables are cast as double (from int) to get a result with decimal value
}

int main()
{
    std::vector<int> nums0 = { 1, 12, -5, -6, 50, 3 };
    int k0 = 4;
    std::vector<int> nums1 = { 5 };
    int k1 = 1;

    std::cout << std::fixed << std::setprecision(5); // std::fixed makes output stream use a fixed-poind notation for floats, std::setprecision sets the decimal precision to the passed value
    std::cout << findMaxAverage(nums0, k0) << '\n'; // Expected output: 12.75000
    std::cout << findMaxAverage(nums1, k1) << '\n'; // Expected output: 5.00000
}