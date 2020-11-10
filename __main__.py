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
    sql = "INSERT INTO uczen (id_ucznia, karta, imie, nazwisko, id_klasy_fk) VALUES(NULL, %s, %s, %s, (SELECT id_klasy FROM klasa WHERE nazwa_klasy = %s))"
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
    #skończe to jutro dzisiaj hur dur
    lesson_id = input("Podaj id klasy: ")
    database.close()

def addclass():
    #trudno tu coś spierdolić
    class_name = input("Podaj nazwe klasy: ")

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )
    mycursor = database.cursor()
    variables = [class_name]
    sql = "INSERT INTO klasa (id_klasy, nazwa_klasy) VALUES(NULL, %s)"
    mycursor.execute(sql, variables)
    database.commit()
    database.close()

def choice():
    print("Dostępne funkcje: \n1. Sprawdź obecność\n2. Dodaj ucznia\n3. Dodaj klasę\n4. Dodaj lekcję")
    user_choice = input("Wybierz, co chcesz zrobić: ")
    if user_choice == "1":
        check_presence()
    elif user_choice == "2":
        addstudent()
    elif user_choice == "3":
        addclass()
    elif user_choice == "4":
        addlesson()
    else:
        print("DEBUG. Wrong choice")


def addlesson():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )

    mycursor = database.cursor()
    gn = 0
    przedmiot = 0
    dic = 0
    klasa = 0
    sala = 0
    #whileuje sie ile chcesz
    while gn == 0:
        przedmiot = input("Podaj nazwę przedmiotu: ")
        dic = input("Podaj date i czas rozpoczecia(rrrr-mm-dd gg-mm-ss): ")
        klasa = input("Podaj klasę: ")
        sala = input("Podaj salę: ")
        print("Przedmiot: " + przedmiot + "\nData i czas: " + dic + "\nKlasa: " + klasa + "\nSala: " + sala)
        czk = input("Jeśli jest git wpisz 1: ")
        if czk == '1':
            gn = 1

    sala = int(sala)

    #wrzucanie do bazy danych
    variables = [przedmiot, dic, klasa, sala]

    sql = "INSERT INTO lekcja (id_lekcji, id_przedmiotu_fk, id_dic_fk,id_klasy_fk, id_sali_fk)" \
          "VALUES(NULL, (SELECT id_przedmiotu FROM przedmiot WHERE nazwa_przedmiotu = %s)," \
          "(SELECT id_dic FROM dataiczas WHERE dic_start = %s)," \
          "(SELECT id_klasy FROM klasa WHERE nazwa_klasy = %s)," \
          "(SELECT id_sali FROM sala WHERE numer_sali = %s))"
    mycursor.execute(sql, variables)
    database.commit()

    #wrzuca na ekran dodany wpis, no chyba że źle wpisałeś to najnowszy
    mycursor.execute("SELECT * FROM lekcja order by id_lekcji desc limit 1")
    for x in mycursor:
        print(x)

    database.close()


def main():
    choice()


if __name__ == "__main__":
    main()
