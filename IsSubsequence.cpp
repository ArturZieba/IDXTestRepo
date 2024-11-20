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
    int subsequenceChars = 0;

    for (int i = 0; i < s.size(); i++)
    {
        for (int j = 0; j < t.size(); j++)
        {
            if (s[i] == t[j])
            {
                subsequenceChars++;
            }
        }
    }

    if(subsequenceChars == s.size())
    {
        return true;
    }
    else 
    {
        return false;
    }
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