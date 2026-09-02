#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <set>

using namespace std;

// ------------------------------------------------------
// Function Prototypes
// ------------------------------------------------------

string readFile(const string &filename);

void writeFile(const string &filename, const string &text);

string encryptMonoalphabetic(
    const string &plaintext,
    const string &key
);

void frequency_analysis(const string &ciphertext);

void word_frequency_analysis(const string &ciphertext);

string getPattern(const string &word);

void pattern_analysis(const string &ciphertext);

string apply_substitution(
    const string &ciphertext,
    const map<char, char> &substitution
);

void display_partial_plaintext(
    const string &ciphertext,
    const map<char, char> &substitution
);

bool verify_solution(
    const string &plaintext,
    const string &ciphertext,
    const string &key
);

void cryptanalysis(
    const string &ciphertext,
    const string &plaintext,
    const string &encryptionKey
);


// ------------------------------------------------------
// Read complete text file
// ------------------------------------------------------

string readFile(const string &filename)
{
    ifstream file(filename);

    if (!file)
    {
        cout << "Error opening file: " << filename << endl;
        return "";
    }

    string text;
    string line;

    while (getline(file, line))
    {
        text += line;
        text += '\n';
    }

    file.close();

    return text;
}


// ------------------------------------------------------
// Write text to file
// ------------------------------------------------------

void writeFile(
    const string &filename,
    const string &text
)
{
    ofstream file(filename);

    if (!file)
    {
        cout << "Error creating file: "
             << filename << endl;

        return;
    }

    file << text;

    file.close();
}


// ------------------------------------------------------
// Monoalphabetic substitution encryption
//
// alphabet:
// ABCDEFGHIJKLMNOPQRSTUVWXYZ
//
// Example key:
// QWERTYUIOPASDFGHJKLZXCVBNM
//
// A -> Q
// B -> W
// C -> E
// ...
// ------------------------------------------------------

string encryptMonoalphabetic(
    const string &plaintext,
    const string &key
)
{
    string ciphertext = "";

    for (char ch : plaintext)
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            int index = ch - 'A';

            ciphertext += key[index];
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            int index = ch - 'a';

            ciphertext += key[index];
        }
        else
        {
            // Preserve spaces and punctuation
            ciphertext += ch;
        }
    }

    return ciphertext;
}


// ------------------------------------------------------
// Required Function 1
//
// Letter frequency analysis
// ------------------------------------------------------

void frequency_analysis(
    const string &ciphertext
)
{
    int frequency[26] = {0};

    int totalLetters = 0;

    for (char ch : ciphertext)
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            frequency[ch - 'A']++;

            totalLetters++;
        }
        else if (ch >= 'a' && ch <= 'z')
        {
            frequency[ch - 'a']++;

            totalLetters++;
        }
    }

    vector<pair<char, int>> result;

    for (int i = 0; i < 26; i++)
    {
        result.push_back(
            {char('A' + i), frequency[i]}
        );
    }

    // Sort by descending frequency
    sort(
        result.begin(),
        result.end(),
        [](const pair<char, int> &a,
           const pair<char, int> &b)
        {
            return a.second > b.second;
        }
    );

    cout << "\n==========================================\n";
    cout << "        LETTER FREQUENCY ANALYSIS\n";
    cout << "==========================================\n\n";

    cout << left
         << setw(12) << "Letter"
         << setw(12) << "Count"
         << setw(15) << "Percentage"
         << endl;

    cout << "------------------------------------------\n";

    for (auto p : result)
    {
        double percentage = 0;

        if (totalLetters != 0)
        {
            percentage =
                (p.second * 100.0) / totalLetters;
        }

        cout << left
             << setw(12) << p.first
             << setw(12) << p.second
             << fixed
             << setprecision(2)
             << percentage
             << "%"
             << endl;
    }

    cout << "\nDescending frequency order:\n";

    for (auto p : result)
    {
        if (p.second > 0)
        {
            cout << p.first << " ";
        }
    }

    cout << endl;

    if (!result.empty())
    {
        int maximum = result[0].second;

        cout << "\nMost frequent letter(s): ";

        for (auto p : result)
        {
            if (p.second == maximum)
            {
                cout << p.first << " ";
            }
        }

        cout << endl;
    }
}


