// Source: https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

#include <algorithm> // For std::sort
#include <iostream>
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

bool uniqueOccurences(std::vector<int>& arr)
{
    std::sort(arr.begin(), arr.end());
    for(int element : arr)
    {
        std::cout << element;
    }

    return 1;
}

int main()
{
    std::vector arr0 = { 1, 2, 2, 1, 1, 3 };
    std::vector arr1 = { 1, 2 };
    std::vector arr2 = { -3, 0, 1, -3, 1, 1, 1, -3, 10, 0 };

    printBool(uniqueOccurences(arr0)); // Expected output: true
    printBool(uniqueOccurences(arr1)); // Expected output: false
    printBool(uniqueOccurences(arr2)); // Expected output: true
}