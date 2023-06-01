#1 Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza
fav_pizzas = ['New York','Detroit','Sicilian']
for pizza in fav_pizzas:
    print(pizza)

# - Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza should instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza
fav_pizzas = ['New York','Detroit','Sicilian'] 
for pizza in fav_pizzas:
    print(f"I think my favorite pizza is {pizza} style pizza.")
print("I really like pizza!")

# 2 Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
dogs = ['beagle','dachshund','dalmatian']
for dog in dogs:
    print(dog)
# - Modify you program to print a statement about each animal, such as A dog would make a great pet.
dogs = ['beagle','dachshund','dalmatian']
for dog in dogs:
    print(f"A {dog.title()} would make a great pet.")

# - Add a line at the end of your program stating what these animals have in common. 
dogs = ['beagle','dachshund','dalmatian']
for dog in dogs:
    print(f"I love {dog}s because they are so loyal.")
print("Any of these dogs would make a great pet!")

# 3 Counting to Twenty: Use a for loop for print the numbers from 1 to 20, inclusive 
for i in range(1,21):
    print(i)

# 4 One Million: Make a list of the numbers from one to a million, and then use a for loop to print the numbers.
million = []
for number  in range(1, 1_000_001):
    million.append(number)

# 5 Summing a Million: Make  a 
million = list(range(1,1_000_001))
#print(million)
print(min(million))
print(max(million))
print(sum(million))

# 6 Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
i = []
for i in range(1,21,2):
    print(i)

# 7 Threes: Make a list of the multiples of 3 from 3 to 30. Use a loop to print the numbers in your list
x = []
for x in range(3,31,3):
    print(x)

# 8 Cubes: Make a list of the first 10 cubes, and use a for loop to print out the value of each cube
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# Use a list comprehension  to generate a list of the first 9 cubes
cubes = [value**3 for value in range(1,11)]
print(cubes)

# 10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
bands = ['A Day to Remember','Dance Gavin Dance', 'Lorna Shore','Chelsea Grin','Pierce the Veil']
print('The first three items in the list are:')
for band in bands[:3]:
    print(band)

# - print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
bands = ['A Day to Remember','Dance Gavin Dance', 'Lorna Shore','Chelsea Grin','Pierce the Veil']
print("\n"'The items in the middle of the list are:')
for band in bands[1:4]:
    print(band)

bands = ['A Day to Remember','Dance Gavin Dance', 'Lorna Shore','Chelsea Grin','Pierce the Veil']
print("\n"'The last three items in the list are:')
for band in bands[2:5]:
    print(band)

# 



