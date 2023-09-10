class Node: #this class represents individual elements in the linked list
    def __init__(self, data = None, next = None): #it has two class members... data and next..data can contain int, complex numbers
        self.data = data #self.data is a variable..
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None # we need a head variable ..which point to the head of link list

    def insert_at_begning(self, data):
        # it is taking data value and inserting that at the begning of the linked list
        # self.head = 5
        node = Node(data, self.head) #5, none
        self.head = node

    #we need a fnction to print =the linkedlist
    def print(self):
        # self.head = 10
        if self.head is None: #if i have a blank link list
            print("Empty link list")
            return
        itr = self.head #iterator variable
        llstr = ""

        while itr:
            llstr += str(itr.data) + "->"
            itr = itr.next 
        print(llstr)

ll = LinkedList()
# print(ll)
ll.insert_at_begning(5)
ll.insert_at_begning(7)
ll.insert_at_begning(8)
ll.print()