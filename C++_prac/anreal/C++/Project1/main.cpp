#include <iostream>



int main()
{
	int num0 = 5, num1 = 10;

	int temp = num0;
	num0 = num1;
	num1 = temp;

	std::cout << num0 << std::endl;
	std::cout << num1 << std::endl;

	return 0; 
}

