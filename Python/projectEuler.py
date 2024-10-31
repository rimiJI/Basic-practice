sumlist=[]
sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sumlist.append(i)
        sum+=i

print("합:",sum)
print("배수리스트:",sumlist)
