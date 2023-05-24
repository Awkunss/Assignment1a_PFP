# Function to add two large numbers
def adding_bignum(a, b):
    while len(a) > len(b):
        b = "0" + b
    while len(a) < len(b):
        a = "0" + a

    temp = 0
    res = ""
    for i in range(len(a) - 1, -1, -1):
        value_a = int(a[i])
        value_b = int(b[i])
        sum_ = value_a + value_b + temp
        temp = sum_ // 10
        res = str(sum_ % 10) + res

    if temp > 0:
        res = str(temp) + res

    return res

# Function to subtract one large number from another
def subtracting_bignum(a, b):
    while len(a) > len(b):
        b = "0" + b
    while len(a) < len(b):
        a = "0" + a
    if a < b:
        temp = a
        a = b
        b = temp

    temp = 0
    res = ""
    for i in range(len(a) - 1, -1, -1):
        value_a = int(a[i])
        value_b = int(b[i])
        value_a = value_a - temp

        if value_a < value_b:
            minus = value_a + 10 - value_b
            temp = 1
        else:
            minus = value_a - value_b
            temp = 0
        res = str(minus % 10) + res
    while res[0] == "0":
        res = res[1:]
    return res

# Function to multiply two large numbers
def multi_bignum_bignum(a, b):
    zeros = ""
    res = ""
    for i in range(len(b) - 1, -1, -1):
        temp = multi_bignum_digit(a, int(b[i])) + zeros
        zeros += "0"
        res = adding_bignum(res, temp)
    return res

# Function to multiply a large number by a single-digit number
def multi_bignum_digit(st, a):
    temp = 0
    res = ""
    for i in range(len(st) - 1, -1, -1):
        multi = int(st[i]) * a + temp
        temp = multi // 10
        res = str(multi % 10) + res
    return res

# The function to calculate the quotient of a large number divided by a number not bignum
def div_bignum(st, a):
    number = 0
    res = ""
    for i in range(0, len(st)):
        number = number * 10 + int(st[i])
        res = str(number // a) + res
        number = number % a
    while res[0] == "0":
        res = res[1:]
    return res

# The function to calculate the modulo of a large number divided by a number not bignum
def mod_bignum(st, a):
    number = 0
    res = ""
    for i in range(0, len(st)):
        number = number * 10 + int(st[i])
        number = number % a

    return number

# Main
if "__main__"==__name__:
    while True:
        number1 = input("Number 1:")
        number2 = input("Number 2:")
        if number1.isdecimal() and number2.isdecimal():
            break
        else:
            print("Your type of input not match !!!")

    print(mod_bignum(number1, int(number2)))
