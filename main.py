travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
  travel_log.append({"country": country, "visits": visits, "cities": cities})



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# What you know

# These are questions you got right on the first try.
# Which line of code will print "Steak"?order = { "starter": {1: "Salad", 2: "Soup"}, "main": {1: ["Burger", "Fries"], 2: ["Steak"]}, "dessert": {1: ["Ice Cream"], 2: []}, }
# What you should review

# Which line of code will change the starting_dictionary to the final_dictionary?starting_dictionary = { "a": 9, "b": 8, }final_dictionary = { "a": 9, "b": 8, "c": 7, }
# Which line of code will produce an error?dict = { "a": 1, "b": 2, "c": 3, }
