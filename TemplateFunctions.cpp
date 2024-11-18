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

int main()
{
    // Tests for functions
    printBool(0); // Expected output: false
    printBool(1); // Expected output: true
}