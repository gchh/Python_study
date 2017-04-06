def foo():
    m=1
    def bar():
        n=2
        return m+n
    m=bar()
    print(m)
foo()

def foo(arg1,arg2='test',arg3=100):
    print(arg1,arg2,arg3)
foo('where')
foo(arg1='where',arg2='what')
foo('where','what')

def gcd(m,n):
    r=m%n
    if r==0:
        return n
    else:
        r=m%n
        return gcd(n,r)
print(gcd(15,36))

def fib(n):
    f1,f2=0,1
    while f2<n:
        print(f2,)
        f1,f2=f2,f1+f2
fib(10)
