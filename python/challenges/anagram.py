import random
import time

def anagramCheck(s, t):
    return not False in [s.count(letter) == t.count(letter) for letter in s]

def anagramASCII(s, t):
    codeS = [0] * 128
    codeT = [0] * 128
    if len(s) != len(t):
        return False
    if len(s) == 0 or len(t) == 0:
        return True
    
    for letter in s:
        codeS[ord(letter)] += 1
    for letter in t:
        codeT[ord(letter)] += 1

    return codeS == codeT

def anagramASCII2(s, t):
    return not False in [s.count(chr(x)) == t.count(chr(x)) for x in range(32,126) ]


def anagram(s, t):
    return sorted(s) == sorted(t)


N=10000000
s=''
for _ in range(N):
    s+= chr(random.randint(32,126))
#print(s)

#print('='*40)

idx=[x for x in range(N)]
random.shuffle(idx)
#print(idx)
t=[s[x] for x in idx]
tt=''.join(t)
#print(tt)

start = time.time()
#print(anagramCheck(s,tt))
#print(anagramASCII(s, tt))
print(anagramASCII2(s, tt))
#print(anagram(s,tt))

end = time.time()
print(end-start)