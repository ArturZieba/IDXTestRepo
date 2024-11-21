#include <iostream>
#include <string>
#include <vector>

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
    int subsequenceCount = 0;

    if(t.size() >= s.size()) // Confirm that the t string can even contain s string
    {
        for(int i = 0; i < t.size(); i++)
        {
            for(int j = 0; j < s.size(); j++)
            {
                if (t[i] == s[j])
                {
                    subsequenceCount++;
                    std::cout << subsequenceCount;
                }
            }
        }
    }

    return subsequenceCount == s.size();
}

int main()
{
    std::string s0 = "abc";
    std::string t0 = "aahbgdc";

    std::string s1 = "axc";
    std::string t1 = "ahbgdc";

    printBool(isSubsequence(s0, t0)); // Expected output: true
    printBool(isSubsequence(s1, t1)); // Expected output: false
}