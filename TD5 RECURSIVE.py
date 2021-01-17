#####EXERCICE 1
"1e question"
def trie(L):
    n=len(L)
    for i in range(0,n-2):
        if L[i]>L[i+1]:
           return("nope")
    return("YES")

"2e question"
def trierec(L):
    if len(L)==1:
       return("yep")
    if len(L)==2:
       if L[0]>L[1]:
          return("nope")
       else:
            L.remove(L[0])
            return(trierec(L))
    if len(L)==3:
        if L[0]>L[1] or L[1]>L[2]:
           return("nope")
        else:
            L.remove(L[0])
            return(trierec(L))

    else:
        if L[0]>L[1]:
           L.remove(L[0])
           return(trierec(L))

"ou correction"
def trirec(L):
    if len(L)==1:
        return(True)
    else:
        if L[0]>L[1]:
            return(False)
        else:
            trirec(L[1:])

######EXO4
"1E QUESTION"
"1)b)"
def sommerec(L):
    len(L)==2
    if L[0]==1 or L[1]==1:
        return(L[0]+L[1])
    else:
        L[0]=l[0]-1
        L[1]=L[1]+1
        return(sommerec(L))

"1)a)"

def somme(L):
    len(L)==2
    while L[0]>1 and L[1]>1:
          L[0]=L[0]-1;L[1]=L[1]+1
    return(L[0]+L[1])


"2e question"
def carre(n):
    if n==1:
        return(1)
    else:
        return(carre(n-1)+2*(n-1))

    "ou utiliser sum(sum(carre(n-1),n),n)-1"






