#lambda functions
a = lambda c : c+5
print(a(8))

b = lambda c,d : c+d
print(b(8,6))

e = lambda c,d :c if  (c>d) else d
print(e(8,6))

q = lambda p : p*p
print(q(5))

#maping
lst = [1,2,3,4,5,6,7,8]
f=list(map(lambda x : x+5,lst))
print(f)

#FILTER
lst = [1,2,3,4,5,6,7,8]
k=list(filter(lambda v : v%2,lst))
print(k)

lst = [1,2,3,4,5,6,7,8]
k=list(filter(lambda v : v>7,lst))
print(k)

#reduce
lst=[1,2,3,4,5,6,7,8,9]
from functools import reduce
p=reduce(lambda v,d : v+d,lst)
print(p)
