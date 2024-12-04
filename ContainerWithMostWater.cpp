// Source: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
#include <algorithm> // For max_element()
#include <iostream>
#include <vector>

int maxArea(std::vector<int>& height)
{
    if (height.size() <= 1) // Container cannot be made with a zero or one element vector
    {
        return 0;
    }

    int highestHeight = *max_element(height.begin(), height.end());

    // Water area = value of the lowest element * (index of the element closest to vector.end() - index of the element closest to vector.begin())
    // Determine these "walls"

    return highestHeight;
}

int main()
{
    std::vector<int> height0 = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
    std::vector<int> height1 = { 1, 1 };

    std::cout << maxArea(height0); // Expected output: 49
    std::cout << maxArea(height1); // Expected output: 1
}