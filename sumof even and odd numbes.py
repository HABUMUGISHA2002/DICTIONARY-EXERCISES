def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    
    for i in numbers:
        if i % 2 == 0:  
            even_sum += i
        else:  
            odd_sum += i
            
    return (even_sum, odd_sum)


numbers = [1, 2, 3, 4, 5,6,7,8,9]
result = sum_even_odd(numbers)
print(result)  