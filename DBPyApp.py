import sqlite3

def main():
    user_option = ""

    conn = sqlite3.connect('StudentDataBase.sqlite') #file path

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS 
                Students(
                StudentId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                FistName VARCHAR(25), 
                LastName VARCHAR(25), 
                GPA REAL, 
                Major VARCHAR(10), 
                FacultyAdvisor VARCHAR(25));
                ''')


    while True:

        user_option = int(input("Enter 1 to display all students with their attributes\nEnter 2 to create a new students\nEnter 3 to update existing students\nEnter 4 to remove students\nEnter 5 to search for students\nEnter 0 to quit"))

        if user_option == 1: #display all students
           displayAll(c)

        elif user_option == 2: #create student
            createStudent(c)

        elif user_option == 3: #update student
            updateStudent(c)
        elif user_option == 4: #remove student
            deleteStudent(c)
        elif user_option == 5: #search for students
            searchStudents(c)
        elif user_option == 0:  # search for students
            conn.commit()
            conn.close()
            break
        else:
            print("Invalid input")
            continue
        conn.commit()


def displayAll(cursor):
    cursor.execute("SELECT * FROM Students")
    data = cursor.fetchall()
    for row in data:
        print(row)

def createStudent(cursor):
    try:
        fName = raw_input("Enter first name: ")
        lName = raw_input("Enter last name: ")
        gpa = float(input("Enter GPA: "))
        major = raw_input("Enter major: ")
        advisor = raw_input("Enter faculty advisor: ")
    except:
        print("Invalid input")
        return
    cursor.execute(
        "INSERT INTO Students(FistName, LastName, GPA, Major, FacultyAdvisor) VALUES (?, ?, ?, ?, ?)",
        (fName, lName, gpa, major, advisor))


def updateStudent(cursor):

    try:
        id = int(input("Enter the ID of the student to update: "))
    except:
        print("Invalid input")
        return
    try:
        choice = int(input("Enter 1 to update major, 2 to update advisor: "))
    except:
        print("Invalid input")
        return

    if choice == 1:
        newMajor = raw_input("Enter the new major: ")
        cursor.execute("UPDATE Students SET Major = ? WHERE StudentId = ?", (newMajor, id))
    elif choice == 2:
        newAdviosr = raw_input("Enter the new advisor: ")
        cursor.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentId = ?", (newAdviosr, id))

def deleteStudent(cursor):
    try:
        id = int(input("Enter the ID of the student to delete: "))
    except:
        print("Invalid input")
        return
    cursor.execute("DELETE FROM Students WHERE StudentId = ?", id)

def searchStudents(cursor):
    option = int(input("Enter 1 to search by major, 2 to search by GPA, and 3 to search by advisor: "))
    if option == 1:
        major = raw_input("Enter the major: ")
        cursor.execute("SELECT * FROM Students WHERE Major = ?", major)
    elif option == 2:
        gpa = float(input("Enter the GPA: "))
        cursor.execute("SELECT * FROM Students WHERE GPA = ?", gpa)
    elif option == 3:
        advisor = raw_input("Enter the Advisor: ")
        cursor.execute("SELECT * FROM Students WHERE FacultyAdvisor = ?", advisor)
    else:
        print("Invalid input")
        return

    data = cursor.fetchall()
    for row in data:
        print(row)


main()