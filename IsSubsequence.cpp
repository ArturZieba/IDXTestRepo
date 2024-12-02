// Source: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

void printBool (bool bInput)
{
    if (bInput == 1) {
        std::cout << "true\n";
    }
    else 
    {
        std::cout << "false\n";
    }
}

bool isSubsequence(std::string s, std::string t)
{
    int sIterator = 0;
    int tIterator = 0;

    if(t.size() >= s.size()) // Confirm that the t string can even contain s string
    {
        for(; sIterator < s.size() && tIterator < t.size(); tIterator++)
        {
            if (t[tIterator] == s[sIterator])
            {
                ++sIterator;
                std::cout << sIterator;
            }
        }
    }

    return sIterator == s.size();
}

int main()
{
    std::string s0 = "abc";
    std::string t0 = "ahbgdc";

    std::string s1 = "axc";
    std::string t1 = "ahbgdc";

    printBool(isSubsequence(s0, t0)); // Expected output: true
    printBool(isSubsequence(s1, t1)); // Expected output: false
}