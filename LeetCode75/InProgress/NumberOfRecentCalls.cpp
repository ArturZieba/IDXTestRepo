// Source: https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>

class RecentCounter
{
public:
    RecentCounter()
    {
        
    }

    int Counter = 0;

    int ping(int t)
    {
        return t;
    }
};

int main()
{
    // Expected output: [null, 1, 2, 3, 3]
    RecentCounter* recentCounter = new RecentCounter(); 
    std::cout << recentCounter->Counter << '\n'; // Expected output: null
    std::cout << recentCounter->ping(1) << '\n'; // Expected output: 1
    std::cout << recentCounter->ping(100) << '\n'; // Expected output: 2
    std::cout << recentCounter->ping(3001) << '\n'; // Expected output: 3
    std::cout << recentCounter->ping(3002) << '\n'; // Expected output: 3
}