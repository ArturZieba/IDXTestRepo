// Source: https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int largestAltitude(std::vector<int>& gain)
{
    int currentAltitude = 0;
    int highestAltitude = currentAltitude;

    for(int i = 0; i < gain.size(); i++)
    {
        currentAltitude += gain[i];

        if(currentAltitude > highestAltitude)
        {
            highestAltitude = currentAltitude;  
        }
    }

    return highestAltitude;
}

int main()
{
    std::vector gain0 = { -5, 1, 5, 0, -7 };
    std::vector gain1 = { -4, -3, -2, -1, 4, 3, 2 };

    std::cout << largestAltitude(gain0) << '\n'; // Expected output: 1
    std::cout << largestAltitude(gain1) << '\n'; // Expected output: 0
}