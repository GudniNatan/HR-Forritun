def createKey(comma_seperated_name):
    lastname, firstname = comma_seperated_name.split(", ")
    firstname = firstname.strip()
    lastname = lastname.strip()
    return firstname + " " + lastname


def clean_row(row):
    value_list = row.split(";")
    key = createKey(value_list[1])

    rank = int(value_list[0].strip())
    country = value_list[2].strip()
    rating = int(value_list[3].strip())
    byear = int(value_list[4].strip())
    value_dict = {"rank": rank, "country": country, "rating": rating, "birth year": byear}

    return key, value_dict


def openFile(filename):
    try:
        file = open(filename)
    except FileNotFoundError:
        print("File not found!")
        return
    file_contents = [line for line in file]
    file.close()
    return file_contents


def readCsvFile(file):
    chess_dict = dict()
    for line in file:
        key, values = clean_row(line)
        chess_dict[key] = values
    return chess_dict


def groupBy(chess_dict, col_name):
    group_dict = dict()
    for key, value in chess_dict.items():
        try:
            group_dict[value[col_name]].append(key)
        except KeyError:
            group_dict[value[col_name]] = [key]
    print(group_dict)
    return group_dict


def getAverageRating(chess_dict, names):
    players = [chess_dict[name] for name in names]
    total_score = 0
    for player in players:
        total_score += player["rating"]
    avg_score = total_score / len(players)
    return avg_score


def printGroupedList(chess_dict, grouped_dict, col_name):
    table_string = "Players by " + col_name + ":"
    print(table_string)
    print('-' * len(table_string))

    for country, playernames in sorted(grouped_dict.items()):
        avg_score = getAverageRating(chess_dict, playernames)
        print("{} ({}) ({:.1f}):".format(country, len(playernames), avg_score))

        for name in playernames:
            print("{:>40}{:>10d}".format(name, chess_dict[name]["rating"]))


def main():
    filename = input("Enter filename: ")
    file = openFile(filename)
    if file:
        chess_list = readCsvFile(file)
        grouped_chess_list = groupBy(chess_list, "country")
        printGroupedList(chess_list, grouped_chess_list, "country")
        print()
        grouped_chess_list2 = groupBy(chess_list, "birth year")
        printGroupedList(chess_list, grouped_chess_list2, "birth year")


main()
