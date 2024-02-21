def power(x,y):
    result = 1 
    for _ in range(y):
        result *= x
    return result
x = 5
y = 3
print(power(x,y))
#output should be 125
#successfully ran in terminal


def min_max(numbers):
    return min(numbers), max(numbers)
numbers = [55, 6, 14, 68, 7, 8]
result = min_max(numbers)
print("minimum value:", result[0])
print("maximum value:", result [1])
#output should have min=6 and max=68
#successfully ran in terminal


def is_it_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = 2024
print(is_it_leap_year(year))
#output should be True
#successfully ran in terminal


def calculate_bmi(weight_kg, height_m):
    if height_m == 0:
        return "Error: Height cannot be zero"
    bmi = weight_kg / (height_m ** 2)
    return bmi
weight = 68 
height = 1.5 
bmi = calculate_bmi(weight, height)
print("BMI:", bmi)
#output should be 30.2
#successfully ran in terminal


def rotate_digits(n):
    last_digit = n % 10
    rotated_n = last_digit * (10 ** (len(str(n)) - 1)) + n // 10
    return rotated_n
number = 12345
rotated_number = rotate_digits(number)
print("Rotated number:", rotated_number)
#output shoudl be 51234
#successfully ran in terminal


def count_vowels(string):
    vowels = "aeiouAEIOU" 
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
input_string = "Python is fun"
print("Number of vowels:", count_vowels(input_string))  
#output should be 3
#successfully ran in terminal


def digital_root(n):
    n = sum(int(digit) for digit in str(n))
    return n
number = 12345
print("Digital root:", digital_root(number))
#output should return 15
#successfully ran is terminal 