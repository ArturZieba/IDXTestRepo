// Source: https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int equalPairs(std::vector<std::vector<int>>& grid)
{
    for (auto vectorElement : grid)
    {
        for (auto element : vectorElement)
        {
            std::cout << element << " ";
        }
    }
    return 321;
}

int main()
{
    std::vector<int> gridRow00 = { 3, 2, 1 };
    std::vector<int> gridRow01 = { 1, 7, 6 };
    std::vector<int> gridRow02 = { 2, 7, 7 };
    std::vector<std::vector<int>> grid0 = { gridRow00, gridRow01, gridRow02 };

    std::vector<int> gridRow10 = { 3, 1, 2, 2 };
    std::vector<int> gridRow11 = { 1, 4, 4, 5 };
    std::vector<int> gridRow12 = { 2, 4, 2, 2 };
    std::vector<int> gridRow13 = { 2, 4, 2, 2 };
    std::vector<std::vector<int>> grid1 = { gridRow10, gridRow11, gridRow12, gridRow13 };

    std::cout << equalPairs(grid0) << '\n'; // Expected output: 1
    std::cout << equalPairs(grid1) << '\n'; // Expected output: 3
    std::cout << "Test1";
}