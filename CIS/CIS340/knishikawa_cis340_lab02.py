# Excersize 2.2
# Ken Nishikawa
# CIS 340, Tue-Thur, Prof Lau
# Lab Chapter 2
# FYI:Prof Lau, I endned up using lots of comments # because I had LOTS of frutstration with my
# formulas ending up with the correct answer.



# Question 2.1
# name the variables in the formula
pi = 3.141592653589793
r = 5
# express the formula given
volume = (4/3) * pi * r**3
# show output
print(volume)

# 523.5987755982989




# question 2.2
# name the variables in teh forumal
# prompt user to enter textbook unit price and number of copies
full_price = float(input("Enter the unit price of the textbook: "))
copies = int(input("Enter the number of copies to order: "))
# shipping and discount variables
disc = 0.40
base_shipping = 3.00
additional_shipping = 0.75
# express the calculation given
disc_price = full_price * (1 - disc)
total_cost = disc_price * copies + base_shipping + additional_shipping * (copies - 1)
# display number in two decimel places
print("Grand total: $",round(total_cost,2))

# Enter the unit price of the textbook:  25.50
# Enter the number of copies to order:  20
# Grand total: $ 323.25




# question 2.3
# prompt the user for the starting time
start_hour = int(input("Enter the starting hour: "))
start_minute = int(input("Enter the starting minute: "))
# name pace variables in the formula and convert to seconds per mile
easy_pace = (8 * 60) + 15
tempo_pace = (7 * 60) + 12
# calculate total run time in seconds (2 easy miles + 3 tempo miles)
total_seconds = (easy_pace * 2) + (tempo_pace * 3)
# convert starting time to seconds
start_time_seconds = (start_hour * 3600) + (start_minute * 60)
# add total run time
end_time_seconds = start_time_seconds + total_seconds
# calculate back to hours, minutes (wrap 24h)
hours = (end_time_seconds // 3600) % 24
minutes = (end_time_seconds % 3600) // 60
# Print the result in HH:MM format
print("You will arrive home at: {:02d}:{:02d}".format(hours, minutes))

# Enter the starting hour:  7
# Enter the starting minute:  52
# You will arrive home at: 08:30
