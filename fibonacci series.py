num = int (input("\n enter the range: "))
p = int(input("enter 0 for even 1 for odd"))
i=0;x=0;y=1
while(i<num):
        if(i>1):
                k=x+y
                y=k
                x=y
        else:
                k=i
        if p%2 == 0:
                print("fibonacci series: ",k)
        i=i+1
        p+=1
