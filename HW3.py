#Name:Adrian silver
#Class: 5th Hour
#Assignment: HW3
from idlelib.debugobj import myrepr

#1. Print "Hello World!"
print('hello world')
#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
my_int =10 my_str ="python" my_bool =True
#3. Print all three variables on the same print function (at the same time).
print('my_int my_str my_bool')
#4. Create a variable that asks the user to input an integer.
user_input = input("please enter a number")
#5. Add the integer variable from #2 with the integer from #4 and print the result.
addition_result = my_int + user_input print(addition_result)
#6. Take the result from #5 and divide it by 2. Print the result.
division_result = addition_result / 2 print(division_result)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
my_bool =not my_bool
#8. Print the value of the boolean variable.
print(my_bool)
#9. Create a variable with a number that contains decimals.
decimal_num =7.65
#10. Round the number from #9 up or down using the round function.
rounded_num = round(decimal_num)