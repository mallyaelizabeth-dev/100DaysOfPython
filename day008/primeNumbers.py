def prime_numbers(number):
    is_prime = True
    num_interval = range(2, number)
    
    for num in num_interval:
        if number % num == 0:
            is_prime = False
            break # exit the loop early if a divisor is found
    if is_prime:
        print(f"{number} It's a prime number")
    else:    
        print(f"{number} It's not a prime number.")
        
n =  int(input("Write your test no bt 2-100: "))    
if n<2 or n>100:
    print("Please enter a valid number in the specified range!")
    
prime_numbers(n)