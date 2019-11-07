L=[]
for n in range(7):
    L.append(2**n)
X=5

if 2**X in L:
    print('at index',L.index(2**X))
         
else:
    print(X, 'not found')
