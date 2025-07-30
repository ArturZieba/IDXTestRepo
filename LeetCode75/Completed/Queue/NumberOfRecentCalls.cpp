// Source: https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <vector>

class RecentCounter
{
public:
    RecentCounter()
    {
    }

    std::vector<int> recentPings = {};

    int ping(int t)
    {
        recentPings.push_back(t);

        // If there is a recent ping and the front ping is smaller than the difference between current ping and 3000ms (more then 3000ms difference)
        while(!recentPings.empty() && recentPings.front() < t - 3000)
        {
            // Remove the front ping
            recentPings.erase(recentPings.begin());
        }

        return recentPings.size();
    }
};

int main()
{
    RecentCounter* recentCounter = new RecentCounter();
    std::cout << recentCounter->ping(1) << '\n'; // Expected output: 1
    std::cout << recentCounter->ping(100) << '\n'; // Expected output: 2
    std::cout << recentCounter->ping(3001) << '\n'; // Expected output: 3
    std::cout << recentCounter->ping(3002) << '\n'; // Expected output: 3
}