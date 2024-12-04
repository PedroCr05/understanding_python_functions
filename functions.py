# ------------------------ #
# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):  
    return (base * height) / 2

print('Exercise 1.1:', calculate_area_triangle(10, 5))
print('Exercise 1.2:', calculate_area_triangle(7, 3))
print('Exercise 1.3:', calculate_area_triangle(2, 9))
# ------------------------ #
# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2.1:', simple_interest(1000, 5, 2))
print('Exercise 2.2:', simple_interest(1500, 3.5, 5))
print('Exercise 2.3:', simple_interest(3789, 9.6, 8))
# ------------------------ #
# Exercise 3: Apply a Discount

def apply_discount(price, discount):
    discounted_amount = (discount / 100) * price
    final_price = price - discounted_amount
    return final_price

print('Exercise 3.1:', apply_discount(100, 25))
print('Exercise 3.2:', apply_discount(80, 10))
print('Exercise 3.3:', apply_discount(900, 94))
# ------------------------ #
# Exercise 4: Convert Temperature
def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
# ------------------------ #
# Exercise 5: Sum to N
def sum_to(N):
    if N < 1:
        return "Input must be a positive integer."
    return sum(range(1, N + 1))

print('Exercise 5: Sum of integers from 1 to 6:', sum_to(6))
print('Exercise 5: Sum of integers from 1 to 10:', sum_to(10))
# ------------------------ #
# Exercise 6: Find the Largest Number
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print('Exercise 6.1: Largest of (1, 2, 3):', largest(1, 2, 3))
print('Exercise 6.2: Largest of (10, 4, 2):', largest(10, 4, 2))
print('Exercise 6.3: Largest of (7, 7, 5):', largest(7, 7, 5))
# ------------------------ #
# Exercise 7: Calculate a Tip
def calculate_tip(bill_amount, tip_percentage):
    return (bill_amount * tip_percentage) / 100

print('Exercise 7.1: Tip for a $50 bill with 20% tip:', calculate_tip(50, 20))
print('Exercise 7.2: Tip for a $100 bill with 15% tip:', calculate_tip(100, 15))
print('Exercise 7.3: Tip for a $75 bill with 18% tip:', calculate_tip(75, 18))
# ------------------------ #
# Exercise 8: Calculate Product of Numbers
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8.1: Product of (-1, 4):', product(-1, 4))
print('Exercise 8.2: Product of (2, 5, 5):', product(2, 5, 5))
print('Exercise 8.3: Product of (3, 7, 9):', product(3, 7, 9))
# ------------------------ #
# Exercise 9: Basic Calculator
def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operation"

print('Exercise 9.1: 10 - 5 =', basic_calculator(10, 5, 'subtract'))
print('Exercise 9.2: 10 + 5 =', basic_calculator(10, 5, 'add'))
print('Exercise 9.3: 10 * 5 =', basic_calculator(10, 5, 'multiply'))
print('Exercise 9.4: 10 / 5 =', basic_calculator(10, 5, 'divide'))