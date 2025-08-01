def calculator(a, b, c):
  
    if c == '+':
        print(a + b)

    elif(c == '-'):
        print(a -b)

    elif(c == '*'):
        print(a * b)

    elif(c == '%'):
        print(a % b)

    else:
        return "Invalid operator"
    
a = input("Key in the first number: ")
b = input("Key in the second number: ")
c = input("Key in the operator: ")

try:
    a = float(a)
    b = float(b)
    result = calculator(a, b, c)
    print(result)

except ValueError:
    print("Key in an operator")
    


              

      

        

        







