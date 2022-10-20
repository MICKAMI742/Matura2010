# wczytanie do pliku
f = open("anagram.txt", "r")
w = open("odp_4a.txt", "w")
list = []

# przepisanie danych do listy
for line in f.readlines():
    list.append(line)

numberOfLetters = 0
# tablica która zapsisuje długość jednego słowa w wierszu jako jeden element
listOfLetterNumberInWord = []

for line in list:
    for i in line:
        if i == " " or i == "\n":
            listOfLetterNumberInWord.append(numberOfLetters)
            numberOfLetters = 0
        else:
            numberOfLetters += 1
    # sprawdzenie czy wszystkie elementy w zbiorze są identyczne
    result = all(elements == listOfLetterNumberInWord[0] for elements in listOfLetterNumberInWord)
    # jesli tak zapisujemy linie do pliku
    if result:
        w.write(line)
    # po kazdym przejsciu do nastepnego wiersza czyszcze tablice
    listOfLetterNumberInWord.clear()
f.close()  
w.close()