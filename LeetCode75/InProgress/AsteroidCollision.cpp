// Source: https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

// Function used to print contents of int vector containers enclosed in [] (for example [1, 2, 3])
void printVectorInt (std::vector<int> vInput)
{
    std::cout << '[';

    for (int i = 0; i < vInput.size(); i++)
    {
        std::cout << vInput[i];
        if (i != vInput.size() - 1)
        {
            std::cout << ',';
        }
    }

    std::cout << "]\n";
}

std::vector<int> asteroidCollision(std::vector<int>& asteroids)
{
    std::vector<int> indicesToErase = {}; // Indices marked for remove (destroyed asteroids)

    for (int i = 0; i < (asteroids.size() - 1); i++)
    {
        if (asteroids[i] > 0) // Asteroid is flying right
        {
            if (asteroids[i] > asteroids [i + 1] && asteroids [i + 1] < 0) // If asteroid is bigger than the one on the right, and the one on the right is flying left destroy it
            {
                // Add indices to indicesToErase
            } 
            else if (asteroids[i] == asteroids[i + 1]) // If asteroid is the same size as the one on the right, and the one on the right is flying left destroy both
            {
                // Add indices to indicesToErase
            }
        } 
    }
    
    /*
    for ()
    {
        asteroids.erase(asteroids.begin() + (i - 1));
        asteroids.erase(asteroids.begin() + i, asteroids.begin() + (i + 1));
    }
    */

    return asteroids;
} 

int main()
{
    std::vector<int> asteroids0 = { 5, 10, -5 };
    std::vector<int> asteroids1 = { 8, -8 };
    std::vector<int> asteroids2 = { 10, 2, -5 };

    printVectorInt(asteroidCollision(asteroids0)); // Expected output: [5,10]
    printVectorInt(asteroidCollision(asteroids1)); // Expected output: []
    printVectorInt(asteroidCollision(asteroids2)); // Expected output: [10]
}