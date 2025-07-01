// Source: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::remove
#include <iostream>
#include <string>
#include <vector>

std::string removeStars(std::string s)
{
    std::vector<int> charToRemove = {};

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '*')
        {
            //charToRemove.push_back(i);
            s.erase(i - 1, 2);
        }
    }

    /*
    for (auto element : charToRemove)
    {
        std::cout << element;
    }
    */

    for (int i = 0; i < charToRemove.size(); i++)
    {
        //s.erase(i, 2);
    }

    // Remove all * from the string
    //s.erase(std::remove(s.begin(), s.end(), '*'), s.end());
    return s;
}

int main()
{
    std::string s0 = "leet**cod*e";
    std::string s1 = "erase*****";

    std::cout << removeStars(s0) << '\n'; // Expected output: "lecoe"
    std::cout << removeStars(s1) << '\n'; // Expected output: ""
}