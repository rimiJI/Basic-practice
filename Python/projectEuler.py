n=int(input())
prime_factor=[]
i=2
while i<=n:
    if n%i==0:
        prime_factor.append(i)
        n=n//i
    else:
        i+=1

if n > 1:
    prime_factor.append(n)

print(prime_factor)
print(max(prime_factor))




'''
2.
A,B,even_sum=1,2,0

while A<=4000000 :
    if A%2==0:
        even_sum+=A
    A,B=B,A+B

print(even_sum)



1.
sumlist=[]
sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sumlist.append(i)
        sum+=i

print("합:",sum)
print("배수리스트:",sumlist)
'''