# colors = ["blue", "red", "pink", 23, True, [1,2,3]]
colors = ["blue", "red", "pink"]
my_favorite_color = colors[1]
print(my_favorite_color)

colors = ["blue", "red", "pink", ["a","b", "c"]]
letter_c = colors[3][2]
print(letter_c)

# colors[3] # ["a", "b", "c"]

len(str) #length

colors = ["blue", "red", "pink"]
colors.append("yellow") # add the color of the end of the list
print(colors)
colors.insert(1, "green")
print(colors)

colors = ["blue", "red", "pink", ["a","b", "c"]]
colors[3].append("d")
colors[-1].append("d")
print(colors)
colors[3].insert(0, "z")
print(colors)

#append
appends/ adds automaticly at the end of a list

#insert
#add in certain position
colors = ["blue", "red", "pink"]
colors.insert(2, "white") #["blue", "red", "pink", "green"]

#remove element of list
#colors = ["blue", "red", "pink"]
colors.pop () #deleting the last element
#print colors
colors.pop(1) # deleting the element at position 1
#print (color)
colors.remove ("red")
print(colors)


colors = ["blue", "red", "pink"]
favorite_colors = colors

#print(favorite colors)
favorite_colors.pop() # delete last element in the list
# ["blue", "red"]
print("favorite_colors" ,favorite_colors)
print("colors" ,colors)

#exercise 1 platfrom day 2
list1 = [5, 10, 15, 20, 25, 50, 20]
# FIRST WAY -HARDCODED
list1[3] = "200"

# SECOND WAY - BETTER
position = my_list.index(20) # 3
# first position of the number 20 in the list

my_list[position]
list1[3] = "hello"

index_of_d = list1.index("d") #3 to find the position



# LOOP
# loop a cretain number of time -->

#for variable in list of number :
 # do this

#  for number in range(5) :
#  print(number)
#  print("hello")

# 1st Loop
# 0, "hello"

# 2nd Loop
# 1, "hello"

# etc, etc ...

color = ["blue", "red", "yellow", "pink"]

# loop that goes inside the list and print

for color in colors : 
    print(color)
    1st loop 
    "blue"

    2nd loop
    "red"

    3rd loop
    "yellow"

    4th loop
    "pink"

    numbers = [1,2,3,4,5,6]

for num in numbers :
    if num % 2 == 0:
    print("the number is even")
elif num % 2 == 1:
print("the number is odd")