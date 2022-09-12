s = open(r"E:\all notes\j.txt" , "r" , encoding = "utf8")
a=s.readlines()

print("Lines removed are:")

y = len(a)

t = open(r"E:\all notes\new1.txt" , "a" , encoding = "utf8")
b = []
b=a


for i in a:


    if i[0]=="A" :
        
        print(i)
        t.writelines(i)
        b.pop(a.index(i))
    elif  i[0] == "a":
        print(i)
        t.writelines(i)
        b.pop(a.index(i))


    else:
        continue


s1 = open(r"E:\all notes\j.txt" , "w" , encoding = "utf8")
s1.writelines(b)



t.flush()
s1.flush()

t.close()
s.close()
s1.close()
