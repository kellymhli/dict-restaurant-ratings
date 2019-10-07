"""Restaurant rating lister."""
def run_restaurant_program(filename):

    f = open(filename)

    restaurant_ratings = {}

    for line in f:
        line = line.rstrip()
        line_list = line.split(':')
        restaurant_ratings[line_list[0]] = line_list[1]

    string_input = (f"What do you want to do? \n""" 
                    f"""Add (A)\n"""
                    f"""See all ratings(S)\n"""
                    f"""Quit (Q)\n"""
                    f"""> """)

    user_choice = input(string_input)
    while user_choice != 'Q':
        if user_choice == 'A':
            prompt_user(restaurant_ratings)
        if user_choice == 'S':
            print_restaurant_ratings(restaurant_ratings)

        user_choice = input(string_input)


def prompt_user(restaurant_ratings):
    success = False
    new_restaurant = input('What is the restaurant name? ')
    while not success:
        try:
            new_rating = int(input("What is the restaurant's rating? "))
            while new_rating > 5 or new_rating < 1:
                new_rating = int(input("Invalid rating. Please reenter. "))
                success = True
        except:
            print('Rating should be a number.')
        else:
            restaurant_ratings[new_restaurant] = new_rating
            user_choice = input('Do you want to add a restaurant rating? (Y or N): ')
    return restaurant_ratings

def print_restaurant_ratings(restaurant_ratings):
    #Sorting
    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        print(f"{restaurant} is rated at {restaurant_ratings[restaurant]}.")

    # for key, value in restaurant_ratings.items():
    #     print(f"{key} is rated at {value}.")

run_restaurant_program('scores.txt')