#include <bits/stdc++.h>

using namespace std;

// <stone, <iteration, number>>
map<long long, map<long long, long long>> prev_stones_map;

long long check_stone(long long stone, int counter)
{
    ++counter;

    if (counter == 76)
    {
        return 1;
    }

    if (prev_stones_map.count(stone))
    {
        if (prev_stones_map[stone].count(counter))
        {
            // If stone iteration is in map, return the stone number
            return prev_stones_map[stone][counter];
        }
    }

    int digits_num = floor(log10(stone) + 1);

    long long num;

    if (stone == 0)
    {
        num = check_stone(1, counter);
    }
    else if (digits_num % 2 == 0)
    {
        int power = pow(10, digits_num / 2);
        num = check_stone(stone / power, counter) + check_stone(stone % power, counter);
    }
    else
    {
        num = check_stone(stone * 2024, counter);
    }

    prev_stones_map[stone][counter] = num;
    return num;
}


int main()
{
    const int length = 8;

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
