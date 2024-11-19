// A header file for storing custom functions which were used in two or more different excercises (.cpp files)
// Note that for readability sake this should not be included for most of the .cpp files in this repo, as they usually do not exceed ~60 lines of code
// Include for bigger source files where most of listed functions would be used
#include <iostream>

// Function used to print true or false to the terminal depending on the passed boolean's value
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