#include <iostream>
using namespace std;
void getKeyMatrix(string key, int keyMatrix[][3])
{
    int k = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            keyMatrix[i][j] = (key[k]) % 65;
            k++;
        }
    }
}
void encrypt(int cipherMatrix[][1],
             int keyMatrix[][3],
             int messageVector[][1])
{
    int x, i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 1; j++)
        {
            cipherMatrix[i][j] = 0;
            for (x = 0; x < 3; x++)
            {
                cipherMatrix[i][j] +=
                    keyMatrix[i][x] * messageVector[x][j];
            }
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
        }
    }
}
string HillCipher(string message, string key)
{
    int keyMatrix[3][3];
    getKeyMatrix(key, keyMatrix);
    int messageVector[3][1];
    for (int i = 0; i < 3; i++)
        messageVector[i][0] = (message[i]) % 65;
    int cipherMatrix[3][1];
    encrypt(cipherMatrix, keyMatrix, messageVector);
    string CipherText;
    for (int i = 0; i < 3; i++)
        CipherText += cipherMatrix[i][0] + 65;
    cout << "Encrypted text: " << CipherText;
    return CipherText;
}
int modInverse(int a, int m)
{
    for (int i = 1; i < m; i++)
    {
        if ((a * i) % m == 1)
        {
            return i;
        }
    }
    return -1;
}
void getInverseKeyMatrix(int keyMatrix[][3], int inverseKeyMatrix[][3])
{
    int det = keyMatrix[0][0] * (keyMatrix[1][1] * keyMatrix[2][2] -
                                 keyMatrix[1][2] * keyMatrix[2][1]) -
              keyMatrix[0][1] * (keyMatrix[1][0] * keyMatrix[2][2] -
                                 keyMatrix[1][2] * keyMatrix[2][0]) +
              keyMatrix[0][2] * (keyMatrix[1][0] * keyMatrix[2][1] -
                                 keyMatrix[1][1] * keyMatrix[2][0]);
    det = (det + 26) % 26;
    int detInverse = modInverse(det, 26);
    inverseKeyMatrix[0][0] = (keyMatrix[1][1] * keyMatrix[2][2] -
                              keyMatrix[1][2] * keyMatrix[2][1]) %
                             26;
    inverseKeyMatrix[0][1] = (keyMatrix[0][2] * keyMatrix[2][1] -
                              keyMatrix[0][1] * keyMatrix[2][2]) %
                             26;
    inverseKeyMatrix[0][2] = (keyMatrix[0][1] * keyMatrix[1][2] -
                              keyMatrix[0][2] * keyMatrix[1][1]) %
                             26;
    inverseKeyMatrix[1][0] = (keyMatrix[1][2] * keyMatrix[2][0] -
                              keyMatrix[1][0] * keyMatrix[2][2]) %
                             26;
    inverseKeyMatrix[1][1] = (keyMatrix[0][0] * keyMatrix[2][2] -
                              keyMatrix[0][2] * keyMatrix[2][0]) %
                             26;
    inverseKeyMatrix[1][2] = (keyMatrix[0][2] * keyMatrix[1][0] -
                              keyMatrix[0][0] * keyMatrix[1][2]) %
                             26;
    inverseKeyMatrix[2][0] = (keyMatrix[1][0] * keyMatrix[2][1] -
                              keyMatrix[1][1] * keyMatrix[2][0]) %
                             26;
    inverseKeyMatrix[2][1] = (keyMatrix[0][1] * keyMatrix[2][0] -
                              keyMatrix[0][0] * keyMatrix[2][1]) %
                             26;
    inverseKeyMatrix[2][2] = (keyMatrix[0][0] * keyMatrix[1][1] -
                              keyMatrix[0][1] * keyMatrix[1][0]) %
                             26;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            inverseKeyMatrix[i][j] = (inverseKeyMatrix[i][j] * detInverse) %
                                     26;
            if (inverseKeyMatrix[i][j] < 0)
            {
                inverseKeyMatrix[i][j] += 26;
            }
        }
    }
}
void decrypt(int decipherMatrix[][1], int inverseKeyMatrix[][3], int cipherMatrix[][1])
{
    int x, i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 1; j++)
        {
            decipherMatrix[i][j] = 0;
            for (x = 0; x < 3; x++)
            {
                decipherMatrix[i][j] +=
                    inverseKeyMatrix[i][x] * cipherMatrix[x][j];
            }
            decipherMatrix[i][j] = decipherMatrix[i][j] % 26;
        }
    }
}
void HillDecipher(string cipherText, string key)
{
    int keyMatrix[3][3];
    getKeyMatrix(key, keyMatrix);
    int inverseKeyMatrix[3][3];
    getInverseKeyMatrix(keyMatrix, inverseKeyMatrix);
    int cipherMatrix[3][1];
    for (int i = 0; i < 3; i++)
        cipherMatrix[i][0] = (cipherText[i] - 'A') % 26;
    int decipherMatrix[3][1];
    decrypt(decipherMatrix, inverseKeyMatrix, cipherMatrix);
    string DecipherText;
    for (int i = 0; i < 3; i++)
        DecipherText += decipherMatrix[i][0] + 'A';
    cout << "Decrypted Text: " << DecipherText;
}
int main()
{
    string message = "WIN";
    string key = "GYBNQKURP";
    cout << "Message: " << message << endl;
    cout << "Key: " << key << endl;
    string encrypted_text = HillCipher(message, key);
    cout << endl;
    HillDecipher(encrypted_text, key);
    return 0;
}