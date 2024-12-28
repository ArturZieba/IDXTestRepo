// Source: https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

int compress(std::vector<char>& chars)
{
    return 2;
}

int main()
{
    std::vector<char> chars0 = { "a", "a", "b", "b", "c", "c", "c" };
    std::vector<char> chars1 = { "a" };
    std::vector<char> chars2 = { "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b" };

    std::cout << compress(chars0) << '\n'; // Expected output: 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    std::cout << compress(chars1) << '\n'; // Expected output: 1, and the first character of the input array should be: ["a"]
    std::cout << compress(chars2) << '\n'; // Expected output: 4, and the first 4 characters of the input array should be: ["a","b","1","2"]
}