import mysql.connector


def addstudent():
    card_id = int(input("Wczytaj kartę: "))
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )
    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM klasa")
    for x in mycursor:
        print(x)
    student_class = input("Podaj klase: ")
    variables = [card_id, first_name, last_name, student_class]
    sql = "INSERT INTO uczen (id_ucznia, karta, imie, nazwisko, id_klasy) VALUES(NULL, %s, %s, %s, %s)"
    mycursor.execute(sql, variables)
    database.commit()
    database.close()


def addclass():
    class_name = input("Podaj nazwe klasy: ")

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )
    mycursor = database.cursor()
    variables = [class_name]
    sql = "INSERT INTO klasa (id_klasy, klasa) VALUES(NULL, %s)"
    mycursor.execute(sql, variables)
    database.commit()
    database.close()


def check_presence():
    # tutaj będzie pobierało wszystkie klasy i je wypisywalo
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )
    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM klasa ")
    for x in mycursor:
        print(x)
    lesson_id = input("Podaj id klasy: ")
    database.close()


def choice():
    print("Dostępne funkcje: \n1. Sprawdź obecność\n2. Dodaj ucznia\n3. Dodaj klasę")
    user_choice = input("Wybierz, co chcesz zrobić: ")
    if user_choice == "1":
        check_presence()
    elif user_choice == "2":
        addstudent()
    elif user_choice == "3":
        addclass()
    else:
        print("DEBUG. Wrong choice")


def main():
    choice()


if __name__ == "__main__":
    main()
