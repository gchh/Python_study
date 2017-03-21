x=float(input())
low=0
high=x
guess=(low+high)/2

while abs(guess**2-x)>1e-5:
    if guess**2<x:
        low=guess
    else:
        high=guess
    guess=(low+high)/2
print('The root of %f is: %f'%(x,guess))
