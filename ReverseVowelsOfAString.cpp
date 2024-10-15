//Source: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::find and std::search
#include <cctype> // For std::tolower
#include <iostream>
#include <string>
#include <vector>

std::string reverseVowels (std::string s)
{
    // Vowels: 'a', 'e', 'i', 'o', 'u'
    std::vector<char> vowels = { 'a', 'e', 'i', 'o', 'u' };

    for(char& character : s)
    {
        if(std::find(vowels.begin(), vowels.end(), std::tolower(character)) != vowels.end()) // TODO: Check std::search
        {
            std::cout << character;
        }
    }

    return s;
}

int main()
{
    std::cout << reverseVowels("IceCreAm") << '\n'; // Expected output: AceCreIm
    std::cout << reverseVowels("leetcode") << '\n'; // Expected output: leotcede
}