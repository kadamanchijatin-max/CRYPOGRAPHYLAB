#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
using namespace std;

string plaintext;
string ciphertext;
string recoveredPlaintext;
char encryptionKey[26];
char recoveredKey[26];

void apply_substitution(string text,char key[],string &result){
    result="";
    for(int i=0;i<text.length();i++){
        char ch=text[i];
        if(isalpha(ch)){
            bool upper=isupper(ch);
            char c=toupper(ch);
            char newChar=key[c-'A'];
            if(upper)
                result+=newChar;
            else
                result+=tolower(newChar);
        }
        else
            result+=ch;
    }
}

void frequency_analysis(){
    int frequency[26]={0};
    int totalLetters=0;

    for(int i=0;i<ciphertext.length();i++){
        char ch=ciphertext[i];
        if(isalpha(ch)){
            ch=toupper(ch);
            frequency[ch-'A']++;
            totalLetters++;
        }
    }

    vector<pair<char,int>> data;

    for(int i=0;i<26;i++)
        data.push_back({char('A'+i),frequency[i]});

    sort(data.begin(),data.end(),[](pair<char,int>a,pair<char,int>b){
        return a.second>b.second;
    });

    cout<<"\n===== FREQUENCY ANALYSIS =====\n\n";
    cout<<"Letter\tFrequency\tPercentage\n";

    for(int i=0;i<26;i++){
        double percentage=0;
        if(totalLetters>0)
            percentage=(double)data[i].second/totalLetters*100;

        cout<<data[i].first<<"\t"<<data[i].second<<"\t\t"<<percentage<<"%\n";
    }

    cout<<"\nMost frequent letters:\n";

    for(int i=0;i<5;i++){
        if(data[i].second>0)
            cout<<data[i].first<<" ";
    }

    cout<<"\n";
}

vector<string> getWords(string text){
    vector<string> words;
    string word="";

    for(int i=0;i<=text.length();i++){
        if(i<text.length()&&isalpha(text[i]))
            word+=toupper(text[i]);
        else{
            if(word.length()>0){
                words.push_back(word);
                word="";
            }
        }
    }

    return words;
}

void word_frequency_analysis(){
    vector<string> words=getWords(ciphertext);
    map<string,int> frequency;

    for(int i=0;i<words.size();i++)
        frequency[words[i]]++;

    cout<<"\n===== WORD FREQUENCY ANALYSIS =====\n";

    cout<<"\nOne-letter words:\n";
    for(auto x:frequency)
        if(x.first.length()==1)
            cout<<x.first<<" ("<<x.second<<")\n";

    cout<<"\nTwo-letter words:\n";
    for(auto x:frequency)
        if(x.first.length()==2)
            cout<<x.first<<" ("<<x.second<<")\n";

    cout<<"\nThree-letter words:\n";
    for(auto x:frequency)
        if(x.first.length()==3)
            cout<<x.first<<" ("<<x.second<<")\n";

    cout<<"\nRepeated words:\n";
    for(auto x:frequency)
        if(x.second>1)
            cout<<x.first<<" ("<<x.second<<" times)\n";
}

string getPattern(string word){
    map<char,int> patternMap;
    string pattern="";
    int number=1;

    for(int i=0;i<word.length();i++){
        char ch=word[i];

        if(patternMap.find(ch)==patternMap.end()){
            patternMap[ch]=number;
            number++;
        }

        pattern+=to_string(patternMap[ch]);

        if(i!=word.length()-1)
            pattern+="-";
    }

    return pattern;
}

void pattern_analysis(){
    vector<string> words=getWords(ciphertext);
    map<string,vector<string>> patterns;

    for(int i=0;i<words.size();i++){
        string pattern=getPattern(words[i]);
        patterns[pattern].push_back(words[i]);
    }

    cout<<"\n===== PATTERN ANALYSIS =====\n";
    cout<<"\nRepeated letter patterns:\n";

    for(auto x:patterns){
        if(x.second.size()>1){
            cout<<"Pattern "<<x.first<<": ";

            for(int i=0;i<x.second.size();i++)
                cout<<x.second[i]<<" ";

            cout<<"\n";
        }
    }

    cout<<"\nIndividual word patterns:\n";

    for(int i=0;i<words.size();i++)
        cout<<words[i]<<" -> "<<getPattern(words[i])<<"\n";
}

void display_partial_plaintext(){
    string partialText="";
    apply_substitution(ciphertext,recoveredKey,partialText);

    cout<<"\n===== PARTIAL PLAINTEXT =====\n\n";
    cout<<partialText<<"\n";
}

