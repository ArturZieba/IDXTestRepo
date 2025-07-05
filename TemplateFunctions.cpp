#include "Headers/TemplateFunctions.h"

int main()
{
    // Tests for functions from TemplateFunctions.h
    printBool(0); // Expected output: false
    printBool(1); // Expected output: true

    std::vector<int> v = {1, 2, 3, 4, 5};
    printVectorInt(v); // Expected output: [1,2,3,4,5]
}