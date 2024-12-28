// Source: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string gcdOfStrings(std::string str1, std::string str2)
{
    std::string strDenominator;

    for (int i; i < str1.size() && str2.size(); i++)
    {
        if (str1[i] == str2[i])
        {
            strDenominator += str1[i];
        }
    }

    return strDenominator;    
}

int main()
{
    std::cout << gcdOfStrings("ABCABC", "ABC") << '\n';  // Expected output: "ABC"
    std::cout << gcdOfStrings("ABABAB", "AB") << '\n';   // Expected output: "AB"
    std::cout << gcdOfStrings("LEET", "CODE") << '\n';   // Expected output: ""
    std::cout << gcdOfStrings("TEST","TESTTES") << '\n'; // Expected output: "TEST"
}