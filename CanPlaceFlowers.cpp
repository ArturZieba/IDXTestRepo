// Source: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

bool canPlaceFlowers(std::vector<int>& flowerbed, int n)
{
    int iterator = 0;

    for(int flower : flowerbed)
    {
        if(flower == 0)
        {
            if (iterator == 0)
            {
                if (flowerbed[iterator + 1] == 0)
                {
                    n -= 1;
                    std::cout << "Ping element: " << iterator << '\n';
                }
            }
            else if (iterator == flowerbed.size())
            {
                if (flowerbed[iterator - 1] == 0)
                {
                    n -= 1;
                    std::cout << "Ping element: " << iterator << '\n';
                }
            }
            else 
            {
                if (flowerbed[iterator - 1] == 0 && flowerbed[iterator + 1] == 0)
                {
                    n -= 1;
                    std::cout << "Ping element: " << iterator << '\n';
                }
            }

            iterator += 1;
        }
        else if (flower == 1)
        {
            iterator += 1;
        }
    }

     if (n > 0)
    {
        std::cout << "n: " << n << '\n';
        return true;
    }
    else
    {
        std::cout << "n: " << n << '\n';
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

    printBool(canPlaceFlowers(flowerbed0, n0)); //Expected output: true
    printBool(canPlaceFlowers(flowerbed1, n1)); //Expected output: false
}