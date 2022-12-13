"""
Day 13: Pay Your Tax
Write a function called your_vat. The function takes no 
parameter. The function asks the user to input the price of an 
item and VAT (vat should be a percentage). The function should 
return the price of the item plus VAT. If the price is 220 and, 
VAT is 15% your code should return a vat inclusive price of 253. 
Make sure that your code can handle ValueError. Ensure the 
code runs until valid numbers are entered. (hint: Your code 
should include a while loop).
"""
"""
research
https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained
"""
price = float(input("Please Enter price ($) : "))

vat = float(input("Please Enter Vat % (%) : "))

vat_price = price * (1 + vat/100)

print(f"price with vat : {round(vat_price)}")




""""
https://www.w3schools.com/python/python_try_except.asp
"""