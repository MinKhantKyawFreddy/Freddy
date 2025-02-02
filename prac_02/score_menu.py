MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    score = int(input("Score: "))
    choice = input(">>>").upper()

    while choice != "Q":
        if choice == "G":
            valid_score(score)
            print(valid_score(score))
        elif choice == "P":
            result(score)
            print(result(score))
        elif choice == "S":
            show_stars(score)
            print(show_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    else:
        print("GOOD BYE")


def valid_score(score):
    if score > 100 or score < 0:
        return "INVALID SCORE"
    else:
        return "Score is valid"


def result(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def show_stars(score):
    star = "*" * score
    return star


main()