// ------------------------------------------------------
// Extract words manually
// ------------------------------------------------------

vector<string> extractWords(
    const string &text
)
{
    vector<string> words;

    string currentWord = "";

    for (char ch : text)
    {
        if ((ch >= 'A' && ch <= 'Z') ||
            (ch >= 'a' && ch <= 'z'))
        {
            if (ch >= 'a' && ch <= 'z')
            {
                ch = ch - 'a' + 'A';
            }

            currentWord += ch;
        }
        else
        {
            if (!currentWord.empty())
            {
                words.push_back(currentWord);

                currentWord = "";
            }
        }
    }

    if (!currentWord.empty())
    {
        words.push_back(currentWord);
    }

    return words;
}


// ------------------------------------------------------
// Required Function 2
//
// Word-frequency analysis
// ------------------------------------------------------

void word_frequency_analysis(
    const string &ciphertext
)
{
    vector<string> words =
        extractWords(ciphertext);

    map<string, int> frequency;

    for (string word : words)
    {
        frequency[word]++;
    }

    vector<pair<string, int>> result;

    for (auto item : frequency)
    {
        result.push_back(item);
    }

    sort(
        result.begin(),
        result.end(),
        [](const pair<string, int> &a,
           const pair<string, int> &b)
        {
            return a.second > b.second;
        }
    );

    cout << "\n==========================================\n";
    cout << "           WORD FREQUENCY ANALYSIS\n";
    cout << "==========================================\n";

    cout << "\nRepeated / frequent words:\n\n";

    cout << left
         << setw(20) << "Word"
         << setw(10) << "Count"
         << endl;

    cout << "------------------------------\n";

    for (auto item : result)
    {
        if (item.second > 1)
        {
            cout << left
                 << setw(20) << item.first
                 << setw(10) << item.second
                 << endl;
        }
    }

    cout << "\nOne-letter words:\n";

    for (auto item : frequency)
    {
        if (item.first.length() == 1)
        {
            cout << item.first
                 << " ("
                 << item.second
                 << ") ";
        }
    }

    cout << "\n\nTwo-letter words:\n";

    for (auto item : frequency)
    {
        if (item.first.length() == 2)
        {
            cout << item.first
                 << " ("
                 << item.second
                 << ") ";
        }
    }

    cout << "\n\nThree-letter words:\n";

    for (auto item : frequency)
    {
        if (item.first.length() == 3)
        {
            cout << item.first
                 << " ("
                 << item.second
                 << ") ";
        }
    }

    cout << endl;
}


// ------------------------------------------------------
// Generate repeated-letter pattern
//
// HELLO -> 0 1 2 2 3
// APPLE -> 0 1 1 2 3
// TEST  -> 0 1 2 0
// THAT  -> 0 1 2 0
// ------------------------------------------------------

string getPattern(
    const string &word
)
{
    map<char, int> positions;

    int nextNumber = 0;

    string pattern = "";

    for (char ch : word)
    {
        if (positions.find(ch) ==
            positions.end())
        {
            positions[ch] = nextNumber;

            nextNumber++;
        }

        pattern +=
            to_string(positions[ch]);

        pattern += ".";
    }

    return pattern;
}


// ------------------------------------------------------
// Required Function 3
//
// Pattern analysis
// ------------------------------------------------------

