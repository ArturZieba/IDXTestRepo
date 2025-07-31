// Source: https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>
#include <string>

std::string predictPartyVictory(std::string senate)
{
    while (!senate.find("R") || !senate.find("D"))
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
                //senate.pop_back(senate.find("D"));
            }
            else if(senate[i] - '0' == 'D')
            {
                //senate.pop_back(senate.find("R"));
            }
        }
    }

    return senate;
}

int main()
{
    std::string senate0 = "RD";
    std::string senate1 = "RDD"; 

    std::cout << predictPartyVictory(senate0); // Expected output: "Radiant"
    std::cout << predictPartyVictory(senate1); // Expected output: "Dire"
}