// Source: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::remove
#include <iostream>
#include <string>

std::string removeStars(std::string s)
{
    // Remove all * from the string
    s.erase(std::remove(s.begin(), s.end(), '*'), s.end());
    return s;
}

int main()
{
    std::string s0 = "leet**cod*e";
    std::string s1 = "erase*****";

    std::cout << removeStars(s0) << '\n'; // Expected output: "lecoe"
    std::cout << removeStars(s1) << '\n'; // Expected output: ""
}