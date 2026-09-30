from collections import Counter
def generate_key_matrix(keyword):
    keyword=keyword.upper().replace("J","I")
    chars=[]
    for c in keyword:
        if c.isalpha() and c not in chars:
            chars.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in chars:
            chars.append(c)
    return [chars[i:i+5] for i in range(0,25,5)]
def prepare_plaintext(text):
    text="".join(c for c in text.upper() if c.isalpha()).replace("J","I")
    return text
def create_digraphs(text):
    digraphs=[]
    i=0
    while i<len(text):
        a=text[i]
        if i+1>=len(text):
            digraphs.append(a+"X")
            i+=1
        elif text[i+1]==a:
            digraphs.append(a+"X")
            i+=1
        else:
            digraphs.append(a+text[i+1])
            i+=2
    return digraphs
def find_position(matrix,char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c]==char:
                return r,c
def playfair_encrypt(digraphs,matrix):
    result=""
    for pair in digraphs:
        r1,c1=find_position(matrix,pair[0])
        r2,c2=find_position(matrix,pair[1])
        if r1==r2:
            result+=matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]
        elif c1==c2:
            result+=matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]
        else:
            result+=matrix[r1][c2]+matrix[r2][c1]
    return result
def playfair_decrypt(ciphertext,matrix):
    result=""
    for i in range(0,len(ciphertext),2):
        a,b=ciphertext[i],ciphertext[i+1]
        r1,c1=find_position(matrix,a)
        r2,c2=find_position(matrix,b)
        if r1==r2:
            result+=matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]
        elif c1==c2:
            result+=matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]
        else:
            result+=matrix[r1][c2]+matrix[r2][c1]
    return result
def digraph_frequency(ciphertext):
    return Counter(ciphertext[i:i+2] for i in range(0,len(ciphertext),2))
def verify(prepared,decrypted):
    if len(decrypted)==len(prepared)+1 and decrypted.endswith("X"):
        decrypted=decrypted[:-1]
    return prepared==decrypted
keyword=input("Keyword: ")
plaintext=input("Plaintext: ")
matrix=generate_key_matrix(keyword)
prepared=prepare_plaintext(plaintext)
digraphs=create_digraphs(prepared)
ciphertext=playfair_encrypt(digraphs,matrix)
decrypted=playfair_decrypt(ciphertext,matrix)
frequency=digraph_frequency(ciphertext)
print("\nKey Matrix")
for row in matrix:
    print(" ".join(row))
print("\nPrepared Digraphs:")
print(" ".join(digraphs))
print("\nCiphertext:")
print(ciphertext)
print("\nDecrypted Text:")
print(decrypted)
print("\nDigraph Frequency:")
for pair,count in frequency.items():
    print(pair+":",count)
print("\nVerification:")
print("SUCCESS" if verify(prepared,decrypted) else "FAILED")

