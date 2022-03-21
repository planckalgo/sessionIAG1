def triSelectin(liste):
    n= len(liste)
    for i in range (0,n-2):
        indexMin = i
        for j in range (i+1, n-1):
            if (liste(j)< liste(indexMin)):
                indexMin = j
        return liste
        if (indexMin== i):
          tmp = liste(i)
          liste(i)== liste(indexMin)
          liste(indexMin)== tmp
        return liste
