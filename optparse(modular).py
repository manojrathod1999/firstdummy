import argparse
def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
if __name__ == "__main__":
    parser =argparse.ArgumentParser(description='simple calculator')
    parser.add_argument('-n1',"--number1",type=float,help="enter the first number to operate")
    parser.add_argument('-n2',"--number2",type=float,help="enter the second number to operate")
    parser.add_argument('-o','--operation',help="arthematic operation like add,mul,sub,div")
    args = parser.parse_args()
    print("print",args.number1)
    print("number2")
    print("operation")


    x=args.number1
    y=args.number2
    ans=None
    if args.operation=="add":
        ans=add(x,y)

    elif args.operation=="sub":
        ans = sub(x,y)

    elif args.operation=="mul":
        ans=mul(x,y)
    elif args.operation=="div":
        ans=div(x,y)

    else:
        print("Invalid input")
    print("result: ",ans)