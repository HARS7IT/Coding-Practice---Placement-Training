class Hospital:
  

    def isAvailable(self,date):

        slots={
        10:True,
        11:False,
        12:False,
        13:True
        }
    
        if slots[date] == True:
          print(f"on {date} Slot booked successfully")
        else:
          print(f"on {date} Slot not available")



    def __init__(self,pid,name,room,age):
        self.pid=pid
        self.name=name
        self.room=room
        self.age=age
pid=int(input("Enter patient id: "))
name=input("Enter patient name: ")
room=int(input("Enter patient room: "))
age=int(input("Enter patient age: "))

p1=Hospital(pid,name,room,age)
date=int(input("Enter date: "))
p1.isAvailable(date)