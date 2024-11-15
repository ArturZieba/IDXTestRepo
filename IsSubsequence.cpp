#include <iostream>
#include <string>

bool isSubsequence(std::string s, std::string t)
{
    return true;
}

int main()
{
    std::string s0 = "abc";
    std::string t0 = "ahbgdc";

    std::string s1 = "axc";
    std::string t1 = "ahbgdc";

    std::cout << isSubsequence(s0, t0) << '\n'; // Expected output: true
    std::cout << isSubsequence(s1, t1) << '\n'; // Expected output: false
}