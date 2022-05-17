import pandas as pd
import os

counter = 0
sums=0
target = []
for i in range(100) :
    print(i)
    if counter <= 33 :
        target.append(0)
        sums +=1

    elif counter > 33 and counter < 67:
        target.append(1)
        sums +=1
    else :
        target.append(2)
        sums +=1
    counter += 1


print(target)

df = pd.DataFrame([target])

print(df.iloc[:,:])
print(sums)
df.to_csv('target.csv')
