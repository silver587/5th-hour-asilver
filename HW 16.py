#Name: Adrian silver
#Class: 5th Hour
#Assignment: HW16

#1. import the random library
import random

#2. print Hello World!
print("Hello World!")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))

#4. Add a and b together, then divide the sum by c. Print the result.
result = (a + b) / c
print("Result:", result)

#5. Round the result from #4 up or down, and then determine if it is even or odd.
rounded_result = round(result)
print("Rounded result:", rounded_result)

if rounded_result % 2 == 0:
    print("The rounded result is even.")
else:
    print("The rounded result is odd.")

#6. Create a list of five different random integers between 1 and 10.
num_list = random.sample(range(1, 11), 5)
print("Random list:", num_list)

#7. Print the 4th number in the list.
# Note: Lists start at index 0, so the 4th item is at index 3.
print("4th number:", num_list[3])

#8. Append another integer to the end of the list, also random from 1 to 10.
num_list.append(random.randint(1, 10))
print("List after appending:", num_list)

#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num_list.sort()
print("Sorted list:", num_list)
print("New 4th number:", num_list[3])

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i

#11. Create a list containing the names of five other students in the classroom.
students = ["cruz","lila",'max',"gavin","ethan"]

#12. Create a for loop that individually prints out the names of each student in the list.
for student in students:
    print(student)

#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for num in range(1, 101):
    print(num)
    if num % 10 == 0:
        break

#14. Free space. Do something creative. :)
