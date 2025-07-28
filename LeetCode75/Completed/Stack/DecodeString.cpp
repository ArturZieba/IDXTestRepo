// Source: https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string decodeString (std::string s)
{
    std::string decodedString = "";
    int currentIndex = 0;
    int repetition = 0; // Integer before []
    int nestedBracket = 0; // Number of [] sets 

    for (int i = 0; i < s.size(); i++)
    {
        if(nestedBracket == 0 && s[i] >= 'a' && s[i] <= 'z')
        {
            decodedString.push_back(s[i]);
            currentIndex = i + 1;
        }
        if(s[i] == '[')
        {
            nestedBracket++;
            if(nestedBracket == 1)
            {
                repetition = s[i - 1] - '0'; // char - '0' returns an int
                currentIndex = i + 1;
            }
        }
        else if(s[i] == ']')
        {
            nestedBracket--;
            if(nestedBracket == 0)
            {
                while(repetition > 0)
                {
                    decodedString += decodeString(s.substr(currentIndex, i - currentIndex));
                    repetition--;
                }
                currentIndex = i + 1;
            }
        }
    }

    return decodedString;
}

int main()
{
    std::string s0 = "3[a]2[bc]";
    std::string s1 = "3[a2[c]]";
    std::string s2 = "2[abc]3[cd]ef";

    std::cout << decodeString(s0) << '\n'; // Expected output: aaabcbc
    std::cout << decodeString(s1) << '\n'; // Expected output: accaccacc
    std::cout << decodeString(s2) << '\n'; // Expected output: abcabccdcdcdef
}