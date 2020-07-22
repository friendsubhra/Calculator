e=2.718281228459045
pi=3.141592653589793
import math as m
def sum(*nums):
    res=0
    for i in nums:
        res+=i
    return res
def multiply(*nums):
    res=1
    for i in nums:
        res*=i
    return res
def pow(a,b):
    return a**b
def sqrroot(a):
    return a**0.5
def gcd(*nums):
    a=nums[0]
    for num in nums:
        a=m.gcd(a,num)
    return a
def lcm(*nums):
    a=1
    for num in nums:
        a=a*num/m.gcd(a,num)
    return a
def fact(n):
    return m.factorial(n)
def mod(x):
    if x<0:
        return -x
    return x
def sin_old(x):
    x=x-(x//(2*pi))*2*pi
    def f(x,n):
        d=2*n+1
        return x**d*(-1)**n/fact(d)
    a=0
    for i in range (0,10):
        a=a+f(x,i)
    return a
def sin(x):
    return m.sin(x)
def cos(x):
    return m.cos(x)
def tan(x):
    return m.tan(x)
def sec(x):
    return (cos(x))**(-1)
def cosec(x):
    return (sin(x))**(-1)
def cot(x):
    return (tan(x))**(-1)
def asin(x):
    return m.asin(x)
def acos(x):
    return m.acos(x)
def atan(x):
    return m.atan(x)
def asec(x):
    return m.acos(1/x)
def acosec(x):
    return m.asin(1/x)
def acot(x):
    return m.atan(1/x)
def sinh(x):
    return m.sinh(x)
def cosh(x):
    return m.cosh(x)
def tanh(x):
    return m.tanh(x)
def sech(x):
    return 1/m.cosh(x)
def cosech(x):
    return 1/m.sinh(x)
def coth(x):
    return 1/m.tanh(x)
def floor(x):
    if x<0:
        x-=1
    return int(x)
def ceil(x):
    return floor(x)+1
def derivative(formula,n):
    a = lambda x : eval(formula)
    h=0.0000000001
    der_n=(a(n+h)-a(n))/h
    return round(der_n,3)
def log_old(c0,base=e):
    i=0
    inc=1
    c=c0
    if c0<1:
        c=1/c0
    while True:
        if base**(i+inc)<=c:
            i+=inc
            if base**i==c:
                break
        else :
            inc/=10
        if mod(inc)<=10**-10:
            break
    if c0<1:
        i=-i
    return round(i,10)
def log(num,base=e):
    return m.log(num,base=base)
def area_tri(a,b=None,c=None):
    if b==None and c==None:
        b,c=a,a
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
def sgn(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0
def deg_to_rad(x):
    return x*pi/180
def rad_to_deg(x):
    return x*180/pi
def AM(*nums):
    total=len(nums)
    return sum(nums)/total
def GM(*nums):
    total=len(nums)
    res = multiply(nums)**(1/total)
    return res