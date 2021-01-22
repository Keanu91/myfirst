fibb=[0,1]
for i in range(1000):
    fibb.append(fibb[i]+fibb[i+1])
print(fibb)
