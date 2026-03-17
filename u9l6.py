class Customer:
    def __init__(self,name,cid,phone,age):
        self.name=name
        self.cid=cid
        self.phone=phone
        self.age=age

class BookMyShow:
    movie="Dhurandhar"
    code="FREE15"
    def __init__(self,tid):
        self.tid=tid  

    def billing(self):
        coupon=input('Enter the coupon: ')
        seat=input('select your seat category: ')
        price=0
       
        category={
            'high':750,
            'medium':500,
            'low':250
            }
        if coupon==BookMyShow.code:
            price+=category[seat]
            total=price-(price*0.15)
        else:
            print('Invalid coupon')
        return total

c1=BookMyShow(101)
c2=BookMyShow(102)
c3=BookMyShow(103)
c4=BookMyShow(104)
queue=[c1,c2,c3,c4]
for obj in queue:
    print(obj.billing())