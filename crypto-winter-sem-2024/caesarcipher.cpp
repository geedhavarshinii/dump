#include <iostream>
using namespace std;

string encrypt(string text, int s)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
            result += char(int(text[i] + s - 65) % 26 + 65);
        else
            result += char(int(text[i] + s - 97) % 26 + 97);
    }
    return result;
}

string decrypt(string text, int s)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
            result += char(int(text[i] - s - 65 + 26) % 26 + 65);
        else
            result += char(int(text[i] - s - 97 + 26) % 26 + 97);
    }
    return result;
}

int main()
{
    string text;
    int s;
    cout << "Enter the text: ";
    cin >> text;
    cout << "Enter the shift: ";
    cin >> s;
    string encrypted_text = encrypt(text, s);
    cout << "\nEncrypted text: " << encrypted_text;
    string decrypted_text = decrypt(encrypted_text, s);
    cout << "\nDecrypted text: " << decrypted_text;
    return 0;
}