import getpass
import pickle
import os
import sys
import six
import statistics
from statistics import mean


def login():
    user = input("Username: ")
    passw = getpass.getpass("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print("Login successful!")
            return True
    print("Wrong username/password")
    return False


def menu():
    ChrMenu1 = "="
    ChrMenu2 = " "
    ChrMenu3 = "||"
    print(ChrMenu1 * 42)
    print(ChrMenu3, ChrMenu2 * 36, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 36, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 4, "[1] - Add Student", ChrMenu2 * 13, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 4, "[2] - Add Grades", ChrMenu2 * 14, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 4, "[3] - Student Average Grades", ChrMenu2 * 2, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 4, "[4] - Delete Student", ChrMenu2 * 10, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 4, "[5] - Exit", ChrMenu2 * 20, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 36, ChrMenu3)
    print(ChrMenu3, ChrMenu2 * 36, ChrMenu3)
    print(ChrMenu1 * 42)
    print('\n')

    options = {
        1: AddStu,
        2: AddGrad,
        3: AveGrad,
        4: DelStu,
        5: exit,
    }

    # num = int(input("Good Day! What do you want to do?: "))
    msg = "Good Day! What do you want to do?: "
    # print (msg)
    num = is_string(msg)
    options[num]()


def readDB():
    my_path = 'GradesDB.txt'

    if not os.path.exists(my_path):
        Conti = str(input("You dont have any Student, do you want add one? [y/n]:"))

        if Conti == "y":
            AddStu()
        elif Conti == "n":
            menu()
        else:
            print("Please use Y or N ")
            readDB()

    file = open('GradesDB.txt', 'rb')
    DicSch = pickle.load(file)
    print(DicSch)


def writeDB(GravaVal):
    file = open('GradesDB.txt', 'wb')
    pickle.dump(GravaVal, file)
    file.close()


def AveGrad():
    print("This is the current Students, With one do you want the Average: ")
    readDB()
    file = open('GradesDB.txt', 'rb')
    DicSch = pickle.load(file)
    StuNa = input("Tell me the Student's Name: ")
    print(StuNa, "Let do!")
    AveStu = DicSch[StuNa]
    print(AveStu)
    AveStu = mean(AveStu)
    print("{} Average is {}".format(StuNa, AveStu))
    menu()


def AddGrad():
    print("This is the current Students, With one do you want add some Grade: ")
    readDB()
    file = open('GradesDB.txt', 'rb')
    DicSch = pickle.load(file)

    StuNa = input("Tell me the Student's Name: ")
    print(StuNa, "Right!")
    msg = "How many Grades do you want add?: "
    GraNu = is_string(msg)
    for i in range(GraNu):
        print("{} of {} to over:".format(str(i + 1), str(GraNu)))
        Gra = float(input("Grade: "))
        DicSch[StuNa].append(Gra)

        if i + 1 == GraNu:
            Conti = str(input("Do you want continue? [y/n]:"))
            if Conti == "y":
                GravaVal = DicSch
                writeDB(GravaVal)
                AddGrad()
    GravaVal = DicSch
    writeDB(GravaVal)
    menu()


def AddStu():
    my_path = 'GradesDB.txt'
    print("This is the current Students: ")
    readDB()
    if not os.path.exists(my_path):
        DicSch = {}
        StuNa = input("Tell me the Name of your First Student:")
        DicSch[StuNa] = []
        GravaVal = DicSch
        writeDB(GravaVal)
        Conti = str(input("Do you want continue? [y/n]:"))
        if Conti == "y":
            AddStu()


    else:

        file = open('GradesDB.txt', 'rb')
        DicSch = pickle.load(file)
        msg = "how many studants do you want add?: "
        StuAddNum = is_string(msg)
        for i in range(StuAddNum):
            StuNa2 = input("Tell me the Student's Name: ")
            DicSch[StuNa2] = []
            print(DicSch)

    GravaVal = DicSch
    writeDB(GravaVal)

    menu()


def DelStu():
    print("This is the current Students: ")
    readDB()
    file = open('GradesDB.txt', 'rb')
    DicSch = pickle.load(file)
    msg = "how many studants do you want delete?: "
    StuAddNum = is_string(msg)
    for i in range(StuAddNum):
        StuNa2 = input("Tell me the Student's Name: ")
        DicSch.pop(StuNa2, None)
        print(DicSch)
        GravaVal = DicSch
        writeDB(GravaVal)
    menu()


def is_string(var_input):
    while True:
        try:
            # print(var_input)
            return int(input(var_input))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def main():
    log = login()
    if log is True:
        menu()


DicSch = {}
main()
