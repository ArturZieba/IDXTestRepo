// Source: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
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

bool closeStrings(std::string word1, std::string word2)
{
    // Strings cannot be close if they do not have the same number of characters as per operations
    if(word1.length() != word2.length())
    {
        return 0;
    }

    // Check if there is the same number of the same characters
    std::unordered_map<int, int> uniqueValues0;
    std::unordered_map<int, int> uniqueValues1;

    for(int i = 0; i < word1.size(); i++)
    {
            uniqueValues0[word1[i] - 'a']++; // - 'a' converts the char into int
            uniqueValues1[word2[i] - 'a']++;
    }
    
    std::vector<int> uniqueValuesCount0;
    std::vector<int> uniqueValuesCount1;

    for(int i = 0; i < 26; i++) // 26 for all lower case letters as per constraints
    {
        if(
            ((uniqueValues0.find(i) == uniqueValues0.end())
            && (uniqueValues1.find(i) != uniqueValues1.end())) 
            || 
            ((uniqueValues1.find(i) == uniqueValues1.end())
            && (uniqueValues0.find(i) != uniqueValues0.end()))
        ) // Check if unordered_map contains the same set of unique characters (converted to int)
        {
            return false; // If it does not it cannot match the constraints
        } else if ((uniqueValues0.find(i) != uniqueValues0.end()) && (uniqueValues1.find(i) != uniqueValues1.end()))
        {
           uniqueValuesCount0.push_back(uniqueValues0[i]);
           uniqueValuesCount1.push_back(uniqueValues1[i]);
        }
    }

    std::sort(begin(uniqueValuesCount0), end(uniqueValuesCount0));
    std::sort(begin(uniqueValuesCount1), end(uniqueValuesCount1));

    return uniqueValuesCount0 == uniqueValuesCount1;
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