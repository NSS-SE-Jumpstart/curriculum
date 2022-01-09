# This is a comment
# Python will ignore this
# But a human can read it




####################################
# if statement example

favorite_color = input("What's your favorite color? ")

if favorite_color == "green":
    print("I like green too")
elif favorite_color == "red":
    print("Like a fire engine!")
elif favorite_color == "purple":
    print("You must have royal blood")
else:
    print("Your favorite color, " + favorite_color + ", does not interest me")




####################################
# print a visual separator

print() # print a blank line
print("-------------------")
print()




####################################
# while loop example

counter = 0
while counter < 3:
    print("Cheer!")
    counter = counter + 1




####################################
# print a visual separator

print()
print("-------------------")
print()




####################################
# string to integer example

str_loop_count = input("How many times should we loop? ")
loop_count = int(str_loop_count)

counter = 0
while counter < loop_count:
    print("LOOP-DA-LOOP")
    counter = counter + 1

