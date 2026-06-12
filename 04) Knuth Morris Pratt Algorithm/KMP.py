#lps means longest preffix that also works as a suffix

index = []
i = []                                           #pointer to navigate index

lps = [0]                                        #array of zeros

pattern = print("Entre the array that you want to search through: ")                              
text = print("Entre the text that you want to search: ")   

n = len(pattern)                                 #length pattern to be searched in
m = len(text)                                    #length pattern to be searched for 
                                 

def compute_lps(pattern):
    lps = [0] * len(pattern)                     #array of zeros that is the length of the pattern
    length = 0                                   #length of previous longest preffix which is 0 because we are at the start of the pattern
    i = 1                                        #pointer scanning through pattern (starting from index 1)

    while i < len(pattern):
        if pattern[i] == pattern[length]:        #pattern repeating until suffix matches prefix
            length += 1                          #length extended
            lps[i] = length                      #length stored
            i += 1                               #pointer moved forward

    else:
        if length != 0:                          #if length is not 0
            length = lps[length - 1]             #check previous element
        else:                                    #if length is 0
            lps[i] = 0                           #stored length is set as 0
            i += 1                               #pointer moved forward

a = 0                                            #pointer for text (only moving left to right) (no backward movement allowed)
b = 0                                            #pointer for pattern

#if pattern matches

if pattern[b] == text[a]:
    a += 1                                       #text pointer moved forward
    b += 1                                       #pattern pointer moved forward

#if pattern matches completely 

elif b == m:                                     #pattern pointer reaches the end of the entered pattern
    index.append(a - b)                          #calculate index
    b = lps[b - 1]                               #check if end of pattern can be starting point of next match

#if pattern does not match

elif a < n and pattern [b] != text[a]:           #pattern does not match text
    if b != 0:                                   #if pattern pointer is not 0
        b = lps[b - 1]                           #pattern pointer moved forward and index pointer not moved
    else:                                        #if pattern pointer is 0
        i += 1                                   #index pointer moved forward 