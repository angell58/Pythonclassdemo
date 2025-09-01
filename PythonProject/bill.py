subtotal = float(input("type the subtotal of your bill"))
num = int(input("your number of friends"))

#total = subtotal + 0.2 * subtotal
#divided = total/num

divided = subtotal/num

# .2f rounds off the float to 2 decimal places
print(f"each friend has to pay= {divided:.2f}")

""" 
round() can be used to round off to 2
places such as : round(divided, 2)
"""

print("Thank you for using the bill calculator!")
