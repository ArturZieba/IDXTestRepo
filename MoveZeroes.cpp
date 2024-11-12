// Source: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

void moveZeroes(std::vector<int>& nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        std::cout << nums[i];
    }
}

int main()
{
    std::vector<int> nums = { 0, 1, 0, 3, 12 }; // Expected output: [1,3,12,0,0]

    moveZeroes(nums);

    std::cout << "Test\n";
}