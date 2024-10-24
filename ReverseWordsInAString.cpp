// Source: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string reverseWords(std::string s)
{
    std::string modString;
    std::string toReverse;
    
    int i = 0; // Iterator for std::string toReverse

    toReverse += "\""; // Add " at the end of the string

    for(int i = s.find_first_not_of(" "); i < s.size(); i++)
    {
        if(s[i] != ' ')
        {
            toReverse += s[i];
        }
        else if(s[i] == ' ' && s[i - 1] != ' ')
        {
            toReverse += s[i];
        }
    }

    if(toReverse.substr(toReverse.size() - 1) == " ")
    {
        toReverse.pop_back();
    }

    toReverse += "\""; // Add " at the end of the string

    for(char& character : toReverse)
    {
        if(character != ' ') 
        {
            toReverse[i] = character;
            i++;
        }
    }
    for(char& character : toReverse)
    {
        if(character != ' ') 
        {
            character = toReverse[i - 1];
            i--;
        }
    }

    return toReverse;
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