#include <iostream>

using namespace std;

int check_stone(long long stone, int counter)
{
    ++counter;

    if (counter < 40)
    {
        cout << counter << "\n";
    }

    if (counter == 76)
    {
        return 1;
    }

    int num = 0;

    string stone_str = to_string(stone);

    if (stone == 0)
    {
        int new_stone = 1;
        num = check_stone(new_stone, counter);
    }
    else if (stone_str.length() % 2 == 0)
    {
        int split_index = stone_str.length() / 2;
        string new_stone_1_str = stone_str.substr(0, split_index);
        // cout << new_stone_1_str << "\n";
        long long new_stone_1 = stoi(new_stone_1_str);
        string new_stone_2_str = stone_str.substr(split_index, stone_str.length() - split_index);
        // cout << new_stone_2_str << "\n";
        long long new_stone_2 = stoi(new_stone_2_str);
        int num_1 = check_stone(new_stone_1, counter);
        int num_2 = check_stone(new_stone_2, counter);
        num = num_1 + num_2;
    }
    else
    {
        long long new_stone = stone * 2024;
        num = check_stone(new_stone, counter);
    }

    return num;
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
