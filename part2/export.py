from reports import *


# exporting files from reports.py to a newly created txt file
def export_data(file_name="export_results.txt"):
    with open(file_name, 'w', newline="\n") as file:
            file.writelines(str(get_most_played("game_stat.txt"))+"\n")
            file.writelines(str(sum_sold("game_stat.txt"))+"\n")
            file.writelines(str(get_selling_avg("game_stat.txt"))+"\n")
            file.writelines(str(count_longest_title("game_stat.txt"))+"\n")
            file.writelines(str(get_date_avg("game_stat.txt"))+"\n")
            file.writelines(str(get_game("game_stat.txt", "Doom 3"))+"\n")
            file.writelines(str(count_grouped_by_genre("game_stat.txt"))+"\n")
            file.writelines(str(get_date_ordered("game_stat.txt"))+"\n")

export_data()