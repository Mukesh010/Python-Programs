#Input string format = "KA51 ZZ9998"
string = input().strip()
N = int(input().strip())

S = string.split(" ")
Pre = S[0]
S = S[1]
Chars = S[:2]
Numbers = int(S[2:])


if((Numbers + N) <= 9999 ):
    print(Pre, Chars+str(Numbers+N))
else:
    K = Numbers+N
    Numbers = K % 10000
    if(Numbers < 10):
        Numbers = '000'+str(Numbers)
    elif(10 <= Numbers < 100):
        Numbers = '00'+str(Numbers)
    elif(100 <= Numbers < 1000):
        Numbers = '0'+str(Numbers)
    else:
        Numbers = str(Numbers)
    K = int(K/10000)
    if ((ord(Chars[1]) + K ) <= ord('Z') ):
        Char1 = chr(ord(Chars[1]) + K)
        Chars = Chars[0]+Char1
        print(Pre, Chars+Numbers)
    else:
        L = (ord(Chars[1]) + K) - ord('Z')
        if((ord(Chars[0]) + L ) > ord('Z')):
            print("invalid number")
        else:
            Char2 = chr(ord(Chars[0]) + L )
            Chars = Char2[0]+'Z'
            print(Pre, Chars+Numbers)