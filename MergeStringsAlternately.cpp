// Source: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string mergeAlternately(std::string word1, std::string word2)
{
    std::string alternatingString;
    int word1Iterator = 0;
    int word2Iterator = 0;

    while (word1Iterator < word1.size() && word2Iterator < word2.size())
    {
        if (word1Iterator < word1.size())
        {
            alternatingString += word1[word1Iterator];
            word1Iterator++;
        }
            
        if (word2Iterator < word2.size())
        {
            alternatingString += word2[word2Iterator];
            word2Iterator++;
        }
    }

    while (word1Iterator < word1.size())
        {
            alternatingString += word1[word1Iterator];
            word1Iterator++;
        }

    while (word2Iterator < word2.size())
        {
            alternatingString += word2[word2Iterator];
            word2Iterator++;
        }

    return alternatingString + '\n';
}

int main()
{
    std::cout << mergeAlternately("abc", "pqr"); //Expected output: apbqcr
    std::cout << mergeAlternately("ab", "pqrs"); //Expected output: apbqrs
    std::cout << mergeAlternately("abcd", "pq"); //Expected output: apbqcd
    std::cout << mergeAlternately("test","TTEESSTT"); //Expected output: tTeTsEtESSTT
}