void pattern_analysis(
    const string &ciphertext
)
{
    vector<string> words =
        extractWords(ciphertext);

    set<string> uniqueWords;

    for (string word : words)
    {
        uniqueWords.insert(word);
    }

    cout << "\n==========================================\n";
    cout << "              PATTERN ANALYSIS\n";
    cout << "==========================================\n";

    cout << "\nWord patterns:\n\n";

    cout << left
         << setw(20) << "Cipher Word"
         << setw(20) << "Pattern"
         << endl;

    cout << "------------------------------------------\n";

    for (string word : uniqueWords)
    {
        cout << left
             << setw(20) << word
             << setw(20) << getPattern(word)
             << endl;
    }

    cout << "\nWords containing repeated letters:\n\n";

    for (string word : uniqueWords)
    {
        bool repeated = false;

        for (int i = 0;
             i < (int)word.size();
             i++)
        {
            for (int j = i + 1;
                 j < (int)word.size();
                 j++)
            {
                if (word[i] == word[j])
                {
                    repeated = true;
                }
            }
        }

        if (repeated)
        {
            cout << word
                 << " -> "
                 << getPattern(word)
                 << endl;
        }
    }
}


// ------------------------------------------------------
// Required Function 4
//
// Apply guessed ciphertext -> plaintext mapping
// ------------------------------------------------------

string apply_substitution(
    const string &ciphertext,
    const map<char, char> &substitution
)
{
    string result = "";

    for (char ch : ciphertext)
    {
        char upper = ch;

        if (ch >= 'a' && ch <= 'z')
        {
            upper =
                ch - 'a' + 'A';
        }

        if (upper >= 'A' &&
            upper <= 'Z')
        {
            auto it =
                substitution.find(upper);

            if (it != substitution.end())
            {
                result += it->second;
            }
            else
            {
                // Unknown letters shown with _
                result += '_';
            }
        }
        else
        {
            result += ch;
        }
    }

    return result;
}


// ------------------------------------------------------
// Required Function 5
//
// Display partially recovered plaintext
// ------------------------------------------------------

void display_partial_plaintext(
    const string &ciphertext,
    const map<char, char> &substitution
)
{
    cout << "\n==========================================\n";
    cout << "            PARTIAL PLAINTEXT\n";
    cout << "==========================================\n\n";

    string partial =
        apply_substitution(
            ciphertext,
            substitution
        );

    cout << partial << endl;

    cout << "\nCurrent substitutions:\n";

    if (substitution.empty())
    {
        cout << "No substitutions yet.\n";
    }

    for (auto item : substitution)
    {
        cout << item.first
             << " -> "
             << item.second
             << endl;
    }
}


// ------------------------------------------------------
// Required Function 6
//
// Verify by re-encrypting recovered plaintext
// ------------------------------------------------------

bool verify_solution(
    const string &plaintext,
    const string &ciphertext,
    const string &key
)
{
    string encryptedAgain =
        encryptMonoalphabetic(
            plaintext,
            key
        );

    return encryptedAgain == ciphertext;
}


// ------------------------------------------------------
// Interactive cryptanalysis
// ------------------------------------------------------

