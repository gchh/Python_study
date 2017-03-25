x=float(input())
y=abs(x)
if y>=1:
    low=0
    high=y
    guess=(low+high)/2

    while abs(guess**2-y)>1e-5:
        if guess**2<y:
            low=guess
        else:
            high=guess
        guess=(low+high)/2
else:
    low=y
    high=1
    guess=(low+high)/2

    while abs(guess**2-y)>1e-5:
        if guess**2>y:
            high=guess
        else:
            low=guess
        guess=(low+high)/2
if x>=0:
    print('The root of %f is: ±%f'%(x,guess))
else:
    print('The root of %f is: ±%fi'%(x,guess))
