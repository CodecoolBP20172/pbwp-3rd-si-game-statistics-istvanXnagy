from reports import *


# Printing function
def print_func(file_name, year, genre, title):
    print(count_games(file_name))
    print(decide(file_name, year))
    print(get_latest(file_name))
    print(count_by_genre(file_name, genre))
    print(get_line_number_by_title(file_name, title))
    print(get_genres(file_name))
    print(when_was_top_sold_fps(file_name))


print_func("game_stat.txt", "2004", "RPG", "Diablo III")