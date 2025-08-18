def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * ((100 - discount_percent) / 100)
        return discounted_price
    else:
       return price
    
try:
    price = int(input("Key in the price: "))
    discount_percent = int(input("Key in the dicount: "))
    result = calculate_discount(price, discount_percent)
    print("Final price:", result) 
    
except ValueError:
    print("Key in intergers")


