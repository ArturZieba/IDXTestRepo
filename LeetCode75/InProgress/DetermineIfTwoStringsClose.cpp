// Source: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

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

bool closeStrings(std::string word1, std::string word2)
{
    return 0;
}

int main()
{
    std::string word01 = "abc";
    std::string word02 = "bca";
    std::string word11 = "a";
    std::string word12 = "aa";
    std::string word21 = "cabbba";
    std::string word22 = "abbccc";

    printBool(closeStrings(word01, word02)); // Expected output: true
    printBool(closeStrings(word11, word12)); // Expected output: false
    printBool(closeStrings(word21, word22)); // Expected output: true
}