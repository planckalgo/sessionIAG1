######## Mahamat souradjadine djibraïl.py
# exercice2
n = int(input("donnez la valeur de n"))
print("voici la table de multiplication de ",n)
for i in range(1,21):
	print(i,"x",n,"=",i*n)
	
	
# exercice 5
def extract(L):
	pair = [ ]
	impair = [ ]
	for x in L:
		if (x%2 == 0):
			pair.append(x)
		else:
			impair.append(x)	
	print(" la liste des entiers pairs est " ,pair)
	print(" la liste des entiers impairs est " ,impair)				
# tester l'algorithme
L =[13,10,7,18,19,76,44,32,15,81,23]
print(extract(L))


# exercice3
print('entrez la temperature')
tmpf = int( )
tmpc = float( tmpf)

tmpc = (tmpf - 36) / 1.8
print('la valeur de la temperature en degre celsus est : ' , tmpc)


# exercice6
def max(list):
	max = list[0]
	for i in range(1,10):
			if (list[i]> max):
				max=list[i]
	print("le plus grand element est:",max)
# liste des elements
list =[1,2,3,4,5,6,7,8,9,10]				
max(list)

### session

# exo2
  for i in range(a,b):
  	      if (a<0 and b>1):     
  	        a=float(input())  
  	             b=float(input())  
  	                 return false
  	                   else: 
  	                        return true
  	                        
# EXO3
Mahamat Souradjadine Djibraïl
Hv=21
Mv=50
Hv=4
Mv=20
Hv= float (input("entrer les heures"))
Mv= float (input ("entrer les minutes"))
if (Hv>heures and Mv>minutes):  
    print('entrer la valeur Hd:21')
    elif (Mv>minutes and not Hv>heures):      print('entrer la valeur Md:5')
    elif (Hv<heures and not Mv<minutes):      
print('entrer la valeur Hv:6')
    elif (Mv<minutes and not Hv<heures):     
 print('entrer la valeur Mv:30')
    else:     
     print('la valeur Hv et Mv:"4"20')
     

# EXO5
Mahamat Souradjadine Djibraïl
liste_nombre=()
print("entrer un nombre")
N= int(input())for i in range(0,20):  
  if (list(i)<0 and list(i)>20):    
   print("plus grand")  
      else:  
         print ("plus petit")
         
# Exo6
Mahamat Souradjadine Djibraïl 
def min(lst):    
min=lst(0) 
   for i in range(1,8):       
    if(lst(i)<min):      
          min=lst(i)   
           print('le plus petit element de cette liste a la valeur',min)   
            lst=(64,34,25,12,22,11,20,90)  
              min(lst)
              
              
# Exo4
Mahamat souradjadine Djibraïl
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
