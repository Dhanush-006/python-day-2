a=int(input("no of sentence"))
count=1
b=[ ]
while a>=1:
    i=str(input("enter a string"))
    for j in i:
        if j==" ":
            count=count+1
        print(count)
        b.append(count)
        a=a-1
        count=count-count-count+1
        print(b)
d=max(b)
print(b)
