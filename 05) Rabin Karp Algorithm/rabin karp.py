index = []

pattern = print("Entre the array that you want to search through: ")                              
text = print("Entre the text that you want to search: ")   

m = len(pattern) 
n = len(text)
char = 256                                                                  #total ASCII characters
prime = 101                                                                 #range of ASCII number (hash values)
h = 1 

for i in range(m - 1):                                                      #if index pointer is within the range of length of pattern - 1
    h = (h * char) % prime                                                  #hash formula defined

a = 0                                                                       #hash value of pattern
b = 0                                                                       #hash vlue of text

for i in range(m):                                                          #for when index pointer is within length of pattern
    a = (char * a + ord(pattern[i])) % prime                                #convert letter into ASCII number and calculate hash
    b = (char * b + ord(text[i])) % prime                                   #convert letter into ASCII number and calculate hash

for i in range(n - m + 1):                                                  #for when index pointer is length of text - (length of pattern + 1)
    if a == b:                                                              #compare both hash values
        if text[i:i+m] == pattern:                                          #if no collision
            index.append(i)                                                 #saving starting point in index

if a < n - m:                                                               #if hash value of pattern < length of pattern - length of text
    b = (char * (b - ord(text[i]) * h) + ord(text[i + m])) % prime          #subtract, shift and add

if b < 0:                                                                   #if hash value of text < 0 (negative hash value)
    b = b + prime                                                           #make hash value positive 