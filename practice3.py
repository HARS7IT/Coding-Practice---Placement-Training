#linked list

class node:
    def _init_(self,data):
        self.data=data
        self.next=none
class LinkedList:
    def _init_(self):
        self.head=none

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None


    def search_element(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    
    def reverse_element(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev

            prev=current
            current=next_node
        self.head=prev
            

    