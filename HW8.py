#Name:Adrian silver
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print ("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
first_num=random.randint(1,10)
second_num=random.randint(1,10)
third_num=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(first_num,second_num,third_num)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
res_first=first_num+2
res_second=second_num-4
res_third=third_num*1.5
#6. Print each result from #5 on the same line.
print(res_first,res_second,res_third)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
rand_num_list=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),]
#8. Sort the list in #7 and print it.
rand_num_list.sort()
print(rand_num_list)
#9. Add together the highest three numbers in the list from #7 and print the result.

#10. Create a list with 5 names of other students in this class and print the list.
students=["cruz", "lila", "oliver", "antony", "echo"]
print(students)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(students)
print(students)
#12. Print a random choice from the list of names from #10.
print(random.choice(students))
