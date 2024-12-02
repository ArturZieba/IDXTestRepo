// Source: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
#include <iostream>
#include <vector>

int maxArea(std::vector<int>& height)
{
    return 1;
}

int main()
{
    std::vector<int> height0 = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
    std::vector<int> height1 = { 1, 1 };

    std::cout << maxArea(height0); // Expected output: 49
    std::cout << maxArea(height1); // Expected output: 1
}