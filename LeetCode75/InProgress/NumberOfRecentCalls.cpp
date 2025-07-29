// Source: https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

class RecentCounter
{
public:
    RecentCounter()
    {
    }

    int ping(int t)
    {
        int Counter = 0;
        std::vector<int> recentPings = {};
        recentPings.push_back(t);

        return recentPings.size();
    }
};

int main()
{
    // Expected output: [null, 1, 2, 3, 3]
    RecentCounter* recentCounter = new RecentCounter(); // Expected output: null
    std::cout << recentCounter->ping(1) << '\n'; // Expected output: 1
    std::cout << recentCounter->ping(100) << '\n'; // Expected output: 2
    std::cout << recentCounter->ping(3001) << '\n'; // Expected output: 3
    std::cout << recentCounter->ping(3002) << '\n'; // Expected output: 3
}