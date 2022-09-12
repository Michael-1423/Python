Str1 = '''Welcome Sir!!
My name is Jarvis
How may I help you ?'''
print(Str1)
print('Open Official or Guest?')
print('1.Official')
print('2.Guest')
choice = input('Enter Your Choice (1or2)\n')
if choice == '1' :
     name = input('Enter Your Name\n')
     if name == 'Jatin' :
      def password () :
       password = input('Enter Password\n')
       if password == 'abc' :
         print('Welcome Jatin sir')
         i = 0
         while i <10 :
              r=r1=r2=r3=0
              x = input('enter a number:\n')
              y = input('ener another nuber\n')
              z = input('you want to add(1), subtract(2) , multiply(3) or divide(4)?\n')
              if z == '1' :
                   r = int(x) + int(y)
                   print('sum of x and y is',r)
                   
              elif z == '2' :
                   r1 = int(x)-int(y)
                   print('difference of x and y is ',r)
              elif z == '3' :
                   r2 = int(x)*int(y)
                   print('product of x and y is ',r)
              elif z == '4' :
                   r3 = int(x)/int(y)
                   print('dquetionet of x and y is ',r)     
       else :
         print('Access Denied')  
      password ()
     else :
      print('Access Denied') 
elif choice == '2' :
    Guest= input('Please Enter Your Name\n')
    print('Welcome sir',Guest)
    for a in [1,2,3,4,5,6,7,8,9,10]:
         print(a)
         print(a,'*2=',a*2)
    import random
    m= -3268778
    while m <0 :
     number = random.randint(1,10)
     ctr = 0
     while ctr < 5 :
         guess = int(input('Guess a number in range 1 - 10 :' ))
         if guess == number :
              print('You Win!!')

              break
         elif guess==number+2 :
              
              print('you are close')
         elif guess==number-2 :
              
              print('you are close')     
         else :
              ctr+=1
         if not ctr<5 :
              print('you lose. The number was',number)
              print('Let us Play again.')
              end = input('Do you want to exit press 1 \n')
              if end == '1' :
                 break
    m+=1
       
