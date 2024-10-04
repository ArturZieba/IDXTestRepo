//Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> //For *std::max_element
#include <iostream>
#include <vector>

std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies)
{
    std::vector<bool> hasGreatestNumberOfCandies(candies.size());

    for (int kid : candies)
    {
        kid + extraCandies;
        /*
        if (kid >= *std::max_element(candies.begin(), candies.end())) 
        {
            hasGreatestNumberOfCandies[kid] = true;
        }
        else
        {
            hasGreatestNumberOfCandies[kid] = false;
        }
        */
    }

    return hasGreatestNumberOfCandies;
}

int main()
{
    std::vector<int> candies0 = { 2, 3, 5, 1 ,3 };
    int extraCandies0 = 3;
    std::vector<int> candies1 = { 4, 2, 1, 1 ,2 };
    int extraCandies1 = 1;
    std::vector<int> candies2 = { 12, 1, 12 };
    int extraCandies2 = 10;

    //std::vector<bool> greatestNumberOfCandies0 = kidsWithCandies(candies0, extraCandies0);

    for (bool mostCandies : kidsWithCandies(candies0, extraCandies0))
    {
        std::cout << mostCandies << '\n';
    }
}