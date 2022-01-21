def factorial(i):
    for x in range(1,i):
        i*=x
    return i if i != 0 else 1
def pow(a, b):
    c = 1
    for _ in range(b):
        c *= a
    return c
def sqrt(n):
    if n < 0:
        raise ValueError("Cannot use negative numbers.")
    if n == 0:
        return 0
    x=1
    for _ in range(1,1001):
        x=x-((x**2-n)/(2*x))
    return x
def sqrt_2(n):
    if n < 0:
        raise ValueError("Cannot use negative numbers.")
    if n == 0:
        return 0
    m = 1
    for _ in range(1,1001):
        m = (m+float(n/m))*1.0/2.0
    return m
def sin(x):
    y, s = x,-1
    for i in range(3, 100,2):
        y+=s*(pow(x,i)/factorial(i))
        s *= -1
    return y
def cos(x):
    y, s = 1, -1
    for i in range(2,100,2):
        y+=s*(pow(x,i)/factorial(i))
        s *= -1
    return y
def sum(a):
    m=0
    for i in range(len(a)):
        m+=a[i]
    return m
e=sum([1/factorial(n) for n in range(101)]) #sum([1/factorial(1+n) for n in range(1,101)])+2
exp=lambda s:e**s
zeta=lambda s:sum([1/n**s for n in range(1, 10001)])
cos_old=lambda x:(sum([((-1)**n*(x**(2*n))/factorial(2*n)) for n in range(101)]))+x*10**-18
sin_new=lambda x:sum([((-1)**n/factorial(2*n+1))*(x**((2*n)+1)) for n in range(101)])
cos_new=lambda n:sum([((-1)**x*(n**(2*x))/factorial(2*x)) for x in range(101)])
tan=lambda x:(sin(x)/cos(x))
s_integral=lambda x,a,b:(x*b)-(x*a)
estimate_pi=lambda v=1000:sum([(-1)**n/(2*n+1) for n in range(v+1)])*4
ln_old=lambda z,a=10001:sum([(-1)**(k+1)*(z-1)**k/k for k in range(1,a)]) # 0 < z ≤ 2
ln=lambda z,a=10001:2*sum([(1/((2*k)+1))*(((z-1)/(z+1))**((2*k)+1)) for k in range(a)])
log=lambda x,a=None:ln(x) if a is None else ln(x)/ln(a)
sinh=lambda x:sum([x**((2*n)+1)/factorial(2*n+1) for n in range(1001)])
cosh=lambda x:sum([x**(2*n)/factorial(2*n) for n in range(1001)])
ceil=lambda n:-(-n//1)
floor=lambda n:n//1
new_cos=lambda x:sum([(((-1)**n*x**(2*n))/factorial(2*n)) for n in range(1001)])
arsinh=lambda x:ln(x+sqrt(x**2+1))
arcosh=lambda x:ln(x+sqrt(x**2-1)) # x ≥ 1
artanh=lambda x:0.5*ln((1+x)/(1-x)) # |x| < 1
arcoth=lambda x:0.5*ln((x+1)/(x-1)) # |x| > 1
arsech=lambda x:ln((1+sqrt(1-x**2))/x)# 0 < x ≤ 1 # ln((1/x)+sqrt((1/(x**2))-1))
arcsch=lambda x:ln((1/x)+sqrt((1/x**2)+1)) # x ≠ 0
log2=lambda x:log(x,2)
log10=lambda x:log(x,10)
