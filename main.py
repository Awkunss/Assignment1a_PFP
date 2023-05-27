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
        res = str(temp ) + res

    return res

def subtracting_bignum(a,b):
    while len(a) > len(b):
        b = "0" + b
    while len(a) < len(b):
        a = "0" + a
    if a < b:
        temp=a
        a=b
        b=temp
    
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
    while res[0]=='0':
        res=res[1:]
    return res


def multi_bignum_bignum(a,b):
    zeros=""
    res=""
    for i in range(len(b)-1,-1,-1):
        temp=multi_bignum_digit(a,int(b[i]))+zeros
        zeros+='0'
        res=adding_bignum(res,temp)
    return res

def multi_bignum_digit(st, a):
    temp=0
    res=""
    for i in range(len(st)-1,-1,-1):
        multi=int(st[i]) *a+temp
        temp = multi // 10
        res = str(multi % 10) + res
    return res

def div_bignum(st, a):
    number=0
    res=""
    for i in range(0,len(st)):
        number=number*10+int(st[i])
        res=str(number%a)+res
        number=number//a
    return res

# def mod_bignum(st, a):
#     return 0
# while True:
#     number1 = input("Number 1:")
#     number2 = input("Number 2:")
#     if number1.isdecimal() and number2.isdecimal():
#         break
#     else:
#         print("Your type of input not match !!!")

def display_menu():
    while True:
        print("***************** Welcome to program to calculate (add, subtract, multiply and divide) two big number *****************")
        print("a. Adding two number, choose 1.")
        print("b. Subtracting two number, choose 2.")
        print("c. Multiplying two number, choose 3.")
        print("d. Dividing two number, choose 4.")
        print("e. To exit program, choose 5.")
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("You must choose one of our option.")
            continue
        if choice == "5":
            print("Thank for using our app. Goodbye.")
            break
        else:
            while True:
                a = input("Input number a: ")
                if not a.isdigit():
                    print("Please enter a number: ")
                    continue
                else:
                    break
            while True:
                b = input("Input number b: ")
                if not b.isdigit():
                    print("Please enter a number: ")
                    continue
                else:
                    break
            if choice == "1":
                print(f"Sum of two numbers a and b is {adding_bignum(a, b)}")
            elif choice == "2":
                print(f"Subtract two numbers a and b is {subtracting_bignum(a, b)}")
            elif choice == "3":
                print(f"Multiply two numbers a and b is {multi_bignum_bignum(a, b)}")
            # elif choice == "4":
            #     print(f"Divide two numbers a and b is {0}")
            print("******************************************************************************")
            y_n = input("Do you want to exit (Y/N): ")
            if y_n == "N":
                print("Thank for using our app.")
                break
            else:
                continue


if __name__ == "__main__":
    display_menu()

