def is_prime_number(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def get_prime_numbers(start, stop):
    prime_numbers=[]
    for i in range(start,stop+1): 
        if is_prime_number(i):
            prime_numbers.append(i)
    return prime_numbers        
    

print(get_prime_numbers(1,100))