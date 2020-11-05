
def choice():
    print("Dostępne funkcje: \n1. Sprawdź obecność")
    user_choice = input("Wybierz, co chcesz zrobić: ")
    if user_choice == "1":
        print("DEBUG. 1")
    elif user_choice == "2":
        print("DEBUG. 2")
    else:
        print("DEBUG. Wrong choice")


def main():
    choice()


if __name__ == "__main__":
    main()
