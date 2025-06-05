// Source: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>
#include <unordered_map>

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
    // Strings cannot be close if they do not have the same number of characters as per operations
    if(word1.length() != word2.length())
    {
        return 0;
    }

    // Check if there is the same number of the same characters
    std::unordered_map<int, int> uniqueValuesCount = {{1, 1}, {2, 1}, {3, 1}};
    
    for(auto element : uniqueValuesCount)
    {
        std::cout << element.first << " " << element.second << "\n";
    }

    return 1;
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