import random
f=open('hoursoutput.txt','w')
for i in range(0,23):
    s = f'"{i}:00-{i+1}:00",'
    f.write(s)
f.close()