b=int(input())
a=0


def add_numbers(b):
    a=0
    for i in range(b):
        a +=i    
        return a
    
print (add_numbers(b))