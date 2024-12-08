#include <iostream>

using namespace std;

int main()
{
    int num = 0;
    for(int i = 0; i < 736; ++i)
    {
        int num1, num2;
        cin >> num1 >> num2;
        num += num1 * num2;
    }
    cout << num << "\n";
    return 0;
}