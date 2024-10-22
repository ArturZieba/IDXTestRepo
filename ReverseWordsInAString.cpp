// Source: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string reverseWords(std::string s)
{
    /*
    for(char& character : s)
    {
        if(character != ' ')
        {
            std::cout << character;

            
        }

        if(character == ' ' && s[i-1])
        {
            std::cout << character;
        }
     }
    */

    std::string modString;

    for(int i = 0; i < s.size(); i++)
    {
        if(s[i] != ' ')
        {
            modString += s[i];
        }
        else if(s[i] == ' ' && s[i - 1] != ' ')
        {
            modString += s[i];
        }
    }

     return modString;
}

int main()
{
    std::string s0 = "the sky is blue"; // Expected output: "blue is sky the"
    std::string s1 = "  hello world  "; // Expected output: "world hello"
    std::string s2 = "a good   example"; // Expected output: "example good a"

    std::cout << reverseWords(s0) << '\n';
    std::cout << reverseWords(s1) << '\n';
    std::cout << reverseWords(s2) << '\n';
}