#include <bits/stdc++.h>

using namespace std;

// <stone, <iteration, number>>
map<long long, map<long long, long long>> prev_stones_map;

int iteration = 0;

long long check_stone(long long stone, int counter)
{
    ++counter;

    if (counter == 76)
    {
        return 1;
    }

    bool add_to_map = false;

    if (stone < 0)
    {
        cout << stone << "\n";
    }

    if (stone < 10)
    {
        // Check if key is in map
        if (prev_stones_map.count(stone))
        {
            if (prev_stones_map[stone].count(counter))
            {
                // If stone iteration is in map, return the stone number
                long long number_to_return = prev_stones_map[stone][counter];
                if(number_to_return < 0)
                {
                    // cout << num << "\n";
                }
                return number_to_return;
            }
            else
            {
                // If stone iteration isn't in map, add to the map
                add_to_map = true;
            }
        }
        else
        {
            // If stone isn't in map, add to the map
            add_to_map = true;
        }
    }

    if (counter < 40)
    {
        // cout << counter << "\n";
    }

    

    int digits_num = floor(log10(stone) + 1);

    

    long long num;

    // cout << iteration << "\n";
    // ++iteration;

    if (stone == 0)
    {
        num = check_stone(1, counter);
        if (num < 0)
        {
            cout << "ERROR1: " << stone << ": " << counter << ": " << num << "\n";
        }
    }
    else if (digits_num % 2 == 0)
    {
     
        int power = pow(10, digits_num / 2);
        long long stone_1 = stone / power;
        long long stone_2 = stone % power;
        if (stone_1 < 0)
        {
            cout << "ERROR4: " << stone_1 << ": " << counter << ": " << num << "\n";
        }
        if (stone_2 < 0)
        {
            cout << "ERROR5: " << stone_2 << ": " << counter << ": " << num << "\n";
        }
        num = check_stone(stone_1, counter) + check_stone(stone_2, counter);
        if (num < 0)
        {
            // cout << "ERROR2: " << stone << ": " << counter << ": " << num << "\n";
        }
    }
    else
    {
        long long stone_1 = stone * 2024;
        if (stone_1 < 0)
        {
            cout << "ERROR6: " << stone_1 << ": " << counter << ": " << num << "\n";
        }
        num = check_stone(stone_1, counter);
        if (num < 0)
        {
            // cout << "ERROR3: " << stone << ": " << counter << ": " << num << "\n";
        }
    }

    if(add_to_map)
    {
        prev_stones_map[stone][counter] = num;
        // cout << stone << ": " << counter << ": " << num << "\n";
    }

    if(num < 0)
    {
        // cout << "ERROR: " << stone << ": " << num << ": " << counter << "\n";
    }

    return num;
}


int main()
{
    cout << prev_stones_map.max_size() << "\n\n";

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
