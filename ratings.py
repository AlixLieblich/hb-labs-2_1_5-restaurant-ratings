
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant
# Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.
# Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

# put your code here
import copy 

def rating_reader():
    """Restaurant rating lister."""

    restaurant_list = open('scores.txt')
    restaurant_ratings = {}
    
    for line in restaurant_list:
        line = line.strip('/n')
        restaurant, score = line.split(':') # this is a list
        restaurant_ratings[restaurant] = int(score)

    sorted_restaurant = sorted(restaurant_ratings.items())


    for restaurant, score in sorted_restaurant:
        print(f"{restaurant} is rated at {score}.")


    rest_name = input("Which restaurant would you like to review?  > ")
    rest_score = input("What do you  this restaurant?  > ")
   
    restaurant_ratings[rest_name.title()] = int(rest_score)
    # restaurant_ratings['apple'] = 1
    
    restaurant = sorted(restaurant_ratings.items())
    

    for restaurant, score in restaurant:
        print(f"{restaurant} is rated at {score}.")

    
    return restaurant_ratings
    
rating_reader()

