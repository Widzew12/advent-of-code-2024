#include <bits/stdc++.h>
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
	
	sort(arr1, arr1 + SIZE);
	sort(arr2, arr2 + SIZE);
	
	int distance = 0;
	
	for(int i = 0; i < SIZE; ++i)
	{
		distance += abs(arr1[i] - arr2[i]);
	}
	
	cout << distance << "\n";
	
	return 0;
}
