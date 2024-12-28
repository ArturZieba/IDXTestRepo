// Source: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

bool canPlaceFlowers(std::vector<int>& flowerbed, int n)
{
    int iterator = 0;
    int validPlacementPlots = 0;

    for(int plot : flowerbed)
    {
        if(plot == 0)
        {
            if (iterator == 0) // First element of the vector
            {
                if (flowerbed[iterator + 1] == 0)
                {
                    validPlacementPlots++;
                }
            }
            else if (iterator == flowerbed.size()) // Last element of the vector
            {
                if (flowerbed[iterator - 1] == 0)
                {
                    validPlacementPlots++;
                }
            }
            else // Any other element of the vector
            {
                if (flowerbed[iterator - 1] == 0 && flowerbed[iterator + 1] == 0)
                {
                    validPlacementPlots++;
                }
            }

            iterator++;
        }
        else if (plot == 1)
        {
            iterator++;
        }
        else
        {
            std::cout << "Vector should only contain 0 and 1 values";
        }
    }

     if (validPlacementPlots >= n)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void printBool (bool bInput)
{
    if (bInput == 1) {
        std::cout << "true\n";
    }
    else 
    {
        std::cout << "false\n";
    }
}

int main()
{
    std::vector<int> flowerbed0 = { 1, 0, 0, 0, 1 };
    int n0 = 1;
    std::vector<int> flowerbed1 = { 1, 0, 0, 0, 1 };
    int n1 = 2;

    printBool(canPlaceFlowers(flowerbed0, n0)); // Expected output: true
    printBool(canPlaceFlowers(flowerbed1, n1)); // Expected output: false
}