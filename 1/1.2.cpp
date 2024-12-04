#include <iostream>
#define SIZE 1000

using namespace std;

int main()
{
	int arr1[SIZE];
	int arr2[SIZE];
	
	for(int i = 0; i < SIZE; ++i)
	{
		cin >> arr1[i] >> arr2[i];
	}
	
	int sim_score = 0;
	for(int i = 0; i < SIZE; ++i)
	{
		int num = arr1[i];
		int counter = 0;
		for(int j = 0; j < SIZE; ++j)
		{
			if(num == arr2[j])
			{
				++counter;
			}
		}
		sim_score += num * counter;
	}
	
	cout << sim_score << "\n";
	
	return 0;	
}