void cryptanalysis(
    const string &ciphertext,
    const string &plaintext,
    const string &encryptionKey
)
{
    map<char, char> substitution;

    while (true)
    {
        cout << "\n==========================================\n";
        cout << "       MONOALPHABETIC CRYPTANALYSIS\n";
        cout << "==========================================\n";

        cout << "\n1. Letter Frequency Analysis";
        cout << "\n2. Word Frequency Analysis";
        cout << "\n3. Pattern Analysis";
        cout << "\n4. Add Candidate Substitution";
        cout << "\n5. Remove Candidate Substitution";
        cout << "\n6. Display Partial Plaintext";
        cout << "\n7. Display Current Substitution Table";
        cout << "\n8. Verify Original Encryption";
        cout << "\n9. Exit";

        cout << "\n\nEnter choice: ";

        int choice;

        cin >> choice;

        if (choice == 1)
        {
            frequency_analysis(ciphertext);
        }

        else if (choice == 2)
        {
            word_frequency_analysis(ciphertext);
        }

        else if (choice == 3)
        {
            pattern_analysis(ciphertext);
        }

        else if (choice == 4)
        {
            char cipherLetter;
            char plainLetter;

            cout << "\nCiphertext letter: ";
            cin >> cipherLetter;

            cout << "Possible plaintext letter: ";
            cin >> plainLetter;

            if (cipherLetter >= 'a' &&
                cipherLetter <= 'z')
            {
                cipherLetter =
                    cipherLetter - 'a' + 'A';
            }

            if (plainLetter >= 'a' &&
                plainLetter <= 'z')
            {
                plainLetter =
                    plainLetter - 'a' + 'A';
            }

            bool conflict = false;

            for (auto item : substitution)
            {
                if (item.second == plainLetter &&
                    item.first != cipherLetter)
                {
                    cout << "\nWarning: plaintext letter "
                         << plainLetter
                         << " is already assigned to "
                         << item.first
                         << endl;

                    conflict = true;
                }
            }

            if (!conflict)
            {
                substitution[cipherLetter] =
                    plainLetter;

                cout << "\nSubstitution added: "
                     << cipherLetter
                     << " -> "
                     << plainLetter
                     << endl;

                display_partial_plaintext(
                    ciphertext,
                    substitution
                );
            }
        }

        else if (choice == 5)
        {
            char cipherLetter;

            cout << "\nEnter ciphertext letter to remove: ";

            cin >> cipherLetter;

            if (cipherLetter >= 'a' &&
                cipherLetter <= 'z')
            {
                cipherLetter =
                    cipherLetter - 'a' + 'A';
            }

            if (substitution.erase(cipherLetter))
            {
                cout << "Substitution removed.\n";
            }
            else
            {
                cout << "No substitution exists for "
                     << cipherLetter
                     << endl;
            }
        }

        else if (choice == 6)
        {
            display_partial_plaintext(
                ciphertext,
                substitution
            );
        }

        else if (choice == 7)
        {
            cout << "\nCipher -> Plain\n";
            cout << "---------------\n";

            for (auto item : substitution)
            {
                cout << item.first
                     << "      -> "
                     << item.second
                     << endl;
            }
        }

        else if (choice == 8)
        {
            if (verify_solution(
                    plaintext,
                    ciphertext,
                    encryptionKey))
            {
                cout << "\nVerification successful.\n";
                cout << "Re-encrypted plaintext is identical "
                     << "to ciphertext.\n";
            }
            else
            {
                cout << "\nVerification failed.\n";
            }
        }

        else if (choice == 9)
        {
            cout << "\nExiting cryptanalysis.\n";

            break;
        }

        else
        {
            cout << "\nInvalid choice.\n";
        }
    }
}


// ------------------------------------------------------
// Main
// ------------------------------------------------------

int main()
{
    /*
       Plain alphabet:

       ABCDEFGHIJKLMNOPQRSTUVWXYZ

       Encryption key:

       QWERTYUIOPASDFGHJKLZXCVBNM
    */

    string key =
        "QWERTYUIOPASDFGHJKLZXCVBNM";

    string plaintext =
        readFile("plaintext.txt");

    if (plaintext.empty())
    {
        cout << "plaintext.txt is empty "
             << "or could not be opened.\n";

        return 1;
    }

    cout << "\n==========================================\n";
    cout << "       MONOALPHABETIC SUBSTITUTION\n";
    cout << "==========================================\n";

    cout << "\nPlain Alphabet:\n";
    cout << "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n";

    cout << "\nEncryption Key:\n";
    cout << key << endl;

    string ciphertext =
        encryptMonoalphabetic(
            plaintext,
            key
        );

    writeFile(
        "ciphertext.txt",
        ciphertext
    );

    cout << "\nCiphertext generated successfully.\n";
    cout << "Saved to ciphertext.txt\n";

    cout << "\nCiphertext:\n\n";
    cout << ciphertext << endl;

    cryptanalysis(
        ciphertext,
        plaintext,
        key
    );

    return 0;
}