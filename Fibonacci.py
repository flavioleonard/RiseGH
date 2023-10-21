N=int(input())
for i in range(N):
    x=int(input())
    
    calls=[]
    fibonacci=[]
    a=0
    b=1
    c1=2
    c2=4
    for j in range(x):
        #Fibonacci
        fibonacci.append(b)
        c=a+b
        a=b
        b=c

        #Calls
        if j>0:
            calls.append(c1)
            c3=c1+c2+2
            c1=c2
            c2=c3
        else:
            calls.append(1)
        

    result=a
    num_calls=calls[x-1]

    print("fib({}) = {} calls = {}".format(x,num_calls,result))