// Source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

int maxVowels(std::string s, int k)
{
    return 3;
}

int main()
{
    std::string s0 = "abciiidef";
    int k0 = 3;
    std::string s1 = "aeiou";
    int k1 = 2;
    std::string s2 = "leetcode";
    int k2 = 3;

    std::cout << maxVowels(s0, k0) << '\n'; // Expected output: 3
    std::cout << maxVowels(s1, k1) << '\n'; // Expected output: 2
    std::cout << maxVowels(s2, k2) << '\n'; // Expected output: 2
}