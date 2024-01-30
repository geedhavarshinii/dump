#include <iostream>
using namespace std;

string encrypt(string text)
{
    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";
    string encrypted_text = "";
    for (int i = 0; i < text.size(); i++)
    {
        encrypted_text += key[text[i] - 'A'];
    }
    return encrypted_text;
}

string decrypt(string encrypted_text)
{
    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";
    string original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string text = "";
    for (int i = 0; i < encrypted_text.size(); i++)
    {
        int index;
        for (int j = 0; j < 26; j++)
        {
            if (key[j] == encrypted_text[i])
            {
                index = j;
            }
        }
        text += original[index];
    }
    return text;
}
int main()
{
    string text;
    cout << "Enter text (IN CAPITAL): ";
    cin >> text;
    cout << "Encrypted text: " << encrypt(text) << endl;
    cout << "Decrypted text: " << decrypt(encrypt(text)) << endl;
    return 0;
}