a=[0,1,2,3,4,5]
print(id(a),id(a[:3]))
p=a[:2]
p.extend(a[3:])
print(p)