#include <iostream>

int main() {
    // Declare a variable to store the number
    int number;
    std::cin >> number;

    // Calculate the factorial
    int factorial = 1;
    for (int i = 1; i <= number; ++i) {
        factorial *= i;
    }

    // Print the factorial
    std::cout <<factorial << std::endl;

    return 0;
}