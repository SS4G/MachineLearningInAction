from math import log
import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter([1,2,3,4,5], [6,7,8,9,0])
# plt.show()
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.l=None
        self.r=None
a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")
e=Node("e")
f=Node("f")
g=Node("g")
a.l=b
a.r=c
b.l=d
b.r=e
c.l=f
c.r=g
import pickle
f=open("/home/mi/SS4G/dd.txt","wb")
x=pickle.dumps(a)
t=pickle.loads(x)
print(t.val)
print(t.l.val)#b
print(t.r.val)#c
print(t.l.l.val)#d
print(t.l.r.val)#e
print(t.l.r.val)#f
print(t.l.r.val)#g
"""
