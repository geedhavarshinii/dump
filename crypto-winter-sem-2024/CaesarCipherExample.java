import java.util.Scanner;

public class CaesarCipherExample {
    public static final String Alphabet = "abcdefghijklmnopqrstuvwxyz";

    public static String encryptData(String inputStr, int shiftKey) {
        inputStr = inputStr.toLowerCase();
        String encryptStr = "";
        for (int i = 0; i < inputStr.length(); i++) {
            int pos = Alphabet.indexOf(inputStr.charAt(i));
            int encryptPos = (shiftKey + pos) % 26;
            char encryptChar = Alphabet.charAt(encryptPos);
            encryptStr += encryptChar;
        }
        return encryptStr;
    }

    public static String decryptData(String inputStr, int shiftKey) {
        inputStr = inputStr.toLowerCase();
        String decryptStr = "";
        for (int i = 0; i < inputStr.length(); i++) {
            int pos = Alphabet.indexOf(inputStr.charAt(i));
            int decryptPos = (pos - shiftKey) % 26;
            if (decryptPos < 0) {
                decryptPos = Alphabet.length() + decryptPos;
            }
            char decryptChar = Alphabet.charAt(decryptPos);
            decryptStr += decryptChar;
        }
        return decryptStr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string to be encrypted: ");
        String inputStr = sc.nextLine();
        System.out.println("Enter the key to be used to shift: ");
        int shiftKey = sc.nextInt();
        System.out.println("Encrypted data: " + encryptData(inputStr, shiftKey));
        System.out.println("Decrypted data: " + decryptData(encryptData(inputStr, shiftKey), shiftKey));
    }
}
