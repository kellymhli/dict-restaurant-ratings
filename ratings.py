"""Restaurant rating lister."""
import random, os, sys

def run_restaurant_program():

    restaurant_ratings = {}

    string_input = (f"\n\nWhat do you want to do? \n""" 
                    f"""Add (A)\n"""
                    f"""See all ratings (S)\n"""
                    f"""Update rating (U)\n"""
                    f"""Update random restaurant (R)\n"""
                    f"""Import File (I)\n"""
                    f"""Quit (Q)\n"""
                    f"""> """)

    user_choice = input(string_input)
    user_choice = user_choice.upper()
    while user_choice != 'Q':
        if user_choice == 'A':
            prompt_user(restaurant_ratings)
        if user_choice == 'S':
            print_restaurant_ratings(restaurant_ratings)
        if user_choice == 'U':
            update_rating(restaurant_ratings)
        if user_choice == 'R':
            update_random(restaurant_ratings)
        if user_choice == 'I':
            path = "."
            dirs = os.listdir(path)
            for file in dirs:
                if file.endswith(".txt"):
                    print(f'<<{file}')
            file_to_open = input('\nWhat file do you want to import? ')
            import_file(file_to_open, restaurant_ratings)


        user_choice = input(string_input)
        user_choice = user_choice.upper()


def prompt_user(restaurant_ratings):
    new_restaurant = input('\nWhat is the restaurant name? ')
    new_rating = get_and_check_rating()
    restaurant_ratings[new_restaurant] = new_rating
    return restaurant_ratings


def print_restaurant_ratings(restaurant_ratings):
    #Sorting
    sorted_restaurants = sorted(restaurant_ratings)

    for restaurant in sorted_restaurants:
        print(f"{restaurant} is rated at {restaurant_ratings[restaurant]}.")

    # for key, value in restaurant_ratings.items():
    #     print(f"{key} is rated at {value}.")


def update_rating(restaurant_ratings):
    restaurant = input("\nWhat restaurant would you like to update? ")
    if not restaurant_ratings.get(restaurant, False):
        print('That is not a restaurant in the program.')
    else:
        print(f'{restaurant} is currently rated at {restaurant_ratings[restaurant]}.')
        restaurant_ratings[restaurant] = get_and_check_rating()


def get_and_check_rating():
    success = False
    while not success:
        try:
            new_rating = int(input("What is the restaurant's rating? "))
            while new_rating > 5 or new_rating < 1:
                new_rating = int(input("Invalid rating. Please reenter. "))
        except:
            print('Rating should be a number.')
        else:
            success = True
            return new_rating


def update_random(restaurant_ratings):
    restaurant = random.choice(list(restaurant_ratings.keys()))
    print(f'{restaurant} is currently rated at {restaurant_ratings[restaurant]}.')
    restaurant_ratings[restaurant] = get_and_check_rating()


def import_file(filename, restaurant_ratings):
    if os.path.isfile(filename):
        f = open(filename)
        for line in f:
            line = line.rstrip()
            line_list = line.split(':')
            restaurant_ratings[line_list[0]] = line_list[1]
        f.close()
    else:
        print('\nThe file you chose to import is not a file in the directory.')


run_restaurant_program()