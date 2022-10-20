f = open("anagram.txt", "r")
w = open("odp_4b.txt", "w")

list = []
listOfWords = []
listOfRows = []
word = ""


def makeListOfRows(f):
    # ustalam word jako zmienna o globalnym zasiegu
    global word
    for line in f.readlines():
        list.append(line)
    for line in list:
        word = ""
        for letters in line:
            if letters == " " or letters == "\n":
                listOfWords.append(word)
                word = ""
            else:
                word += letters
    i = 0
    j = 5
    # tworzę liste z wierszami
    while j <= len(listOfWords):
        listOfRows.append(listOfWords[i:j])
        i += 5
        j += 5
    return listOfRows


def isAnagram(listOfRows):
    for rows in listOfRows:
        if (all(sorted(ele) == sorted(rows[0]) for ele in rows)):
            w.write(str(rows) + "\n")


def main():
    makeListOfRows(f)
    isAnagram(listOfRows)


if __name__ == "__main__":
    main()

f.close()
w.close()
