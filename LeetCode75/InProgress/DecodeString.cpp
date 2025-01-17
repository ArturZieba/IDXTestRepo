// Source: https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string decodeString (std::string s)
{
    return s;
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