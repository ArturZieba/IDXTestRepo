// Source: https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>
#include <queue>

std::string predictPartyVictory(std::string senate)
{
    std::queue<int> radiantSenators;
    std::queue<int> direSenators;

    for (int i = 0; i < senate.size(); i++)
    {
        if(senate[i] == 'R')
        {
            radiantSenators.push(i);
        }
        else if(senate[i] == 'D')
        {
            direSenators.push(i);
        }
    }

    while (!radiantSenators.empty() && !direSenators.empty())
    {
        int radiantFrontIndex = radiantSenators.front();
        int direFrontIndex = direSenators.front();

        radiantSenators.pop();
        direSenators.pop();

        // If radiant senator is in front of the dire senator in queue
        if (radiantFrontIndex < direFrontIndex)
        {
            // Radiant senator wins (bans dire senator) and gets back at the end of the queue
            radiantSenators.push(radiantFrontIndex + senate.size());
        }
        else // If dire senator is in front of the radiant senator in queue
        {
            // Dire senator wins (bans radiant senator) and gets back at the end of the queue
            direSenators.push(direFrontIndex + senate.size());
        }
    }

    return radiantSenators.empty() ? "Dire" : "Radiant";
}

int main()
{
    std::string senate0 = "RD";
    std::string senate1 = "RDD"; 

    std::cout << predictPartyVictory(senate0) << '\n'; // Expected output: "Radiant"
    std::cout << predictPartyVictory(senate1) << '\n'; // Expected output: "Dire"
}