#Name:Adrian silver
#Class: 5th Hour
#Assignment: HW14
import random

# 1. Create a while loop with variable i that counts down from 5 to 0 and then prints
# "Hello world!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
print("Hello world!")

# 2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
num = 1
while num <= 30:
    if num % 2 == 0:
        print(num)
    num += 1

# 3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
# number is divisible by 3.
count = 0
while count < 30:
    count += 1
    if count % 3 == 0:
        continue
    print(count)

# 4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
# and then breaks the loop if it's a 1.
while True:
    roll = random.randint(1, 6)
    print(roll)
    if roll == 1:
        break

# 5. Create a while loop that asks for a number input until the user inputs the number 0.
user_num = int(input("Enter a number (0 to quit): "))
while user_num != 0:
    user_num = int(input("Enter a number (0 to quit): "))
