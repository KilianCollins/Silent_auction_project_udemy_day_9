#
# travel_log = [
#     {"France":
#           {"cities_visited":["Dijon", "Lille","Paris"]}
#     },
#     {"Germany":
#          {"cities_visited":["Berlin", "Hamburg", "Cologne"]}
#     }
# ]
#
#
#
# print(travel_log)


country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

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
# Do NOT change the code above 👆

def add_new_country(country_input, visit_input,list_of_cites_input):
    travel_log.append({
      "country": country_input,
      "visits": visit_input,
      "cities": list_of_cites_input #my attempt at this excersize is cooler than the instructors :)
    })



# TODO: Write the function that will allow new countries
# to be added to the travel_log.




# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")