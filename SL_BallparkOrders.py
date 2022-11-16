"""You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task
Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format
You will output a number of the total cost of the food and drinks.

Sample Input
'Pizza Cheeseburger Water Popcorn'

Sample Output
26.75"""

nachos = 6
pizza = 6
cheese = 10
water = 4
coke = 5
tax = 0.07

order = input() # 4 items in string
order = order.split(sep = " ")
order = list(order)

sum = 0

for item in range(len(order)):
    if order[item] == "Nachos":
        sum += nachos
    elif order[item] == "Pizza":
        sum += pizza 
    elif order[item] == "Cheeseburger":
        sum += cheese
    elif order[item] == "Water":
        sum += water 
    elif order[item] == "Coke":
        sum += coke 
    else:
        sum += coke

sum = sum + (sum*tax)
print(sum) # 4 water + tax should be 17.12