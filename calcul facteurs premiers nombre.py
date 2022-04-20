list = []
a = int(input('nombre?'))
c=2


while c<a:
    d=a/c
    if int(d)==d :
        list.append(c)
        a=d
    else:
        c=c+1
list.append(a)
print(list)
