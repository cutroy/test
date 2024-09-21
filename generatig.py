import random
a=[]
b=[]
check=[]
chek1=[]
c=[]
f=open('output.txt','w')
for i in range(100000):
    day = random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Wed'])
    time = random.choice(["0:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00","4:00-5:00","5:00-6:00","6:00-7:00","7:00-8:00","8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-13:00","13:00-14:00","14:00-15:00","15:00-16:00","16:00-17:00","17:00-18:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00","22:00-23:00"])
    if [day,time] not in a:
        a.append([day,time])
        t = random.randint(50,75)
        st_ans = f'{day},{time},{t}'
        f.write(st_ans)
        f.write('\n')
f.close()