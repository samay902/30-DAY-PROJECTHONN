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