def sum_of_proper_divisors(n): 
    divisors_sum = 0
    for i in range(1,  n):
        if n % i == 0 :
            divisors_sum += i
    return divisors_sum

def find_amicable_numbers(limit):
    amicable_numbers = []
    for a in range(1, limit):
        b = sum_of_proper_divisors(a)
        if b != a and sum_of_proper_divisors(b) == a:
            amicable_numbers.append(a)
    return amicable_numbers

limit = 10000
amicable_numbers = find_amicable_numbers(limit)
sum_of_amicable_numbers = sum(amicable_numbers)
print(sum_of_amicable_numbers)
