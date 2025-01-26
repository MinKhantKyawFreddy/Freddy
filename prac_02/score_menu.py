MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = int(input("Score: "))
    valid_score(score)
    result(score)


def valid_score(score):
    if score > 100 or score < 0:
        return "INVALID SCORE"


def result(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
