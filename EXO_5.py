lst=[]
pairs=[]
impairs=[]
n=len(lst)
for i in range(0,n):
    if(lst[i]%2==0):
        pairs.append(lst[i])
    else:
        impairs.append(lst[i])
print('Liste pair',pairs)
print('Liste impair',impairs)
#Vous n'avez plus qu'a remplir lst
