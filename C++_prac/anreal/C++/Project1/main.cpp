#include <iostream>

int main()
{
	int arr[6] = { 0,1,2,3,4,5 };
	int* ptr = arr;

	for (int i = 0; i < 6; ++i)
	{
		std::cout << *(ptr + i) << std::endl;
	}

	return 0; 
}
 
