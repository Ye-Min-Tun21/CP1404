import random


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score / 10))


def get_valid_score():
    while True:
        score = float(input("Enter a valid score (0-100): "))
        if score >= 0 and score <= 100:
            return score
        else:
            print("Invalid score")


def print_menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    score = get_valid_score()
    status = determine_score_status(score)

    while True:
        print_menu()
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
            status = determine_score_status(score)
        elif choice == "P":
            print(status)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
