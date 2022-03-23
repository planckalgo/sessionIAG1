def max(lst):
    max=lst[0]
    for i in range(1,5):
        if(lst[i]>max):
            max=lst[i]
    print('Le plus grand élément  de cette liste a la valeur',max)
#Un exemple
lst=[0,10,15,12,9]
max(lst)
        
