def max(list):
    max =list[0]
    for i in range(1,10):
        if(list[i]> max):
            max =list[i]
            print("le plus grand élément est",max)
            #list des éléments
            list =[1,2,3,4,5,6,7,8,9,10]
            max(list)
