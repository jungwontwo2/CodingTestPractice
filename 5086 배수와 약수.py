while True:
    x,y=map(int,input().split())
    if(x==0 and y==0):
        break
    switch = False
    if(x>y):
        for i in range(1,x):
            if(y*i==x):
                print("multiple")
                switch=True
    if(y>x):
        switch=False
        for i in range(1,y):
            if(x*i==y):
                print("factor")
                switch=True
    if (switch == False):
        print("neither")