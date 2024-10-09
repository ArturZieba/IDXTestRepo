// Source: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

bool canPlaceFlowers(std::vector<int>& flowerbed, int n)
{
    return true;
}

int main()
{
    std::vector<int> flowerbed0 = { 1, 0, 0, 0, 1 };
    int n0 = 1;
    std::vector<int> flowerbed1 = { 1, 0, 0, 0, 1 };
    int n1 = 2;

    std::cout << canPlaceFlowers(flowerbed0, n0) << '\n'; //Expected output: true
    std::cout << canPlaceFlowers(flowerbed1, n1) << '\n'; //Expected output: false

    std::cout << "Test\n";
}