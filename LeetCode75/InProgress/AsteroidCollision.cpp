// Source: https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

std::vector<int> asteroidCollision(std::vector<int>& asteroids)
{
    for (int i = 0; i < asteroids.size(); i++)
    {
        if (asteroids[i] < 0 && asteroids[i] != 0)
        {
            if (asteroids[i - 1] > 0)
            {
                if (asteroids[i] > asteroids [i - 1])
                {
                    asteroids.erase(asteroids.begin() + (i - 1));
                } 
                else if (asteroids[i] == asteroids[i - 1])
                {
                    asteroids.erase(asteroids.begin() + (i - 1), asteroids.begin() + i);
                }
                else
                {
                    asteroids.erase(asteroids.begin() + i);
                }
            }
        }
    }
    
    return asteroids;
} 


int main()
{
    std::vector<int> asteroids0 = { 5, 10, -5 };
    std::vector<int> asteroids1 = { 8, -8 };
    std::vector<int> asteroids2 = { 10, 2, -5 };

    for (auto element : asteroidCollision(asteroids0)) // Expected output: [5,10]
    {
        std::cout << element << ' ';
    }

    std::cout << '\n';

    for (auto element : asteroidCollision(asteroids1)) // Expected output: []
    {
        std::cout << element << ' ';
    }

    std::cout << '\n';

    for (auto element : asteroidCollision(asteroids2)) // Expected output: [10]
    {
        std::cout << element << ' ';
    }
}