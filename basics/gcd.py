#GCD of two numbers

# define a function

def compute_gcd(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd
# take first no
x = int(input (" Enter the first number: ") )
# take second no
y = int (input (" Enter the second number: "))
num = compute_gcd(x, y) # call the gcd_fun() to find the result
print("GCD of two number is: ")
# call num
print(num)
