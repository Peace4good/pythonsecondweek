# 1. create an empty list called my_list
# Answer
my_list = []

# 2. Append the following elements to my_list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# 3. insert the value 15 at the second position in the list
my_list[1] = 15
print(my_list)

#4. extend my_list with another list
# creating a second list to extend
second_list = [50, 60, 70]
print(second_list)

my_list.extend(second_list)
print(my_list)

# 5. remove the last element from the list
del my_list [-1]
print (my_list)

# 6. Sort my_list in ascending order.
my_list.sort()
print(my_list)

# Find and print the index of the value 30 in my_list.
print(my_list[2])