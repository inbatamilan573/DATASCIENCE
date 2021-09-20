def minion_game(s):
    # your code goes here
    vow='AEIOU'
    k=0
    m=0
    for i in range(len(s)):
        if s[i] in vow:
            k+=len(s[i:])
        else:
            m+=len(s[i:])
    
    if m  > k:
        print("Stuart"+" "+str(m))
    elif k>m:
        print("Kevin"+" "+str(k))
    else:
        print("Draw")
                 
        
        
s=input("enter: ")
minion_game(s)