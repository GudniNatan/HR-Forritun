#game_of_eights() function goes here
def game_of_eights(a_list):
    try:
        int_list = [int(x) for x in a_list]
    except ValueError:
        return None
    last_n = 0
    for n in int_list:
        if n == 8 and last_n == 8:
            return True
        last_n = n
    return False

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    eightGame = game_of_eights(a_list)

    if eightGame is None:
        print("Error. Please enter only integers.")
    else:
        print(eightGame)

main()