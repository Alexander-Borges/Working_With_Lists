# Slicing a List
# To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify.
players = ['charles','martina','michael','florence','eli']
print(players[0:3])

# You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the index at 1 and end the index at 4:
players = ['charles','martina','michael','florence','eli']
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list. Without a starting index, Python starts at the beginning of a list.

# Similarly you can slice that includes the end of a list

# Looping Through a Slice
# You can use a slice in a for loop if you want to loop though a subset of the elements in a list. In the next example we loop through the first three players and print their names as part of a simple roster:
players = ['charles','martina','michael','florence','eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
 