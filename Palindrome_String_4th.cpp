#include <iostream>
#include <string.h>
using namespace std;

void reverseStr(string str)
{
    int n = str.length();
    string real_str = str;

    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);

    real_str.append(str);

    cout << real_str << endl;
}

int main()
{
    char string1[20];
    int i, length;
    int flag = 0;

    cout << "Enter a string for Palindrome Check: ";
    cin >> string1;

    length = strlen(string1);

    for (i = 0; i < length; i++)
    {
        if (string1[i] != string1[length - i - 1])
        {
            flag = 1;
            break;
        }
    }

    if (flag)
    {
        cout << string1 << " is not a palindrome" << endl;
    }
    else
    {
        cout << string1 << " is a palindrome" << endl;
    }

    string str;
    cout << "Enter String to Reverse and Concatenate: " << endl;
    cin >> str;

    reverseStr(str);
}
