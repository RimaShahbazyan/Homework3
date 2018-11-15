def is_prime(num):
    a=0
    for i in range(2, num-1) :
        if (num%i==0):
            return False  
    return True

num=int(input() ) 
     
for i in range(2, num):
    if is_prime(i):
        print(i,  end=' ')
