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

    /*while (senate.find("R") || senate.find("D"))
    {
        for (int i = 0; i < senate.size(); i++)
        {
            if(senate[i] - '0' == 'R' && !senate.find("D"))
            {
                return "Radiant";
            }
            else if(senate[i] - '0' == 'D' && !senate.find("R"))
            {
                return "Dire";
            }
            else if(senate[i] - '0' == 'R')
            {
                senate.erase(senate.find("D"));
            }
            else if(senate[i] - '0' == 'D')
            {
                senate.erase(senate.find("R"));
            }
        }
    }*/

    return std::to_string(direSenators.back());
}

int main()
{
    std::string senate0 = "RD";
    std::string senate1 = "RDD"; 

    std::cout << predictPartyVictory(senate0); // Expected output: "Radiant"
    std::cout << predictPartyVictory(senate1); // Expected output: "Dire"
}