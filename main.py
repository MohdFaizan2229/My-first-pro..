import sqlite3
conn =sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(roll_no INTEGER PRIMARY KEY,
name TEXT,
branch TEXT,
semester INTEGER,
marks REAL)""")

conn.commit()
conn.close()
while True:
    print("\n===Student Management System===")
    print("1. Add Students")
    print("2. View Students")
    print("3. Serach Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Exit")

    choice = input("Enter Your Choice :")
    if choice == "1":
        roll_no = int(input("Enter the roll no :"))
        name = (input("Enter the Name :"))
        branch =(input("Enter the Branch :"))
        semester = int(input("Enter the Semester :"))
        marks = float(input("Enter the Marks :"))

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO STUDENTS(roll_no,name,branch,semester,marks)
        values(?,?,?,?,?)""",(roll_no,name,branch,semester,marks))

        conn.commit()
        conn.close()
        print("student Added Successfully !")

        print("Add Students")

    elif choice == "2":
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("\n===== All Students====")

        for student in students:
             print("Roll No:",student[0])
             print("Name:",student[1])
             print("Branch:",student[2])
             print("Smester",student[3])
             print("Marks",student[4])

        print("----Successfully View----")
        conn.close()
    
    elif choice == "3":
        roll_no = int(input("Enter Roll No to search :"))
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students Where roll_no = ?", (roll_no,))
        student = cursor.fetchone()

        if student:
                print("\n===Student Found===")
                print("Roll_No ;",student[0])
                print("Name:",student[1])
                print("Branch:",student[2])
                print("Semester:",student[3])
                print("Marks:",student[4])
        else:
           print("Student Not Found")
        
        conn.close()
    elif choice == "4":
     roll_no = int(input("Enter the Roll No to update :"))

     name = input("Enter the New Name :")
     branch = input("Enter the New Branch :")
     semester = int(input("Enter the New Semester :"))
     marks = float(input("Enter the marks :"))
     
     conn =sqlite3.connect("students.db")
     cursor = conn.cursor()

     cursor.execute("""UPDATE students
     SET name = ?,
     branch = ?,
     semester = ?,
     marks = ?
     WHERE roll_no = ?""",(name,branch,semester,marks,roll_no))

     conn.commit()
     print("Student Update Successfully!")

    elif choice == "5":
        roll_no = int(input("Enter the Roll No to Delete :"))

        conn =sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE roll_no = ? ",(roll_no,))

        conn.commit()
        if cursor.rowcount > 0:
            print("Students Deleted Successfully!")
           

    elif choice == "6":
        print("Thank You for Using Student Management System!")
        print("Successfully Exit!") 
    break

else:

        print("Invalid choice")       



