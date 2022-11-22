"""
Day 5: My Discount
Create a function called my_discount. The function takes no 
arguments but asks the user to input the price and the 
discount (percentage) of the product. Once the user inputs the 
price and discount, it calculates the price after the discount. 
The function should return the price after the discount. For 
example, if the user enters 150 as price and 15% as the discount, 
your function should return 127.5.
"""

def my_discount():
    """
    asks the user to input the price and the 
    discount (percentage) of the product. Once the user inputs the 
    price and discount, it calculates the price after the discount. 
    The function should return the price after the discount.  
    
    Args:
        float
        float
    Return
        float 
    """
    price = float(input("Please enter the price of the product in $ : "))
    percent_off = float(input("Please enter the discount in % example 25% off : "))
    
    discount_price = price * (1-percent_off/100)
    return discount_price

print(my_discount())