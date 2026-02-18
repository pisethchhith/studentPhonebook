# Student Phonebook

# build interface 
    # Welcoming title
    # 1. New file
    # 2. Open File
    # 3. Exit
# in New file: create csv file with table and edit
    # Name
    # Telephone
    # then show interface
        # 1.Go back
        # 2.Exit
# in Open file: open csv file and edit previous file
    # interface
        # 1. Add student
        # 2. Go back
# Libraries I used: csv, sys, time, tabulate

import sys
import time
import csv
from tabulate import tabulate

def main():
    interface()

def interface():
    animation("=============== Welcome to students' handbook ===============")
    print("""
1. New file
2. Open file
3. Exit
""")
    while True:
        user = input("Enter: ")
        if user == "1":
            newFile()
            break
        elif user == "2":
            openFile()
            break
        elif user == "3":
            sys.exit()
        else:
            print("Invalid Enter")
            pass

def openFile():
    try:
        name = input("Name File: ")
        csvFile = f"{name}.csv"
        previewFile(csvFile)
        print("""
1. Add Student
2. Go back
""")
        user = input("Enter: ")
        if user == "1":
            try:
                addFile(csvFile)
            except(KeyboardInterrupt, EOFError):
                print()
                previewFile(csvFile)
                print("""
1. Go back
2. Exit
""")
            user = input("Enter: ")
            if user == "1":
                interface()
            elif user == "2":
                sys.exit()
    

        elif user == "2":
            interface()
    except FileNotFoundError:
        print("File does not exit")



def newFile():
    nameFile = input("Name file: ")
    csvFile = f"{nameFile}.csv"
    
    try:
        writeNewFile(csvFile)
    except(KeyboardInterrupt, EOFError):
        print()
        previewFile(csvFile)
        print("""
1. Go back
2. Exit
""")
        user = input("Enter: ")
    if user == "1":
        interface()
    elif user == "2":
        sys.exit()
    


def writeNewFile(csvFile):
    with open(csvFile, "a") as file:
        header = ["Student", "Phone Number"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        while True:
            studentName = input("Student Name: ")
            phoneNumber = input("Phone Number: ")
            writer.writerow({"Student": studentName, "Phone Number": phoneNumber})

def addFile(csvFile):
    with open(csvFile, "a") as file:
        header = ["Student", "Phone Number"]
        writer = csv.DictWriter(file, fieldnames=header)
        while True:
            studentName = input("Student Name: ")
            phoneNumber = input("Phone Number: ")
            writer.writerow({"Student": studentName, "Phone Number": phoneNumber})


def previewFile(csvFile):
    with open(csvFile, "r") as table:
        table = csv.reader(table)
        display = tabulate(table, headers="firstrow", tablefmt="double_grid")
        print(display)


def animation(text, delay=0.05):
    for char in text:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print()
    

if __name__ == "__main__":
    main()
        


