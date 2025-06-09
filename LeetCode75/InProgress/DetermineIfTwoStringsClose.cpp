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
    std::unordered_map<int, int> uniqueValuesCount0;
    std::unordered_map<int, int> uniqueValuesCount1;

    for(int i = 0; i < word1.size(); i++)
    {
            uniqueValuesCount0[word1[i] - 'a']++; // - 'a' converts the char into int
            uniqueValuesCount1[word2[i] - 'a']++;
    }
    
    for(int i = 0; i < 26; i++) // 26 for all lower case letters as per constraints
    {
        if(
            ((uniqueValuesCount0.find(i) == uniqueValuesCount0.end())
            && (uniqueValuesCount1.find(i) != uniqueValuesCount1.end())) 
            || 
            ((uniqueValuesCount1.find(i) == uniqueValuesCount1.end())
            && (uniqueValuesCount0.find(i) != uniqueValuesCount0.end()))
        ) // Check if unordered_map contains the same set of unique characters (converted to int)
        {
            return false; // If it does not it cannot match the constraints
        } /*else if (TBC)
        {
           return true; 
        }*/
    }

    for(auto element : uniqueValuesCount0)
    {
        std::cout << element.first << " " << element.second << "\n";
    }

    for(auto element : uniqueValuesCount1)
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