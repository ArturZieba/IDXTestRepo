//Source: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::find and std::search
#include <cctype> // For std::tolower
#include <iostream>
#include <string>
#include <vector>

std::string reverseVowels (std::string s)
{
    int i = 0;

    std::vector<char> vowels = { 'a', 'e', 'i', 'o', 'u' };
    std::string toReverse;

    for(char& character : s)
    {
        if(std::find(vowels.begin(), vowels.end(), std::tolower(character)) != vowels.end()) 
        {
            std::cout << character;
            toReverse[i] = character;
            i++;
        }
        else
        {
            i++;
        }
    }

    std::cout << toReverse << '\n';

    for(char& character : s)
    {
        if(std::find(vowels.begin(), vowels.end(), std::tolower(character)) != vowels.end()) 
        {
            std::cout << character;
            character = toReverse[i];
            i--;
        }
        else
        {
            i--;
        }
    }
    
    std::cout << toReverse << '\n';

    return s;
}

int main()
{
    std::cout << reverseVowels("IceCreAm") << '\n'; // Expected output: AceCreIm
    std::cout << reverseVowels("leetcode") << '\n'; // Expected output: leotcede
}