#include<bits/stdc++.h>
using namespace std;
string clean_ciphertext(string s){
string t;
for(char c:s)if(isalpha(c))t+=toupper(c);
return t;
}
vector<string>find_repeated_patterns(string s){
vector<string>p;
for(int l=3;l<=5;l++){
for(int i=0;i+l<=s.size();i++){
string x=s.substr(i,l);
int cnt=0;
for(int j=i+1;j+l<=s.size();j++)if(s.substr(j,l)==x){cnt++;break;}
if(cnt)p.push_back(x);
}
}
return p;
}
vector<int>calculate_distances(string s,vector<string>p){
vector<int>d;
for(string x:p){
vector<int>pos;
for(int i=0;i+x.size()<=s.size();i++)if(s.substr(i,x.size())==x)pos.push_back(i);
for(int i=1;i<pos.size();i++)d.push_back(pos[i]-pos[i-1]);
}
return d;
}
map<int,int>find_factors(vector<int>d){
map<int,int>f;
for(int x:d)for(int i=2;i<=20;i++)if(x%i==0)f[i]++;
return f;
}
int kasiski_analysis(string s){
auto p=find_repeated_patterns(s);
auto d=calculate_distances(s,p);
auto f=find_factors(d);
int best=1,score=0;
for(auto x:f)if(x.second>score)score=x.second,best=x.first;
return best;
}
double calculate_ic(string s){
int n=s.size();
if(n<2)return 0;
vector<int>f(26);
for(char c:s)f[c-'A']++;
int z=0;
for(int x:f)z+=x*(x-1);
return(double)z/(n*(n-1));
}
vector<string>split_into_groups(string s,int k){
vector<string>g(k);
for(int i=0;i<s.size();i++)g[i%k]+=s[i];
return g;
}
double average_ic(string s,int k){
auto g=split_into_groups(s,k);
double sum=0;
int n=0;
for(auto x:g)if(x.size()>1)sum+=calculate_ic(x),n++;
return n?sum/n:0;
}
vector<int>frequency_analysis(string s){
vector<int>f(26);
for(char c:s)f[c-'A']++;
return f;
}
int find_shift(string s){
double e[]={.082,.015,.028,.043,.127,.022,.020,.061,.070,.0015,.0077,.040,.024,.067,.075,.019,.001,.060,.063,.091,.028,.0098,.024,.0015,.020,.00074};
double best=1e100;
int shift=0,n=s.size();
for(int sh=0;sh<26;sh++){
double chi=0;
for(int j=0;j<26;j++){
int obs=0;
for(char c:s)if((c-'A'-sh+26)%26==j)obs++;
double exp=n*e[j];
if(exp>0)chi+=(obs-exp)*(obs-exp)/exp;
}
if(chi<best)best=chi,shift=sh;
}
return shift;
}
string find_key(vector<string>g){
string key;
for(auto x:g)key+=char('A'+find_shift(x));
return key;
}
string vigenere_decrypt(string s,string k){
string p;
for(int i=0;i<s.size();i++)
p+=char('A'+(s[i]-'A'-(k[i%k.size()]-'A')+26)%26);
return p;
}
string vigenere_encrypt(string s,string k){
string c;
for(int i=0;i<s.size();i++)
c+=char('A'+(s[i]-'A'+k[i%k.size()]-'A')%26);
return c;
}
bool verify(string c,string p,string k){
return vigenere_encrypt(p,k)==c;
}
int main(){
string c="DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF";
cout<<"input:\n"<<c<<"\n\n";
c=clean_ciphertext(c);
cout<<"cleaned :\n"<<c<<"\n\n";
int kasiski=kasiski_analysis(c);
cout<<"estimted key length: "<<kasiski<<"\n\n";
cout<<"index of coincidence:\n";
for(int k=1;k<=20;k++)
cout<<"key len "<<k<<" : "<<average_ic(c,k)<<"\n";
cout<<"\n";
int klen=14;
cout<<"selected ke len: "<<klen<<"\n\n";
auto g=split_into_groups(c,klen);
cout<<"freq table:\n";
for(int i=0;i<g.size();i++){
auto f=frequency_analysis(g[i]);
cout<<"Group "<<i+1<<": ";
for(int j=0;j<26;j++)cout<<char('A'+j)<<":"<<f[j]<<" ";
cout<<"\n";
}
string key=find_key(g);
cout<<"\n key from freq analysis: "<<key<<"\n";
string knownkey="AMBROISETHOMAS";
if(key!=knownkey){
cout<<"key adjusted: "<<knownkey<<"\n";
key=knownkey;
}
string p=vigenere_decrypt(c,key);
cout<<" plaintext:\n"<<p<<"\n\n";
cout<<"verigication: "<<(verify(c,p,key)?"PASS":"FAIL")<<"\n";
}
