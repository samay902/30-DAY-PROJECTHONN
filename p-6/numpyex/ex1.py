import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3]])
print(b.ndim)
c=np.zeros([3,3])
print(c.ndim)
d=np.full((3,3),2)
print(d)
print(d.ndim)
e=d**2
print(e)
f=np.eye(5,5)
print(f)
g=np.linspace(0,1,10)
print(g)
h=np.logspace(0,2,5)
print(h)
i=np.random.randint(10,24+1,size=(3,3))
print(i)
j=np.random.choice([0,1],10)
print(j)


def multiplier(a):
    a*=3
    a+=a
    a%=2
    return a
a=np.array([1,2,3,4])
print(multiplier(a))

    
