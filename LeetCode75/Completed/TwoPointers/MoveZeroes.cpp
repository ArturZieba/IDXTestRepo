// Source: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::rotate
#include <iostream>
#include <vector>

void moveZeroes(std::vector<int>& nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        if(nums[i] == 0)
        {
            std::rotate(nums.begin() + i, nums.begin() + i + 1, nums.end());
        }
    }


    // Print out the vector matching the expected output
    std::cout << '[';

    for (int i = 0; i < nums.size(); i++)
    {
        if (i == nums.size() - 1)
        {
            std::cout << nums[i];
        }
        else 
        {
            std::cout << nums[i] << ',';
        }
    }

    std::cout << "]\n";
}

int main()
{
    std::vector<int> nums0 = { 0, 1, 0, 3, 12 }; // Expected output: [1,3,12,0,0]
    std::vector<int> nums1 = { 0 }; // Expected output: [0]

    moveZeroes(nums0);
    moveZeroes(nums1);
}