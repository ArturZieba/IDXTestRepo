// Source: https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

std::vector<int> productExceptSelf(std::vector<int>& nums)
{
    
    std::vector<int> sums;

    for(int i = 0; i < nums.size(); i++)
    {
        int sum = 0;

        for(int j = 0; i < nums.size(); j++)
        {
            if(j != i)
            {
                sum += nums[i];
            }
        }
        
        sums.push_back(sum);
    }

    return sums;
}

int main()
{
    std::vector<int> nums0 = { 1, 2, 3, 4 }; // Expected output: [24,12,8,6]
    std::vector<int> nums1 = { -1, -1, 0, -3, 3 }; // Expected output: [0,0,9,0,0]

    for(int i; i < productExceptSelf(nums0).size(); i++)
    {
        std::cout << productExceptSelf(nums0)[i];
    }

    std::cout << '\n';
    
    for(int i; i < productExceptSelf(nums1).size(); i++)
    {
        std::cout << productExceptSelf(nums1)[i];
    }

    std::cout << '\n';
}