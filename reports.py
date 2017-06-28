import csv

# -------------------------------------------------
# Custom functions


def read_file_to_line_list(file_name):
    # open file, read every line, return the list of lines
    with open(file_name) as f:
        content = f.readlines()

    for ctr in range(len(content)):
        content[ctr] = content[ctr].rstrip("\n")

    return content


def convert_line_list_to_dictionary_table(line_list):
    # assume for line_list:
    # line_list is of the type <list>
    # every element of line_list:
    #   is of the type <str>,
    #   has an equal number of tab-delimited substrings

    # Constants
    GAME_NAME_COLUMN_NAME = "Game name"
    COPIES_SOLD_COLUMN_NAME = "Copies sold"
    RELEASE_DATE_COLUMN_NAME = "Release date"
    GENRE_COLUMN_NAME = "Genre"
    PUBLISHER_COLUMN_NAME = "Publisher"

    result = []

    # for every line in line_list, append a new dictionary
    # to the result, of the format:
    # {column_name_1: column_value_1, column_name_2: column_value_2, column_name_3: column_value_3, ...}

    for line in line_list:
        current_line = line.split("\t")
        current_line_dictionary = {}

        current_line_dictionary[GAME_NAME_COLUMN_NAME] = current_line[0]
        current_line_dictionary[COPIES_SOLD_COLUMN_NAME] = float(current_line[1])
        current_line_dictionary[RELEASE_DATE_COLUMN_NAME] = int(current_line[2])
        current_line_dictionary[GENRE_COLUMN_NAME] = current_line[3]
        current_line_dictionary[PUBLISHER_COLUMN_NAME] = current_line[4]

        result.append(current_line_dictionary)

    return result


def read_table(file_name):
    return convert_line_list_to_dictionary_table(read_file_to_line_list(file_name))


# -------------------------------------------------
# Mandatory functions


# How many games are in the file?
def count_games(file_name="game_stat.txt"):
    # count and return the total number of game titles.
    game_list = read_file_to_line_list(file_name)
    return len(game_list)


# Is there a game from a given year?
def decide(file_name, year):
    # read file into a "table dictionary list",
    # for every row, check if its release date == year
    game_list = read_table(file_name)
    for i in game_list:
        if i["Release date"] == int(year):
            return True
    return False


# Which was the latest game?
def get_latest(file_name):
    game_list = read_table(file_name)
    latest = []
    for i in game_list:
        latest.append(i["Release date"])
    latest = max(latest)
    for i in game_list:
        if i["Release date"] == latest:
            return i["Game name"]


# How many games do we have by genre?
def count_by_genre(file_name, genre):
    game_list = read_table(file_name)
    genre_list = []
    for i in game_list:
        if i["Genre"] == genre:
            genre_list.append(i["Game name"])
    return len(genre_list)


# What is the line number of the given game(by title)?
def get_line_number_by_title(file_name, title):
    game_list = read_table(file_name)
    for ctr, i in enumerate(game_list):
        if i["Game name"] == title:
            return ctr+1


# -------------------------------------------------
# Bonus functions


# What are the genres?
def get_genres(file_name):
    game_list = read_table(file_name)
    genre_list = []
    for i in game_list:
        if i["Genre"] not in genre_list:
            genre_list.append(i["Genre"])
    return sorted(genre_list, key=str.lower)


# What is the release date of the top sold "First-person shooter" game?
def when_was_top_sold_fps(file_name):
    game_list = read_table(file_name)
    top_sold_games = []
    for i in game_list:
        if i["Genre"] == "First-person shooter":
            top_sold_games.append(i["Copies sold"])
    top_sold = max(top_sold_games)
    for i in game_list:
        if i["Copies sold"] == top_sold:
            return i["Release date"]
