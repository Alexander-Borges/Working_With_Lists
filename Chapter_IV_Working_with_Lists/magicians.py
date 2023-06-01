# Looping through an entire list
magicians = ['alice','david','carolina']
for item in magicians:
    print(item)

# Let's build on the previous example by printing a message to each magician, telling them that they performed a great trick.
magicians = ['alice','david','carolina']
for item in magicians:
    print(f"{item.title()}, that was a great trick!")
#Lets add a second line to our message, telling each magician that we're looking forward to their next trick:
    print(f"I cant wait to see your next trick, {item.title()}.\n")

# Any lines of code after the "for" loop that are not indented are executed once without repetition. Let's write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show.
magicians = ['alice','david','carolina']
for item in magicians:
    print(f"{item.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {item.title()}.\n")

print("Thank you, everyone. That was a great magic show!")