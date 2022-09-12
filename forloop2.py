for i in range(0,5) :
    for j in range(0,i+1) :
        print('$', end = " ")
    print()    
#----------------------------------------------------


k = 8
for i in range(0,5) :
    for j in range(0,k) :
        print(end = " ")
    k-=2
    for j in range(0,i+1) :
        print('$' , end = ' ')
    print()
#-----------------------------------------------------

k = 8
for i in range(0,5) :
    for j in range(0,k) :
        print(end = " ")
    k-=1
    for j in range(0,i+1) :
        print('$' , end = ' ')
    print()
#-----------------------------------------------------

k = 8
for i in range(0,5) :
    for j in range(0,k) :
        print(end = " ")
    k-=1
    for j in range(0,i+1) :
        print('$' , end = ' ')
    print()        
k = 5

for i in range(5,0,-1) :
    for j in range(k,0,-1) :
        print(end = " ")
    k+=1
    for j in range(0,i-1) :
        print('$' , end = ' ')
    print()   
#---------------------------------------------------------


for i in range(0,5) :
    for j in range(0,i+1) :
        print('$', end = " ")
    print()
for i in range(5,0,-1):
    for j in range(0,i-1):
             print('$', end = " ")
    print()
#---------------------------------------------------------


k = 5
for i in range(5,0,-1) :
    for j in range(k,0,-1) :
        print(end = " ")
    k+=1
    for j in range(0,i-1) :
        print('$' , end = ' ')
    print()       

#------------------------------------------------------------------

for i in range(5,0,-1):
    for j in range(0,i-1):
             print('$', end = " ")
    print()    
