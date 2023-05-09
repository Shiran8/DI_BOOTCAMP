
# # receive all the keys
# # example: print(family.keys())

# # receive all the values
# # example: print(family.values())

# # 🌟 Exercise 2.1 : Cinemax
# # Instructions
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.

# # Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# # How much does each family member have to pay ?

# # Print out the family’s total cost for the movies.
# # Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# # age = int(input("Enter age: "))
# # ticket_price = 0

# # if age < 3:
# #    ticket_price = 0
# # elif age >= 3 and age <= 12:
# #    ticket_price = 10
# # else:
# #    ticket_price = 15

# # print("The ticket price is", ticket_price)

# # Exercise 2.2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# # Exercise 2.3

# total_bill = sum(family.values())
# num_family_members = len(family)

# each_pays = total_bill / num_family_members
# print("Each family member has to pay:", each_pays)

# # Exercise 2.4

# # total_cost = 0

# # for name, age in family.items():
# # #    ticket_price = 0
# # #    if age < 3:
# # #       ticket_price = 0
# # #    elif age >= 3 and age <= 12:
# # #       ticket_price = 10
# # #    else:
# # #       ticket_price = 15
# #     total_cost += ticket_price
   
# #    print("The family's total cost for the movies is:", total_cost)

# # Exercise 2.5

# names = []
# ages = []

# while True:
#     name = input("Enter family member name (or 'done' to finish): ")
#     if name == 'done':
#       break
#     age = int(input(f"Enter {name}'s age (or 'done' to finish): "))
#     names.append(name)
#     ages.append(age)

# print(names, ages)

#     total.bill = sum(family.values())
#     num_family_members = len(family)
#     each_pays = total_bill / num_family_members
   
# print("Each family member has to pay:", each_pays)

    
# age = int(input("Enter age: "))
# family[name] = age

# Exercises 3.1 Zara

# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": { 
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"],
#     }
# }
# print(brand)


# # 3. Change the number of stores to 2.

# # brand["number_stores"] = 2

# # print(brand)

# # 4. Print a sentence that explains who Zaras clients are.

# types_str =''
# types = brand['type_of_clothes']
# types_str += ', '.join(types)

# sentence =f"the clients of zara are {types_str}" #code
# print(sentence)

# # 5. Add a key called country_creation with a value of Spain.

# brand["country_creation"] = "Spain"

# # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

# if "internation_competitors" in brand:
#     brand["international_competitors"] += "Desigual"

# else:
#     brand["international_competitors"] = "Desigual"
# print(brand)

# # 7. Delete the information about the date of creation.

# del brand["creation_date"]
# print(brand)

# 8. Print the last international competitor.

# competitors = brand.get("internation_competitors")
# if competitors:
#     last_competitor = competitors
#     print(last_competitor)

# 9. Print the major clothes colors in the US.

# us_colors = brand["major_color"]["US"]
# print("Major clothes colors in the US:", us_colors)

# 10. Print the amount of key value pairs (ie. length of the dictionary).

# print(len(brand))

# # 11. Print the keys of the dictionary.

# print(brand.keys())

# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?