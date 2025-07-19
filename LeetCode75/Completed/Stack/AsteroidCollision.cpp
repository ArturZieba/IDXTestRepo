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
    std::vector<int> wholeAsteroids = {}; // Array for storing asteroids that are not destroyed

    for (int i = 0; i < asteroids.size(); i++)
    {
        if (asteroids[i] > 0) // Asteroid flying right (positive value)
        {
            wholeAsteroids.push_back(asteroids[i]); // Add a whole asteroid to the vector
        }
        else // Asteroid flying left (there are no 0 size asteroids due to asteroids[i] != 0 constraint)
        {
            // While there are whole asteroids AND the last asteroid is flying right AND last asteroid is smaller than the current asteroid
            while (!wholeAsteroids.empty() && wholeAsteroids.back() > 0 && wholeAsteroids.back() < abs(asteroids[i]))
            {
                wholeAsteroids.pop_back(); // Destroy the last asteroid
            }
            // If there are whole asteroids AND the last asteroid is the same size as the current asteroid
            if (!wholeAsteroids.empty() && abs(wholeAsteroids.back()) == abs(asteroids[i])) 
            {
                wholeAsteroids.pop_back(); // Destroy the last asteroid and implicitly do not add the current asteroid to the vector
            } 
            // If there are no whole asteroids or the last asteroid is flying left
            else if (wholeAsteroids.empty() || wholeAsteroids.back() < 0) 
            {
                // Add the current asteroid to the vector
                wholeAsteroids.push_back(asteroids[i]); 
            }
        }
    }

    return wholeAsteroids;
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