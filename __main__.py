import mysql.connector
from datetime import datetime


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
    mycursor = database.cursor(buffered=True)
    mycursor.execute("SELECT * FROM klasa")
    for x in mycursor:
        print(x)
    student_class = input("Podaj klase: ")
    variables = [card_id, first_name, last_name, student_class]
    sql = "INSERT INTO uczen (id_ucznia, karta, imie, nazwisko, id_klasy_fk) VALUES(NULL, %s, %s, %s," \
          " (SELECT id_klasy FROM klasa WHERE nazwa_klasy = %s))"
    mycursor.execute(sql, variables)
    database.commit()
    database.close()


def check_presence():
    # otwieranie połączenia
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )

    # sprawdza czy podana sala istnieje jesli nie sprawdza do skutku
    nr_sali = 0
    while nr_sali == 0:
        nr_sali = int(input("Podaj numer sali: "))
        var_nr_sali = [nr_sali]
        q_nr_sali = "SELECT * FROM sala WHERE numer_sali = %s"
        mycursor = database.cursor(buffered=True)
        mycursor.execute(q_nr_sali, var_nr_sali)
        chk_nr_sali = mycursor.rowcount
        if chk_nr_sali != 1:
            print("Podano zły numer sali")
            nr_sali = 0
        else:
            elo = 1

            # sprawdza czy do sali jest przypisana lekcja
            while elo == 1:
                time_now = datetime.now()
                var_lekcja = [time_now, time_now, nr_sali]
                q_lekcja = "SELECT lekcja.id_lekcji, sala.numer_sali, dataiczas.dic_start, dataiczas.dic_stop," \
                           " klasa.nazwa_klasy, przedmiot.nazwa_przedmiotu " \
                           "FROM ((((lekcja LEFT JOIN dataiczas ON dataiczas.id_dic=lekcja.id_dic_fk) " \
                           "LEFT JOIN sala ON sala.id_sali=lekcja.id_sali_fk) " \
                           "LEFT JOIN klasa ON klasa.id_klasy=lekcja.id_klasy_fk)" \
                           "LEFT JOIN przedmiot ON przedmiot.id_przedmiotu=lekcja.id_przedmiotu_fk)" \
                           "WHERE dataiczas.dic_start < %s AND dataiczas.dic_stop > %s AND sala.numer_sali = %s"
                mycursor.execute(q_lekcja, var_lekcja)
                chk_lekcja = mycursor.rowcount
                if chk_lekcja != 1:
                    input("Nie ma lekcji w tej sali\n Kliknij Enter aby sprawdzić ponownie...")

                # jeśli jest przypisana pokazuje jej wartości i pozwala zczytać kartę
                else:
                    for x in mycursor:
                        wp_lekcja = x
                    d0 = time_now.strftime("%H:%M")
                    d1 = wp_lekcja[2].strftime("%H:%M")
                    d2 = wp_lekcja[3].strftime("%H:%M")
                    print("Sala: " + str(wp_lekcja[1]) + "\nAktualny czas: " + d0 + "\nRozpoczęcie lekcji: " + d1 +
                          "\nKoniec lekcji: " + d2 + "\nKlasa: " + wp_lekcja[4] + "\nPrzedmiot: " + wp_lekcja[5])
                    benc = 1
                    while benc == 1:
                        nr_karty = int(input("Przyłóż karte: "))
                        var_uczen = [nr_karty]

                        # wprowadzenie 0 sprawdza ponownie status lekcji, a poniżej kończy funkcję
                        if nr_karty == 0:
                            benc = 0
                        elif nr_karty < 0:
                            elo = 0
                            benc = 0

                        # następnie sprawdza ucznia, najpierw czy istnieje a potem
                        # czy lekcja przypisana do sali jest dla jego klasy
                        else:
                            q_uczen = "SELECT uczen.id_ucznia, uczen.karta, uczen.imie, uczen.nazwisko," \
                                      " klasa.nazwa_klasy " \
                                      "FROM uczen LEFT JOIN klasa ON uczen.id_klasy_fk = klasa.id_klasy WHERE" \
                                      " karta = %s"
                            mycursor.execute(q_uczen, var_uczen)
                            chk_uczen = mycursor.rowcount
                            if chk_uczen == 0:
                                print("Nie znaleziono ucznia z tą kartą")
                            else:
                                for x in mycursor:
                                    print(x)
                                    wp_uczen = x
                                if wp_uczen[4] != wp_lekcja[4]:
                                    print("Chyba klasy ci się pomyliły XD")

                                # Jęśli wszystko się zgadza sprawdza czy uczen ma już wpisana
                                # obecnosc a jesli nie wpisuje ja
                                else:
                                    q_preputis = "SELECT * FROM wpis WHERE id_lekcji_fk = %s AND id_ucznia_fk = %s"
                                    var_preputis = [wp_lekcja[0], wp_uczen[0]]
                                    mycursor.execute(q_preputis, var_preputis)
                                    chk_puttis = mycursor.rowcount
                                    if chk_puttis == 1:
                                        print("Już masz obecność XD")
                                    else:
                                        var_putis = [wp_lekcja[0], wp_uczen[0], 1]
                                        q_putis = "INSERT INTO wpis (id_lekcji_fk, id_ucznia_fk, obecnosc)" \
                                                  " VALUES (%s ,%s , %s)"
                                        mycursor.execute(q_putis, var_putis)
                                        database.commit()
                                        print("Dodano obecność byczku")
                                        var_end = [wp_lekcja[0], wp_uczen[0]]
                                        q_end = "SELECT * FROM wpis WHERE id_lekcji_fk = %s AND id_ucznia_fk = %s"
                                        mycursor.execute(q_end, var_end)

    # kończenie połączenia z bazą
    database.close()


def addclass():
    # trudno tu coś *REDACTED*
    class_name = input("Podaj nazwe klasy: ")

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="presence_check"
    )
    mycursor = database.cursor(buffered=True)
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

    mycursor = database.cursor(buffered=True)
    gn = 0
    przedmiot = 0
    dic = 0
    klasa = 0
    sala = 0
    # whileuje sie ile chcesz
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

    # wrzucanie do bazy danych
    variables = [przedmiot, dic, klasa, sala]

    sql = "INSERT INTO lekcja (id_lekcji, id_przedmiotu_fk, id_dic_fk,id_klasy_fk, id_sali_fk)" \
          "VALUES(NULL, (SELECT id_przedmiotu FROM przedmiot WHERE nazwa_przedmiotu = %s)," \
          "(SELECT id_dic FROM dataiczas WHERE dic_start = %s)," \
          "(SELECT id_klasy FROM klasa WHERE nazwa_klasy = %s)," \
          "(SELECT id_sali FROM sala WHERE numer_sali = %s))"
    mycursor.execute(sql, variables)
    database.commit()

    # wrzuca na ekran dodany wpis, no chyba że źle wpisałeś to najnowszy
    mycursor.execute("SELECT * FROM lekcja order by id_lekcji desc limit 1")
    for x in mycursor:
        print(x)

    database.close()


def main():
    choice()


if __name__ == "__main__":
    main()
