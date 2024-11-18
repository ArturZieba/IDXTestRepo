// Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For *std::max_element
#include <iostream>
#include <vector>

std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies)
{
    std::vector<bool> hasGreatestNumberOfCandies(candies.size());

    int iterator = 0;

    for (int kid : candies)
    {
        kid += extraCandies;
        
        if (kid >= *std::max_element(candies.begin(), candies.end())) 
        {
            hasGreatestNumberOfCandies[iterator] = true;
        }
        else
        {
            hasGreatestNumberOfCandies[iterator] = false;
        }

        iterator++;
    }

    return hasGreatestNumberOfCandies;
}

void printBoolVector(std::vector<bool> boolVector)
{
    std::cout << '['; 

    for (int i; i < boolVector.size(); i++)
    {  
        if (boolVector[i] == 0)
        {
            std::cout << "false";
        }
        else
        {
            std::cout << "true";
        }

        if (i + 1 == boolVector.size())
        {
            std::cout << ']';
        }
        else
        {
            std::cout << ',';
        }
    }

    std::cout << '\n';
}

int main()
{
    std::vector<int> candies0 = { 2, 3, 5, 1 ,3 }; // Expected output: [true,true,true,false,true]
    int extraCandies0 = 3;
    std::vector<int> candies1 = { 4, 2, 1, 1 ,2 }; // Expected output: [true,false,false,false,false]
    int extraCandies1 = 1;
    std::vector<int> candies2 = { 12, 1, 12 }; // Expected output: [true,false,true]
    int extraCandies2 = 10;

    std::vector<bool> greatestNumberOfCandies0 = kidsWithCandies(candies0, extraCandies0);
    std::vector<bool> greatestNumberOfCandies1 = kidsWithCandies(candies1, extraCandies1);
    std::vector<bool> greatestNumberOfCandies2 = kidsWithCandies(candies2, extraCandies2);

    printBoolVector(greatestNumberOfCandies0);
    printBoolVector(greatestNumberOfCandies1);
    printBoolVector(greatestNumberOfCandies2);
}