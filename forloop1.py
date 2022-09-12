
l = ['A','B','C','D','E']
m = len(l)
for i in range(0,m) :
    for j in range(0,i+1):
        print(l[i],end=' ')
    print()    
#-------------------------------------------
for i in range(0,5):
    num = 1

    for j in range(0,i+1) :
        print(num, end = ' ')
        num+=1
    print()
#------------------------------------------------


num = 1
for i in range(0,5):
    for j in range(0,i+1) :
        print(num, end = ' ')
        num+=1
    print()
#---------------------------------------------------------

num = 65
for i in range(0,5) :
    for j in range(0,i+1):
        ch = chr(num)
        print(ch, end = ' ')
        num+=1
    print()    

#------------------------------------------------------------------

num = 65
for i in range(0,5) :
    num = 65
    for j in range(0,i+1):
        ch = chr(num)
        print(ch, end = ' ')
        num+=1
    print()    
#---------------------------------------------------------------------

for i in range(0,5):
    num=5
    for j in range(i+1,0,-1) :
        print(num, end = ' ')
        num-=1
    print()

#----------------------------------------------------------------------------

num = 15
for i in range(0,5):
    for j in range(i+1,0,-1) :
        print(num, end = ' ')
        num-=1
    print()
#---------------------------------------------------------------------------    
    
num = 79
for i in range(0,5) :
    for j in range(i+1,0,-1):
        ch = chr(num)
        print(ch, end = ' ')
        num-=1
    print()

#-------------------------------------------------------------------------    
num = 69
for i in range(0,5) :
    num = 69
    for j in range(i+1,0,-1):
        ch = chr(num)
        print(ch, end = ' ')
        num-=1
    print()    
