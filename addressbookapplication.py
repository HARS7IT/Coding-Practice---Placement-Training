import sqlite3
dbpath="C:\\Users\\Harshit\\Desktop\\PYTHON\\academy.db"
connection=sqlite3.connect("dbpath")
cursor=connection.cursor()
class AddressBook:
    def giveContactDetails(self):
        contactName=input("Enter person name: ")
        emailid=input("Enter email: ")
        address=input("Enter address: ")
        return{"name" : contactName, "email" : emailid, "address" : address}
def main():
    connection=sqlite3.connect("academy.db")
    cursor=connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS contactdetails (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   emailTEXT UNIQUE NOT NULL,
                   addressTEXT NOT NULL
                )
            ''')
    connection.commit()
    choice='y'
    while choice.lower()=='y':
        print("1. Add New Contact\n2.Display Contacts\n3.Total Contacts Count")
        response = int(input("Enter your choice: "))
        if response == 1:
            contact1 = AddressBook()
            contact = contact1.giveContactDetails()

            cursor.execute('''
                           INSERT INTO contactdetails (name,email,address)
                           VALUES (?, ?, ?)
                           ''', (contact['name'], contact['email'], contact['address']))
            connection.commit()
            print("Contact successfully added")
        elif response == 2:
            cursor.execute("SELECT name, email, address FROM contactdetails")
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"{Name: (row[0]), Email: (row[1]), Address: (row[2])}\n")
            else:
                print("No contacts found!")
        elif response == 3:
            cursor.execute("SELECT COUNT(*) AS totalCountInDB FROM contactdetails")
            result =cursor.fetchall()
            print("totalcount", result)
        else:
            print("Please check your response")
        choice = input("Press'y' to continue, any other key tp exit: ")
    connection.close()
if __name__ == "__main__":
    main()