void show_recovered_key(){
    cout<<"\n===== RECOVERED SUBSTITUTION KEY =====\n\n";

    cout<<"Cipher : ";
    for(int i=0;i<26;i++)
        cout<<char('A'+i)<<" ";

    cout<<"\nPlain  : ";

    for(int i=0;i<26;i++)
        cout<<recoveredKey[i]<<" ";

    cout<<"\n";
}

bool verify_recovered_key(){
    string testCiphertext;
    char reverseKey[26];

    for(int i=0;i<26;i++)
        reverseKey[i]='_';

    for(int i=0;i<26;i++){
        if(recoveredKey[i]!='_'){
            char plain=recoveredKey[i];
            char cipher='A'+i;
            reverseKey[plain-'A']=cipher;
        }
    }

    apply_substitution(recoveredPlaintext,reverseKey,testCiphertext);

    return testCiphertext==ciphertext;
}

bool verify_solution(){
    string result="";
    apply_substitution(plaintext,encryptionKey,result);

    if(result==ciphertext)
        return true;

    return false;
}

void initialize_keys(){
    for(int i=0;i<26;i++){
        encryptionKey[i]='A'+i;
        recoveredKey[i]='_';
    }
}

void cryptanalysis(){
    while(true){
        cout<<"\n===== CRYPTANALYSIS =====\n";
        cout<<"1. Test substitution\n";
        cout<<"2. Display partial plaintext\n";
        cout<<"3. Display recovered key\n";
        cout<<"4. Finish cryptanalysis\n";
        cout<<"Enter choice: ";

        int choice;
        cin>>choice;

        if(choice==1){
            char cipherLetter;
            char plainLetter;

            cout<<"Enter ciphertext letter: ";
            cin>>cipherLetter;

            cout<<"Enter suspected plaintext letter: ";
            cin>>plainLetter;

            cipherLetter=toupper(cipherLetter);
            plainLetter=toupper(plainLetter);

            if(cipherLetter>='A'&&cipherLetter<='Z'&&plainLetter>='A'&&plainLetter<='Z'){
                recoveredKey[cipherLetter-'A']=plainLetter;

                cout<<"\nSubstitution tested: "<<cipherLetter<<" -> "<<plainLetter<<"\n";

                display_partial_plaintext();
            }
            else
                cout<<"Invalid letters.\n";
        }
        else if(choice==2)
            display_partial_plaintext();
        else if(choice==3)
            show_recovered_key();
        else if(choice==4)
            break;
        else
            cout<<"Invalid choice.\n";
    }
}

int main(){
    initialize_keys();

    ifstream inputFile("plaintext.txt");

    if(!inputFile){
        cout<<"Error: plaintext.txt not found.\n";
        return 1;
    }

    string line;

    while(getline(inputFile,line)){
        plaintext+=line;
        plaintext+="\n";
    }

    inputFile.close();

    cout<<"===== MONOALPHABETIC SUBSTITUTION CIPHER =====\n";
    cout<<"\nPlaintext loaded successfully.\n";

    cout<<"\nEnter 26-letter substitution key.\n";
    cout<<"Example: QWERTYUIOPASDFGHJKLZXCVBNM\n";
    cout<<"Key: ";

    string key;
    cin>>key;

    if(key.length()!=26){
        cout<<"Error: Key must contain exactly 26 letters.\n";
        return 1;
    }

    for(int i=0;i<26;i++)
        encryptionKey[i]=toupper(key[i]);

    apply_substitution(plaintext,encryptionKey,ciphertext);

    ofstream outputFile("ciphertext.txt");

    if(!outputFile){
        cout<<"Error creating ciphertext.txt.\n";
        return 1;
    }

    outputFile<<ciphertext;
    outputFile.close();

    cout<<"\n===== CIPHERTEXT =====\n\n";
    cout<<ciphertext<<"\n";

    frequency_analysis();
    word_frequency_analysis();
    pattern_analysis();

    cryptanalysis();

    show_recovered_key();

    apply_substitution(ciphertext,recoveredKey,recoveredPlaintext);

    cout<<"\n===== RECOVERED PLAINTEXT =====\n\n";
    cout<<recoveredPlaintext<<"\n";

    cout<<"\n===== VERIFICATION =====\n";

    if(verify_recovered_key())
        cout<<"Recovered key verification successful.\n";
    else
        cout<<"Recovered key verification failed.\n";

    if(verify_solution())
        cout<<"Original encryption verification successful.\n";
    else
        cout<<"Original encryption verification failed.\n";

    return 0;
}
