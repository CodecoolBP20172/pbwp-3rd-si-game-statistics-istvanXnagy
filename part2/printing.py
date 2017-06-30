from reports import *


# Printing function
def print_func(file_name, title):
    print(get_most_played(file_name))
    print(sum_sold(file_name))
    print(get_selling_avg(file_name))
    print(count_longest_title(file_name))
    print(get_date_avg(file_name))
    print(get_game(file_name, title))
    print(count_grouped_by_genre(file_name))
    print(get_date_ordered(file_name))

print_func("game_stat.txt", "Doom 3")
