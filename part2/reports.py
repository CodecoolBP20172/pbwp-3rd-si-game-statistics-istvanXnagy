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


# What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
    game_list = read_table(file_name)
    sold_list = []
    for i in game_list:
        sold_list.append(i["Copies sold"])
    for i in game_list:
        if i["Copies sold"] == max(sold_list):
            return i["Game name"]


# How many copies have been sold total?
def sum_sold(file_name):
    game_list = read_table(file_name)
    return sum([item['Copies sold'] for item in game_list])


# What is the average selling?
def get_selling_avg(file_name):
    game_list = read_table(file_name)
    sold_list = []
    for i in game_list:
        sold_list.append(i["Copies sold"])
    return sum(sold_list) / len(sold_list)


# How many characters long is the longest title?
def count_longest_title(file_name):
    game_list = read_table(file_name)
    title_list = []
    for i in game_list:
        title_list.append(i["Game name"])
    longest_title = max(title_list, key=len)
    return len(longest_title)


# What is the average of the release dates?
def get_date_avg(file_name):
    game_list = read_table(file_name)
    release_list = []
    for i in game_list:
        release_list.append(i["Release date"])
    return -(sum(release_list) // -(len(release_list)))


# What properties has a game?
def get_game(file_name, title):
    game_list = read_table(file_name)
    for i in game_list:
        if i["Game name"] == title:
            return [i["Game name"], i["Copies sold"], i["Release date"], i["Genre"], i["Publisher"]]


# -------------------------------------------------
# Bonus functions


# How many games are there grouped by genre?
def count_grouped_by_genre(file_name):
    game_list = read_table(file_name)
    genre_dict = {}
    for i in game_list:
        if i["Genre"] not in genre_dict:
            genre_dict[i["Genre"]] = 1
        elif i["Genre"] in genre_dict:
            genre_dict[i["Genre"]] += 1
    return genre_dict


# What is the date ordered list of the games?
def get_date_ordered(file_name):
    game_list = read_table(file_name)
    date_ordered = []
    game_list.sort(key=lambda item: item["Game name"])
    game_list.sort(key=lambda item: item["Release date"], reverse=True)
    for i in game_list:
        date_ordered.append(i["Game name"])
    return date_ordered
