#include <ctime> //For std::time for use as a seed
#include <iostream>
#include <random> //For Mersenne Twister Engine

// Generate and print a specified number of random integers
void randomIntegerInRange(int rangeMin, int rangeMax, int integersToGenerate)
{
    std::mt19937_64 randomNumberGenerator(std::time(nullptr));
    std::uniform_real_distribution<> distribution(rangeMin, rangeMax);

    std::cout << integersToGenerate << " random integers in range " << rangeMin << " to " << rangeMax << ": \n\n";

    for (int i; i < integersToGenerate; i++)
    {
        std::cout << round(distribution(randomNumberGenerator)) << '\n';
    }

    std::cout << '\n';
}

// TODO: Generate and print a specified number of random integers without repeating them
void randomUniqueIntegerInRange(int rangeMin, int rangeMax, int integersToGenerate)
{
    std::cout << "Test: " << rangeMin << " " << rangeMax << " " << integersToGenerate << '\n';
}

int main()
{
    int rangeMin = 5; //REMOVE INITIALIZATION AFTER FINISHING FUNCTIONS
    int rangeMax = 10; //REMOVE INITIALIZATION AFTER FINISHING FUNCTIONS
    int integersToGenerate = 5; //REMOVE INITIALIZATION AFTER FINISHING FUNCTIONS

    //REMOVE COMMENT AFTER FINISHING FUNCTIONS
    /*
    std::cout << "Choose values for the random integer generation functions (please type in only integer values, max value higher than min, and non-negative number of numbers to generate)\n"; //TODO: Potentially add safeguards against unacceptable inputs?
    std::cout << "Type in lower range: ";
    std::cin >> rangeMin;
    std::cout << "\nType in higher range: ";
    std::cin >> rangeMax;
    std::cout << "\nType in how many numbers to generate: ";
    std::cin >> integersToGenerate;
    */

    // TODO: Add accepting input from the Terminal
    randomIntegerInRange(rangeMin, rangeMax, integersToGenerate);
    randomUniqueIntegerInRange(rangeMin, rangeMax, integersToGenerate);
}