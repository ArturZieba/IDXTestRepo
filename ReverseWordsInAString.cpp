// Source: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For reverse()
#include <iostream>
#include <string>

std::string reverseWords(std::string s)
{
    std::string modString;
    std::string toReverse;

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

    reverse(toReverse.begin(), toReverse.end());
    toReverse.insert(toReverse.end(), ' '); // Add a space temporarily so that the last word in a string is recognized later as a separate word

    int j = 0; // Element marking the end of the word in the string

    for(int i = 0; i < toReverse.size(); i++)
    {
        if(toReverse[i] == ' ')
        {
            reverse(toReverse.begin() + j, toReverse.begin() + i);

            j = i + 1;
        }
    }

    toReverse.pop_back();

    toReverse.insert(toReverse.begin(), '\"');
    toReverse.insert(toReverse.end(), '\"');

    return toReverse;
}

int main()
{
    std::string s0 = "the sky is blue";  // Expected output: "blue is sky the"
    std::string s1 = "  hello world  ";  // Expected output: "world hello"
    std::string s2 = "a good   example"; // Expected output: "example good a"

    std::cout << reverseWords(s0) << '\n';
    std::cout << reverseWords(s1) << '\n';
    std::cout << reverseWords(s2) << '\n';
}