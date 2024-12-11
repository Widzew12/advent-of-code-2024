#include <bits/stdc++.h>

using namespace std;

int iteration = 0;

int check_stone(long long stone, int counter)
{
    ++counter;

    if (counter < 40)
    {
        // cout << counter << "\n";
    }

    if (counter == 76)
    {
        return 1;
    }

    int digits_num = floor(log10(stone) + 1);

    cout << iteration << "\n";
    ++iteration;

    if (stone == 0)
    {
        return check_stone(1, counter);
    }
    else if (digits_num % 2 == 0)
    {
        int power = pow(10, digits_num / 2);
        return check_stone(stone / power, counter) + check_stone(stone % power, counter);
    }
    else
    {
        return check_stone(stone * 2024, counter);
    }
}


int main()
{
    const int length = 1;

    int stones[length];
    for (int i = 0; i < length; ++i)
    {
        cin >> stones[i];
    }

    long long total_num = 0;

    for (int i = 0; i < length; ++i)
    {
        long long num = check_stone(stones[i], 0);
        cout << num << "\n";
        total_num += num;
    }

    cout << "\n" << total_num << "\n";

    return 0;
}
