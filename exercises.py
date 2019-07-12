
# Exercise 0.1
fav_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
age_of_family = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
coin_flip = ["head", "head", "tail", "tail", "head"]
fav_performing_artists = ["Eleanor Antin", "Andreas Heusser", "Dennis Oppenheim"]

# Exercise 0.2
words_and_definitions = {
    'noun': "name of a person, animal, place or thing",
    'pronoun': "word that refers to a noun",
    'verb': "word that describes an action, state, or occurence"
}
movie_names_and_year = {
    'the sound of music': 1965,
    'titanic': 1997,
    'avatar': 2009
}
cities_and_population = {
    'new york city': 8613000,
    'london': 8787000, 
    'beijing': 21540000
}
list_of_family_names = {
    'emma': 19,
    'liam': 15,
    'dan': 45,
    'kate': 43
}

# Exercise 1
print(coin_flip)
print(fav_colours[0])
print(age_of_family.sort())
age_of_family.append(0)
print(movie_names_and_year['titanic'])

#Exercise 2
print(fav_colours[6])
cities_and_population['paris'] = 2141000
coin_flip.reverse()
print(coin_flip)
print(cities_and_population['new york city'])
print(fav_performing_artists[0] + " is a female performing artist")
print(fav_performing_artists[1] + " is a male performing artist")
print(fav_performing_artists[2] + " was a male performing artist")


# Exercise 3
print(fav_performing_artists[0])
print(fav_performing_artists[1])
# print(movie_names_and_year[0] + " was produced in 1965")
# print(movie_names_and_year[1] + " was produced in 1997")
# print(movie_names_and_year[2] + " was produced in 2009")
age_of_family.sort()
age_of_family.reverse()
print(age_of_family)
movie_names_and_year['Beauty and the Beast'] = "1991", "2017"
print(movie_names_and_year['Beauty and the Beast'])


# Exercise 4
# Exercise 4.1
for item in age_of_family:
    if item < 30:
        print(item)


# Exercise 4.2
maxAge = 0

for item in age_of_family:
    if maxAge < item:
        maxAge = item

print("Oldest person\'s age {}".format(maxAge))


# Exercise 4.3
count = 0
for item in coin_flip:
    if item.lower() == "head":
        count+=1

# Exercise 4.4
fav_performing_artists.remove("Eleanor Antin")

# Exercise 4.5
cities_and_population['new york city'] = 2700000

#Exercise 5
# Exercise 5.1
print(cities_and_population.values())

sum_of_population = 0
population_values = cities_and_population.values()

for i in population_values:
    sum_of_population += i

print(sum_of_population)


# Exercise 5.2 
for key in list_of_family_names:
    if list_of_family_names[key] < 30:
        print("{} is young".format(key))
    else:
        print("{} is old".format(key))

# Exercise 5.3
print("fav_colours")
print(fav_colours)
print(fav_colours[-2], fav_colours[-1])


# Exercise 5.4
for idx, val in enumerate(age_of_family):
    age_of_family[idx] = val + 1

print(age_of_family)

# Exercise 5.5
fav_colours.append("blue-violet")
fav_colours.append("blue-green")

# Exercise 6.1
movies = {
    1999: ["The Matrix", "Star Wars: Episode 1", "The Mummy"],
"2009": ["Avatar", "Star Trek", "District 9"],
"2019": ["How to Train Your Dragon 3", "Toy Story 4", "Star Wars: Episode 9"]
}


# Exercise 6.2
phone_keypad = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
    ["*", 0, "#"]
]

# Exercise 6.3
countries_info = [
     {
         "name": "Nigeria",
         "continent": "Africa",
         "island": "no"
    },
         {
         "name": "Canada",
         "continent": "North America",
         "island": "no"
    },
         {
         "name": "Jamaica",
         "continent": "North America",
         "island": "yes"
    }

]


#Exercise 7.1 and 7.2
def skate_board_message(number):
    count = 0

    result = []
    while (count < number):
        print("I will not skateboard in the halls")
        result.append("I will not skateboard in the halls")
        count += 1
    return result
result = skate_board_message(20)

# Exercise 7.3, 7.4, 7.5
numbers = [2, 5, 42, 7, 1, 23, 13, 45, 6, 7, 39]

count = 0
for item in numbers: 
    count += item

print(count)

# Exercise 7.6
non_island_countries = []
for country in countries_info:
    if country["island"] == "no":
        non_island_countries.append(country["name"])

print(non_island_countries)


# Exercise 8 
def sum_of_expenses(expenses):

    total_expenses  = 0
    for item in expenses:
        total_expenses += item

    print(total_expenses)

    return total_expenses

sum_of_expenses([250, 7.95, 30.95, 16.50])
sum_of_expenses([3.50, 29.99, 54.23])