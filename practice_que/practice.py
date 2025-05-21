# •	Write a Python program that asks the user for their name and greets them with a personalized message.

# your_name = input("Enter your name: ")
# print(f"your name is {your_name}!")

#####################################################################################################################3

# •	Write a Python program that calculates the area of a rectangle. The program should ask the user for the length and width of the rectangle and then display the calculated area.

# legnth = float(input("Enter the length of rectangle: "))
# breadth = float(input("Enter the breadth of rectangle: "))

# area_of_rectangle = legnth * breadth

# print(f"Area of rectangle is {area_of_rectangle}")

######################################################################################################################

#•	Write a Python program that converts temperature from Celsius to Fahrenheit.
#  The program should ask the user for the temperature in Celsius and then display the equivalent temperature in Fahrenheit.

# celcius = float(input("Enter the celcius: "))
# fahreinheit = (celcius * (9/5)) + 32

# print(f"fahrenheit is equal to {fahreinheit}")

######################################################################################################################

meal = []
tax = 0.25
price = 0

while True:
    food = input("Enter the food (type q to quit): ")
    meal.append(food)
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Price of {food} is: "))
        price += price
    
tip = price * (18/100)

# print(food)
print(price)
print(tip)
print(meal)
