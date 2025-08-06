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
        radiantSenators.pop();
        direSenators.pop();

        if (radiantSenators.front() < direSenators.front())
        {
            radiantSenators.push(radiantSenators.front() + senate.size());
        }
        else
        {
            direSenators.push(direSenators.front() + senate.size());
        }
    }

    return radiantSenators.empty() ? "Dire" : "Radiant";
}

int main()
{
    std::string senate0 = "RD";
    std::string senate1 = "RDD"; 

    std::cout << predictPartyVictory(senate0); // Expected output: "Radiant"
    std::cout << predictPartyVictory(senate1); // Expected output: "Dire"
}