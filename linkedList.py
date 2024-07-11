#linked list implementation in python

'''In LinkedList class that we implemented in our tutorial add following two methods,
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
Now make following calls,

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index for insert at method")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0 
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    #insert after value in linked list
    def insert_after_value(self, data_after, data_to_insert):

        if self.head is None:
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return

            itr = itr.next
    
        # If data_after is not found in the list
        raise ValueError("Data '{}' not found in the linked list".format(data_after))
    

    #remove by value in linked list
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(45)
    ll.insert_at_end(71)
    ll.insert_at_end(23)
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    # print(f"length of the linked list is : {ll.get_length()}")
    # ll.remove_at(2)

    # ll.insert_at(0 ,"Strawberry")
    ll.insert_after_value("mango", "apple")
    ll.remove_by_value("banana")
    ll.print()


    