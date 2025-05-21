// Source: https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <numeric> // For std::accumulate
#include <vector>

int pivotIndex(std::vector<int>& nums)
{
    int sumLeft = 0; // Sum to the left of the index (0 at the start)
    int sumRight = std::accumulate(nums.begin(), nums.end(), 0); // Sum to the right of the index (Sum of the whole vector at the start)
        
    for (int i = 0; i < nums.size(); i++)
    {
        sumRight -= nums[i]; // Subtract current element from sum to the right of index

        if (sumLeft == sumRight)
        {
            return i;
        }

        sumLeft += nums[i]; // Add current element to the sumLeft if sumLeft and sumRight are not equal
    }

    return -1; // If there is no leftmost pivot index return -1
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