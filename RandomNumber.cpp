#include <ctime> //For std::time for use as a seed
#include <iostream>
#include <random> //For Mersenne Twister Engine

// Generate and print a specified number of random integers
void randomIntegerInRange(int rangeMin, int rangeMax, int integersToGenerate)
{
    std::mt19937_64 randomNumberGenerator(std::time(nullptr));
    std::uniform_real_distribution<> distribution(rangeMin, rangeMax);

    for (int i; i < integersToGenerate; i++)
    {
        std::cout << round(distribution(randomNumberGenerator)) << '\n';
    }
}

// TODO: Generate and print a specified number of random integers without repeating them
void randomUniqueIntegerInRange(int rangeMin, int rangeMax, int integersToGenerate)
{
    std::cout << "Test: " << rangeMin << " " << rangeMax << " " << integersToGenerate << '\n';
}

int main()
{
    // TODO: Add accepting input from the Terminal
    randomIntegerInRange(0, 20, 5);
    randomUniqueIntegerInRange(14, 25, 36);
}